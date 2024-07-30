str = input("Enter a string: ")
# string to lower case
str = str.lower()
# str = "write a program to count the number of vowels and consonants present in an input string"
vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
consonant_count = 0
for i in str:
    if i in vowels:
        vowel_count += 1
    elif i.isalpha():
        consonant_count += 1

print("Vowels: ", vowel_count)
print("Consonants: ", consonant_count)
