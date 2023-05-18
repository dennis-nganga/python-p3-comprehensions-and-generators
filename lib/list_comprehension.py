#!/usr/bin/env python3

def return_evens(num_list):
    even_list = []
    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

   
def make_exclamation(sentence_list):
    if len(sentence_list) == 0:
        return []
    
    exclamation_list = []
    for sentence in sentence_list:
        if sentence[-1] in ['.', '!', '?']:
            exclamation_sentence = sentence[:-1] + "!"
        else:
            exclamation_sentence = sentence + "!"
        exclamation_list.append(exclamation_sentence)

    return exclamation_list
