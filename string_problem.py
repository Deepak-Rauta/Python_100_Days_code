# 🔹 1. Reverse a String
text = "Hello world"
print(text[::-1])

# 🔹 2. Check for Palindrome
class Solution:
    def Is_Pallindrome(self, s):
        return str(s) == str(s)[::-1]
name = "madam"
obj = Solution()
print(obj.Is_Pallindrome(name))

# 🔹 3. Count Vowels and Consonants
def count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in s:
        if char.isalpha():  # Only consider alphabet
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    return vowel_count, consonant_count

text = "Data Science"
vowels, consonants = count_vowels_and_consonants(text)
print("Vowels:", vowels)
print("Consonants:", consonants)

# 🔹 4. Remove Duplicate Characters
class Solution:
    def Remove_Duplicates(self, s):
        seen = set()
        result = ''
        for char in s:
            if char not in seen:
                seen.add(char)
                result += char
        return result
text ="Programming"
obj = Solution()
print(obj.Remove_Duplicates(text))

# 🔹 5. Most Frequent Character
# Using Dictionary
def most_frequent_char(s):
    s = s.replace(" ", " ") # Remove spaces
    freq = {} # Create the empty dictionary

    for char in s:
        freq[char] = freq.get(char, 0) + 1  # count frequency

    # Get the character with maximum frequency
    max_char = max(freq, key=freq.get)  # get character with maximum count
    return max_char
text = "hello world"
print(most_frequent_char(text))