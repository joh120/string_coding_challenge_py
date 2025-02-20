

# Challenge 1 Print the number of word in a sentence

sentence = "I am a sentence"
senlen = len(sentence)
print(senlen)


# Challenge 2 Anagram

string1= "listen"
string2= "silent"
print (sorted(string1))
print (sorted(string2))

if sorted(string1) == sorted(string2):
    print("Anagram")
else:
    print("Not an anagram")



# Challenge 3 Palindrome

string = "madam"
if string == string[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")



#Challenge 4 Opens an existing text file, reads its content 

try:
    with open("text1.txt", "r") as file:
        content = file.read()
        print(content)
except:
    print("Something went wrong!")

print("-----------")

try:
    with open("text2.txt", "w") as newFile:
        copied= newFile.write(content)
except:
        print("Something went wrong!")

try:    
    with open("text2.txt", "r") as file:
        print(file.read())
        print("This text file content is copied from its predecessor text1")

except:
    print("Something went wrong!")


# Challenge 5 Loop through a text file 

try: 
    with open("text2.txt", "r") as file:
        lines = file.read()
        for line in lines:
            print(line)
except:
    print("Something went wrong!")


