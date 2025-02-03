#program 1:
def count_characters(input_string):
    vowels = 0
    consonants = 0
    spaces = 0
    others = 0

    for char in input_string:
        if char.lower() in 'aeiou':  
            vowels += 1
        elif char.isalpha():  
            consonants += 1
        elif char.isspace():  
            spaces += 1
        else:  
            others += 1

    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Spaces: {spaces}")
    print(f"Other characters: {others}")

#program 2:

def sum_of_digits(input_string):
    total = 0
    for char in input_string:
        if char.isdigit():  
            total += int(char)  
    print(f"Sum of digits: {total}")

# Example usage:
input_string = "Hello123World45"
count_characters(input_string)
sum_of_digits(input_string)

#program 3A:
def print_pattern_a():
    for i in range(1, 6):  
        for j in range(5 - i): 
            print(" ", end="")
        for k in range(1, i + 1): 
            print(k, end="")
        print() 

# Example usage:
print_pattern_a()

#program 3B:

def print_pattern_b():
    i = 1
    while i <= 7: 
        j = 1
        while j <= i:  
            if i == 2:  
                i += 1
                continue
            print(i, end="")
            j += 1
        print() 
        i += 1

# Example usage:
print_pattern_b()