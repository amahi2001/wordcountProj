from django.shortcuts import render
from django.contrib import messages
import string
import re


# method for /'' path
def home(request):
    # pulling display information from broot.html
    return render(request, 'broot.html')

#function that sends information to broot.html
def submitCount(request):
    # print(request.method)
    if request.method == 'POST':
        textInput = request.POST.get('textInput', None)  # getting the text input
        # if the text is not empty
        if (textInput is not None) and (len(textInput) != 0):
            words = (textInput.split())
            # print(words)
            words.sort()
            #print('im in a get request')
            wordCount = len(words)
            wordDict = countWordsInput(words)

            return render(request, 'count.html', {'textInput': textInput, 'words': words, 'wordCount': wordCount, "wordDict": wordDict.items()})
        else:
            #error message
            messages.error(
                request, 'Please enter an input into the text field below')
            return render(request, 'broot.html')

# counts the words in text field input
def countWordsInput(words) -> dict:
    dict = {}
    for i in words:
        # if the word is already in the dictionary, increment counter
        if i in dict:
            dict[i] += 1
        # if the word is not in the dictionary, add it and set counter to 1
        else:
            # removing punctuation from end of word
            i = i.translate(str.maketrans('', '', string.punctuation))
            dict[i] = 1
            
    return dict

def about(request):
    dict = {}

    return render(request, 'about.html')
