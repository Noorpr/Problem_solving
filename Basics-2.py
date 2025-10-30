import random 

def list_from_two_lists(l1 : list, l2 : list):
    l3 = []
    l3.extend(l1[1::2])
    l3.extend(l2[0::2])
  
    return l3


def add_at_position(l : list, item, position : int):
    if position < 0 or position > len(l):
        raise IndexError("Index out of the range")
    
    return l[:position] + [item] + l[position:]


def slice_list(List : list, num_slices : int, reverse_order = False):
    length = len(List)

    chunk = length // num_slices
    start = 0
    end = chunk

    for i in range(chunk):
        
        indexes = slice(start, end)

        list_chunked = List[indexes]
        print(reversed(list_chunked) if reverse_order else list_chunked)
        start = end
        end += chunk


def check_unique(l : list):
    s = set(l)

    if len(s) == len(l):
        return True
    else:
        return False
    

def create_unique():
    LETTERS = ['a','e','i','o', 'l']

    random.shuffle(LETTERS)

    print(''.join(LETTERS))

def remove_every_third(l : list):
    if len(l) < 3:
        return 0
    third_number = l.pop(2)
    print("the third number is " + str(third_number))
    remove_every_third(l)



def zero_sum(l : list) -> None:
    
    if not all(isinstance(item, int) for item in l):
        raise TypeError("The list should contain only integer numbers")
    answer = list()
    for i in range(len(l) - 2):
        first_triple = l[i]
        for j in range(i + 1, len(l) - 1):
            second_triple = l[j]
            for k in range(j + 1, len(l)):
                third_triple = l[k]
                if (first_triple + second_triple + third_triple) == 0:
                    sorted_tuple = sorted((first_triple, second_triple, third_triple))
                    sorted_tuple = tuple(sorted_tuple)
                    answer.append(sorted_tuple)
                else:
                    continue
    if len(answer) == 0:
        print("there is no sum of zeros inside the list")
    else:
        print(set(answer))


def three_combination(l : list):

    if not all(isinstance(item , int) for item in l) or (len(l) > 3 or len(l) < 3):
        raise TypeError("Please ensure that the list is a three integer numbers to create the combination")
    
    random.shuffle(l)
    print(int("".join(map(str, l))))

