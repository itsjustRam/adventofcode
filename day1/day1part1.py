# --- Day 1: Trebuchet?! ---
# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

#Answer:54630

def calibration(s):
    first_digit = None
    last_digit = None
    sum=0
    # Iterate through each character in the string
    for char in s:
        if char.isdigit():
            # If the character is a digit, update the last_digit
            last_digit = char

            # If first_digit is not set, set it
            if first_digit is None:
                first_digit = char

    sum=int(first_digit)*10+int(last_digit)
    return sum


sum=0
# Read strings from a text file
file_path = ".\day1\input.txt"  # Replace with the path to your text file

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

