import urllib2
from sys import argv
from Tkinter import *
import tkFileDialog

#This version takes words from a file input

def getDefinition(wordArg):
    """
    Returns the definition of the word wordArg.
    """

    #Get the page from an online dictionary
    req = urllib2.Request('http://dictionary.reference.com/browse/' + wordArg)
    response = urllib2.urlopen(req)
    the_page = response.read()

    //find the word in the page
    if(the_page.find('td3n2') != -1):
        definitionIndex = the_page.find('td3n2')
        definitionIndex = the_page.find('>', definitionIndex) + 1
        definitionIndexEnd = the_page.find('</td>', definitionIndex)
        definition = the_page[definitionIndex:definitionIndexEnd]
        definition = cleanup(definition)
        target.write(str(n) + '.' + wordArg + ': ' + the_page[definitionIndex:definitionIndexEnd] + '\n')
    else:
        target.write(str(n) + "." + wordArg + ": Error finding definition.")

def cleanup(defString):
    """
    Cleans up HTML formatting from the definition
    """
    while(defString.find('<') != -1):
        index1 = defString.find('<')
        index2 = defString.find('>', index1) + 1
        defString = defString[:index1] + defString[index2:]
    return defString


#script, inputfile, outputfile = argv
#make GUI
root = Tk()
w = Label(root, text = "Select the input file and then the output file")
w.pack()

print ("Select the input file")
inputfile = tkFileDialog.askopenfilename()
print ("Select the output file")
outputfile = tkFileDialog.askopenfilename()
txt = open(inputfile)
target = open(outputfile, 'w')
target.truncate()
n = 1

for word in txt:
    realWord = word[:len(word) - 1]
    getDefinition(realWord)
    n = n + 1

target.close()
