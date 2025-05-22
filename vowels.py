string = input("Enter string: ")
vowels = ('a', 'e', 'i', 'o', 'u')
cnt = 0

for char in string.lower():  # Convert to lowercase to match vowels
    if char in vowels:
        cnt += 1
    else:
        pass

print("Number of vowels:", cnt)
