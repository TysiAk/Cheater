#!/usr/bin/python3
import urllib.request
import re
from replaceMathChar import replaceMathToReadableCharacters as rM


#  ----------------------------------------------------------------
# |  YES, THIS SCRIPT IS FOR BRAINLY. YOU DON'T NEED BRAINLY PLUS! |
#  ----------------------------------------------------------------


#Get URL from USER
myUrl = str(input('Type URL link: '))

#Fake useragents
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'

#Request UTL using fake useragents
req = urllib.request.Request(myUrl, headers = headers)
resp = urllib.request.urlopen(req)

#Get Polish characters
respData = resp.read().decode('unicode-escape')

#Select only question and best answer from page source
textFromQuestion = re.findall (r'"@type":"Question"(.*?)","author":', str(respData), re.DOTALL)
textFromQuestion = str(re.findall (r'"name":"(.*?)","dateCreated"', str(textFromQuestion), re.DOTALL))
textFromAnswer = str(re.findall (r'suggestedAnswer(.*?)"@type":"Person"', str(respData), re.DOTALL))

#Check if there is awarded answer
if textFromAnswer == '[]':
    #if there is no awarded answer, search normal answer
    textFromAnswer = re.findall(r'acceptedAnswer":{"@type":"Answer"(.*?)@type":"Person', str(respData), re.DOTALL)
#END of IF

#Get only clear text from Answer
textFromAnswer = str(re.findall (r'"text":(.*?)","author"', str(textFromAnswer), re.DOTALL))

if textFromAnswer == '[]':
    # if there is no any answer, print information 'bout that
    textFromAnswer = str('There is no answer')
#END of IF

#Prepare text to write into txt file, normalize math symbols, add descriptions etc
textToWrite = 'QUESTION:\n\n' + rM(textFromQuestion) + u'\n\n\n\n ANSWER:\n\n' + rM(textFromAnswer)

#Print output into txt file
saveFile = open('result.txt', 'w')
saveFile.write(textToWrite)
saveFile.close()
