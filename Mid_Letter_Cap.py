# a python program which will be printing middle letter capital

x = input("Enter any phrase: ")
x=x.casefold()
c = int((len(x))/2)
x=x.split()
word = ' '

for i in x:
    word += i[0:c] + i[c].upper() + i[c+1:-1] + i[-1] + " "

print(word)
