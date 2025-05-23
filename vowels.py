def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Example usage
user_input = input("Enter a string: ")
vowel_count = count_vowels(user_input)
print(f"Number of vowels: {vowel_count}")

