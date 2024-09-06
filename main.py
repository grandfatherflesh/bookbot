#Change the book vars value to the book path.
book = "books/frankenstein.txt"
with open(book) as f:
    #Creates a variable for read book.
    file_contents = f.read()
#Count variable value of which will append with each word.
count = 0
#Splits text into words.
words = file_contents.split()
#Goes over all the words and appends the count variable by 1 for each.
for words in words:
    count +=1
#A variable where all words are lowercased.
low_words = file_contents.lower()
#An empty dictionary that will be populated with character:count pairs.
char_dic = {}
#Goes over all characters in words.
for char in low_words:
    #Checks if the character is a letter.
    if char.isalpha():
        #If word is already in the dictionary, it appends its value by 1.
        if char in char_dic:
            char_dic[char] += 1
        #If word is not in the dictionary, it adds it as a key and sets its value to 1.
        if char not in char_dic:
            char_dic[char] = 1

print(f"--- Begin report of {book} ---")
print(f"{count} words found in the document")
#Goes over a character in alphabetically sorted char_dic dictionary.
for char in sorted(char_dic.keys()):
    #Prints a count for each character
    print(f"The character '{char}' was found {char_dic[char]} times")
print("--- End report ---")