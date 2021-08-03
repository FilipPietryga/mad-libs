#open filestream (like in C++)
file = open("sentence.txt")
#read a line from filestream, ignore endlines
line = file.read()
number = int(line[0])
sentence = line[1:]
#close filestream
file.close() 

print("Do you have any ideas on how to fill up these spaces?\n\n")
print(sentence)

for i in range(number):
    word = input("Suggest a word: ")
    index = sentence.find("_")
    print(index)
    last = index
    while True:
        last += 1
        if sentence[last] != "_":
            break
    print(last)
    sentence = sentence[0:index] + word + sentence[last:]
    print(sentence)