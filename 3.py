str = input("Your word: ")

m = len(str)

for i in range(0,m):
     str[i] = 'a'
     print("str[0:i+1]")
     print("str[i+1:m]")

