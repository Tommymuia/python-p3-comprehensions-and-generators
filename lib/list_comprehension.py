#!/usr/bin/env python3

# 1️⃣ Return only even numbers from a list
def return_evens(num_list):
    return [x for x in num_list if x % 2 == 0]

# 2️⃣ Add an exclamation mark to each string in a list
def make_exclamation(sentence_list):
    return [s + "!" for s in sentence_list]
