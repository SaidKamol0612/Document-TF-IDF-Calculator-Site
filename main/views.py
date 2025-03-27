from django.shortcuts import render
from django.http import HttpRequest
from collections import Counter
import math

class Word:
    def __init__(self, word, tf, idf):
        self.word = word
        self.tf = tf
        self.idf = idf

def main_view(request : HttpRequest):
    return render(request, 'index.html')

def result_view(request: HttpRequest):
    if request.method == 'POST':
        uploaded_file = request.FILES['file'] # uploaded file
        content = uploaded_file.read().decode().splitlines() # Read file content
        
        words = [word for line in content for word in line.split()] # Split words
        total_words = len(words) # Total words
        word_counts = Counter(words) # Dictionary of words and counts
        
        total_docs = len(content) # Total documents
        
        result = []
        for word, count in word_counts.items():
            tf = count / total_words # Term frequency
            doc_count = sum(1 for line in content if word in line)
            idf = math.log((total_docs + 1) / (doc_count + 1)) + 1 # Inverse document frequency
            result.append(Word(word=word, tf=tf, idf=idf)) # Append to result list

            result = sorted(result, key=lambda x: x.idf, reverse=True) # Sort by idf in descending order
        return render(request, 'result.html', {'result': result})