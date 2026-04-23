#converts a number into a banodos number.
#banodos is the process of taking a number, can converting it into binary, then to save space subtracing the zeros after the last one.
#banodos can be writen to somewhere, displayed how many digits it would have been.
#when calling banodos, you give it the number you want to apply to it, what you want out of

from collections import deque
from json import dumps

BinaryList = deque([])

#data = [{
#    f'{{"base number :{number}"}}'
#    f'{{"recursion: {recurse}"}}'
#    f'{{"full list: {BinaryList}"}}'
#}]

#what the user wants to do, either get a full binary or get a length.
def action():
    while True:
        WhatToDo = int(input("do you wish to get the full binary(1) or get the length(2)"))
        if WhatToDo == 1:
            number = int(input("what number do you want to apply to BanoDos?"))
            recurse = int(input("how many times do you want to run BanoDos,(exponent)")) + 1
            Base10ToBinary(number, recurse)
        elif WhatToDo == 2:
            number = int(input("what number do you want to apply to BanoDos?"))
            recurse = int(input("how many times do you want to run BanoDos,(exponent)"))
            Base10ToBinaryNumCount(number, recurse)
        else:
            print("enter a integer for your selection")

#takes a integer in base 10 format and converts to binary
def Base10ToBinary(number, recurse):
    while recurse >= 1:
        while number > 1:
            number = number // 2
            remain = number % 2
            BinaryList.appendleft(remain)
        recurse -= 1
    while True:
        action2 = str(input("do you wish to (s)ave the numbers or (d)isplay them")).lower()
        if action2 == "s":
            with open("~/main.json", "w") as f:
                json.dump(data, f)
            break
        elif action2 == "d":
            print(BinaryList)
            break
        else:
            print("please say if you wish to save the numbers or display them with 's' or 'd'")

#add in taking the number or reading from the json file.
def Base10ToBinaryNumCount(number, recurse):
    while recurse >= 1:
        while number > 1:
            number = number // 2
            remain = number % 2
            BinaryLength += 1
        recurse -= 1
    
    print(BinaryLength)

action()
#add in decimal acceptance.
#could be a blockchain, as they do build on each other
#make a few functions by converting the binary into hexadecimal or octal numbers for easier storage for hexadecimal or computing for octal.
