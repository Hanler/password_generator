# Project <Password generator>
# Made by Danil Khmelnytskyi
# 25.01.2022

# Use this to install dependencies:
# pip install pyqt5
# pip install cryptography

import os
import random
from design import ClssDialog
from dict import dict_translitaration, letters_eng
from cryptography.fernet import Fernet
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from design import Ui_MainWindow
import sys

def prepareWord(string):
    """
    Convert word or phrase to lowercase and delete spaces
    """
    string = string.lower()
    string = string.replace(" ", "")
    return string

def text2translit(string):
    """
    Convert an input word in Cyrillic to Roman by translit
    """
    translatedLetters = []
    arrayLetters = list(string)
    for letter in arrayLetters:
        translatedLetters.append(dict_translitaration[letter])
    res = "".join(translatedLetters)
    return res

def distortWord(string, leet=False):
    """
    Distort an input word according to the rules
    """
    if leet:
        # to leet abbreviation
        string = string.replace("for", "4") # for - four [for]
        string = string.replace("and", "&") # and - &
        string = string.replace("anned", "&") # anned - &
        string = string.replace("ant", "&") # ant - &
        string = string.replace("ed", "'d") # ed - 'd
        string = string.replace("er", "xor") # er - xor
        string = string.replace("or", "xor") # or - xor
    else:
        # to nums
        string = string.replace("for", "4") # for - four [for]
        string = string.replace("to", "2") # to - two [too]
        string = string.replace("th", "3") # th - three
        string = string.replace("sh", "#") # sh - sharp
        string = string.replace("f", "5") # f - five
        string = string.replace("a", "@") # a - @
        string = string.replace("d", "$") # d - dollar
        string = string.replace("p", "%") # p - percent
        string = string.replace("o", "0") # o - 0
        string = string.replace("s", "6") # s - six
        string = string.replace("n", "9") # n - nine
        string = string.replace("e", "8") # e - eight
        string = string.replace("m", "-") # m - - (minus)
    return string

def makeLong(string):
    """
    Check the length of the word. If it is need, make longer
    """
    while len(string) < 6:
        if string.count("age") == 0:
            string += "age"
        else:
            string += "ness"
    return string

def toUpper(string):
    """
    Convert random letter of the word to uppercase
    """
    length = len(string)
    lettersInWord = list(string)
    while True:
        rnd = random.randint(0, length-1)
        if lettersInWord[rnd] in letters_eng:
            lettersInWord[rnd] = lettersInWord[rnd].upper()
            break
    string = "".join(lettersInWord)
    return string

# Security block

def writeKey():
    """
    Create key and save it in a file
    """
    key = Fernet.generate_key()
    with open('crypto.key', 'wb') as key_file:
        key_file.write(key)

def loadKey():
    """
    Load key 'crypto.key' from the directory
    """
    return open('crypto.key', 'rb').read()

def encryptFile(filename, key):
    """
    Encrypt file and write it
    """
    f = Fernet(key)

    with open(filename, 'rb') as file:
        # read all data
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, 'wb') as file:
        file.write(encrypted_data)

def encryptData(filename, key, file_data):
    """
    Encrypt data and write it
    """
    f = Fernet(key)

    encrypted_data = f.encrypt(file_data)

    with open(filename, 'wb') as file:
        file.write(encrypted_data)

def decryptFile(filename, key):
    """
    Decrypt file and save it
    """
    f = Fernet(key)
    with open(filename, 'rb') as file:
        # read encrypred data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)

    # write original file
    with open(filename, 'wb') as file:
        file.write(decrypted_data)

def decryptData(filename, key):
    """
    Decrypt data from file and return it
    """
    f = Fernet(key)
    with open(filename, 'rb') as file:
        # read encrypred data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)

    return decrypted_data

def randomPassword(number=1, length=6):
    """
    Generate random password by choosing random chars from string
    """
    chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for n in range(number):
        password = ''
        for i in range(length):
            password += random.choice(chars)
    return password
 
# GUI start
class mywindow(QtWidgets.QMainWindow):
    """
    Contains generated window with widgets
    """
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.simpleGenerate)
        self.ui.pushButton_2.clicked.connect(self.difficultGenerate)
        self.ui.pushButton_5.clicked.connect(self.randomGenerate)
        self.ui.pushButton.clicked.connect(self.copyPassword)
        self.ui.pushButton_4.clicked.connect(self.savePassword)
        self.ui.tabWidget.tabBarClicked.connect(self.fillTable)
        self.ui.pushButton_6.clicked.connect(self.fillTable)

    def simpleGenerate(self):
        """
        Get data from QLineEdit, generate password (simple generating - leet) and set it to Label
        """
        inputWord = self.ui.lineEdit.text()
        self.whichPlatform = self.ui.lineEdit_2.text()

        normalizedWord = prepareWord(inputWord)
        translatedWord = text2translit(normalizedWord)
        distortedWord = distortWord(translatedWord, True)
        notShortWord = makeLong(distortedWord)
        upperedWord = toUpper(notShortWord)

        self.ui.label_4.setText(upperedWord)

    def difficultGenerate(self):
        """
        Get data from QLineEdit, generate password (difficult generating - more rules) and set it to Label
        """
        inputWord = self.ui.lineEdit.text()
        self.whichPlatform = self.ui.lineEdit_2.text()

        normalizedWord = prepareWord(inputWord)
        translatedWord = text2translit(normalizedWord)
        distortedWord = distortWord(translatedWord)
        notShortWord = makeLong(distortedWord)
        upperedWord = toUpper(notShortWord)

        self.ui.label_4.setText(upperedWord)

    def randomGenerate(self):
        """
        Get generated password (random generating - chars from string) and set it to Label
        """
        self.whichPlatform = self.ui.lineEdit_2.text()
        generatedWord = randomPassword()
        self.ui.label_4.setText(generatedWord)

    def copyPassword(self):
        """
        Copy generated password from Label to clipboard
        """
        password = self.ui.label_4.text()
        command = 'echo ' + password.strip() + '| clip'
        os.system(command)

    def openDialog(self):
        """
        Open dialog window to inform the user
        """
        dialog = ClssDialog(self)
        dialog.exec_()

    def savePassword(self):
        """
        Save generated password from Label to local database
        """
        password = self.ui.label_4.text()

        key = loadKey() # load the key
        file = 'data.txt' # name of file to crypt

        data = decryptData(file, key)
        dataNew = data + b'Platform: ' +  bytes(str(self.whichPlatform), encoding='utf8') + b' | Password: ' + bytes(str(password), encoding='utf8') + b'\r\n'
        encryptData(file, key, dataNew)
        self.openDialog()

    def fillTable(self):
        """
        Fill table with the data from local DB
        """
        key = loadKey() # load the key
        file = 'data.txt' # name of file to crypt

        data = decryptData(file, key) # decrypting data from file
        data = str(data, encoding='utf8')
        newArr = data.split("\r\n") # convert data
        dividedItemArr = []
        for item in newArr:
            dividedItemArr.append(item.split(" | "))
        
        self.ui.tableWidget.clear()
        rows = len(dividedItemArr) - 1
        self.ui.tableWidget.setRowCount(rows)
        self.ui.tableWidget.setColumnCount(2)

        for row in range(len(dividedItemArr)):
            for col in range(len(dividedItemArr[row])):
                item = dividedItemArr[row][col].replace("Platform: ", "")
                item = item.replace("Password: ", "")
                cellinfo = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(row, col, cellinfo)

if "__main__" == __name__:
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    
    filePathFile = "data.txt"
    filePathKey = "crypto.key"

    if not os.path.exists(filePathKey):
        writeKey()
    if not os.path.exists(filePathFile):
        f = open('data.txt', 'tw', encoding='utf-8')
        f.close()
        key = loadKey() # load the key
        file = 'data.txt' # name of file to crypt
        encryptFile(file, key) # crypt the file

    # writeKey() # create key (need to run ones only)

    # key = loadKey() # load the key
    # file = 'data.txt' # name of file to crypt

    # encryptFile(file, key) # crypt the file
    # decryptFile(file, key) # decrypt the file

sys.exit(app.exec())