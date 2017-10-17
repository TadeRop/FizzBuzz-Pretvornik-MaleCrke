#-*- coding: utf-8 -*-

guess = int(raw_input("Izberi številko med 1 in 100:"))

for guess in range(1, guess+1):
    if guess % 3 == 0 and guess % 5 == 0:
        print ("fizzbuzz")
    elif guess % 3 == 0:
        print ("fizz")
    elif guess % 5 == 0:
        print ("buzz")
    else:
        print guess