
import os
import socket
from collections import Counter

def word_count(fname):
        with open("./home/data/{}".format(fname)) as f:
                return Counter(f.read().split())

def required_functionalities():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    sourceFile = open('home/output/result.txt', 'w') # F
    print("System IP Address is:" + IPAddr, file = sourceFile) # E

    # Get the list of all files and directories
    dir_list = os.listdir('./home/data/')
    
    print("Text Files in current directory", file = sourceFile) 
    for file_name in dir_list:
        if file_name.endswith(".txt"):
            print(file_name, file = sourceFile)   # A
    total_word_count = 0
    for file_name in dir_list:
        if file_name.endswith(".txt"):
            print(file_name, file = sourceFile)
            # print("Number of words in the", file_name, " are : ",word_count(file_name))
            print("Top 3 words in", file_name, " are : ",word_count(file_name).most_common()[:3], file = sourceFile) # D


            number_of_words = 0
    
            # Opening our text file in read only mode using the open() function
            with open(r'./home/data/{}'.format(file_name),'r') as file:
            
                # Reading the content of the file using the read() function and storing them in a new variable
                data = file.read()
            
                # Splitting the data into separate lines using the split() function
                lines = data.split()
            
                # Adding the length of the lines in our number_of_words variable
                number_of_words += len(lines)
                total_word_count = total_word_count + number_of_words
            
            
            # Printing total number of words
            print("number of words for file {} are : {}".format(file_name, number_of_words), file = sourceFile) # B


    print("total word count is : ", total_word_count, file = sourceFile) # C

if __name__ == "__main__":
    required_functionalities()
    with open('home/output/result.txt', 'r+') as f:
        lines = f.readlines()
        for line in lines:
                print(line) # G
    
