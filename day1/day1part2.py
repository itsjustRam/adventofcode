# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?

# Your puzzle answer was 54770.
def calibration(s):
    valid_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    valid_digits_mapping = {
        "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }
    f_local=""
    first=1000
    first_digit_index=1000
    
    l_local="" 
    last=0
    last_digit_index=0
    for i, char in enumerate(s):
        if char.isdigit():
            last_digit_index=i
            l_char=char
    r=s[::-1]
    for i, char in enumerate(r):
        if char.isdigit():
            first_digit_index=len(s)-i-1
            f_char=char
    for i in range(len(s)):
        for j in range(len(valid_digits)):
            if s[i:i + len(valid_digits[j])] == valid_digits[j]:
                if i<first:
                    first=i
                    f_local=valid_digits[j]
                if i>last:
                    last=i
                    l_local=valid_digits[j]
    if first<first_digit_index:
        first_digit_int=valid_digits_mapping.get(f_local)
    else:
        first_digit_int=int(f_char)
        
    if last>last_digit_index:
        last_digit_int=valid_digits_mapping.get(l_local)
    else:
        last_digit_int=int(l_char)
  

    sum=int(first_digit_int)*10+int(last_digit_int)
    return sum


sum=0
# Read strings from a text file
file_path = "input.txt"  # Replace with the path to your text file

try:
    with open(file_path, 'r') as file:
        # Read each line from the file
        input_strings = [line.strip() for line in file]

        # Find and print the first and last digit for each string
        for i, input_str in enumerate(input_strings, start=1):
            sum=sum+ calibration(input_str)
            print(sum)

except FileNotFoundError:
    print(f"File not found: {file_path}")
except IOError:
    print(f"Error reading the file: {file_path}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")