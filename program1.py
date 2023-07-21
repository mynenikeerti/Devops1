given_num = 12321
    duplicate_num = given_num
    reverse_number = 0
    while (given_num > 0):
remainder = given_num % 10
reverse_number = (reverse_number * 10) + remainder given_num = given_num // 10
if(duplicate_num == reverse_number):
print("The given number", duplicate_num, "is palindrome")
else:
print("The given number", duplicate_num, "is not palindrome")
Output: The given number 12321 is palindrome
