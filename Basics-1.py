import string
import time

def current_plus_back(a, b, arr : list = None):
    if arr is None:
        arr = []
        if a > b:
            print("the number before ", a , " is ", b , " and there sum is ", (a + b))
        else:
            raise ValueError("Please the first number must be greater than the second no the way around")
        return 0
    else:
        pass


def print_even_chars(text : str):
    for i in range(0, len(text)):
        if i % 2 == 1:
            print(text[i])

def remove_first_n_chars(text : str, n : int):
    if n < 0:
        raise ValueError("the number must be positive or zero")
    else:
        return text[n:]
    
def check_first_and_last(numbers : list):
    if len(numbers) < 2:
        raise ValueError("Please ensure that the list has more or eqaul than 2 numbesr")
    else:
        return numbers[0] == numbers[-1]


def display_numbers_divisible_by(numbers : list, divisible : int):
    answer = []
    for num in numbers:
        if num % divisible == 0:
            answer.append(num)

    return answer

def find_substring(main_text : str, text : str):
    if main_text.find(text) == 1:
        return "there is no such text in the main text"
    else:
        counter = 0
        main_text = main_text.split(" ")
        for txt in main_text:
            if txt == text:
                counter += 1
        return text + " has appeard in the main text " + str(counter) + " times" 
    
def print_pattern(n : int):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()

def check_palindrome(num : int):
    str_num = str(num)
    if str_num == str_num[::-1]:
        return "the number " + str(num) + " is a palindrome number"
    else:
        return "the number " + str(num) + " is not a palindrome number"
    
def merge_two_odd_lists(list1 : list, list2 : list):
    list_temp = []
    for num in list1:
        if num % 2 == 1:
            list_temp.append(num)
    
    for num in list2:
        if num % 2 == 1:
            list_temp.append(num)
    
    return list_temp

def reverse_order_and_return_indv(num : int):
    length = len(str(num))
    dividor = 10

    for i in range(length):
        print((num // dividor ** i) % 10, end=' ')
    

def income_tax(income : int):
    taxes = [0, 0.1, 0.2]
    if income < 20000:
        return 0
    else:
        tax = 0
        for i in range(len(taxes)):
            if i <= 1:
                income = income - 10000
                tax += 10000 * taxes[i]
            else:
                tax += income * taxes[i]
        return tax
    

def multiplication_number_table(start : int, end : int):
    if start >= end or start <= 0:
        raise ValueError("Please enter a valid range from start to end respectivaly.")
    multiplies = list(range(1, 11))
    for i in range(start, end + 1):
        print(i, end="\t")
        for j in range(len(multiplies)):
            print(i * multiplies[j], end=" ")
        print()


def downward_pyramid(n : int):
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

def exponent(base : int, exp : int):
    result = 1
    for i in range(exp):
        result *= base
    return result

def fibonacci(limit = 15):
    NUM1 , NUM2 = 0, 1

    print("fibonacci series:")
    
    for i in range(limit):
        print(NUM1, end=" ")
        res = NUM1 + NUM2
        NUM1 = NUM2
        NUM2 = res
        
def check_leap_year(year : int):
    if year % 4 == 0:
        if year % 100 and year % 400 != 0:
            return True
        else:
            return False
    else:
        return False
    
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_range(start : int, end : int):
    print("the prime numbers from " + str(start) + " to " + str(end) + " is:", end=" ")
    for i in range(start, end + 1):
        if is_prime(i):
            print(i, end=" ")
        else:
            continue

def reversed_range(start : int, end : int):
    number_of_repeat = end
    for i in range(start, end + 1):
        for j in range(number_of_repeat):
            print(i, end= " ")
        number_of_repeat -= 1
        print()
    

def check_numbers_inside_string():
    string = str(input("Enter a string here: "))
    for letter in string:
        try:
            if int(letter) <= 90:
                print("the string has at least one digit character")
                return
        except ValueError:
            continue
    print("the string is just fine")

def capitalize_first_words(text : str):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)


def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    
    print("Time's up!")

countdown_timer(10)


