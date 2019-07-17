# Working with Textual Data

greeting = "Hello"
print("\nEnter your name:")
name = input()

msg = f'{greeting}, {name}. \nWelcome..!'         # common message format for all users 
print("\n"+msg)

len = len(msg)    # find lengh of String
print("\nLength of String : "+str(len))

toLowerCase = name.lower()    # convert msg to lowercase letter
print("Convert Name to LowerCase : " + toLowerCase)

toUpperCase = name.upper()    # convert msg to uppercase letter
print("Convert Name to LowerCase : " + toUpperCase)

cap_each_word = 

print("Enter word to count how many time it occurs in above msg :")
print(" " + str(msg.count(input())))

print("Enter letter to count how many time it occurs in above msg :")
print(msg.count(input()))

