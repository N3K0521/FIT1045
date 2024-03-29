'''
DO NOT CHANGE THE NAME OF THIS FILE, or else the tester will not work. 
The first function requires that you replace the given strings with
your personal details. It is important that you enter your student number
and your student email correctly. If your number and email do not match we
will then check your name, so your name acts as a failsafe.
'''

# Student details
def details():
    student_number = '31552533' #write your student number as a string
    student_email = 'hwan0158' + '@student.monash.edu' #write your student email
    name = 'Huixin Wang' #write your name as it appears on Moodle
    return str(student_number), student_email, name

''' Simple Functions '''
# is_in()
def is_in(char, string):
    for i in range(len(string)):
        if char == string[i]:
            return True
    return False

# is_sorted()
def is_sorted(seq):
    for i in range(len(seq)-1):
        if seq[i] > seq[i+1]:
            return False
    return True

# abs()
def abs(x):
    if x >= 0:
        absx = x        # absx is refering to the absolute value of x
    elif x < 0:
        absx = 0 - x
    return absx

# all()
def all(lst):
    for element in lst:
        if not element:
            return False
    return True

# any()
def any(lst):
    for element in lst:
        if element:
            return True
    return False

# max()
def max(lst):
    ma = lst[0]
    for element in lst:
        if element > ma:
            ma = element
    return ma

# min()
def min(lst):
    mi = lst [0]
    for element in lst:
        if element < mi:
            mi = element
    return mi

# reversed()
def reversed(seq):
    res = []
    ri = len(seq) - 1
    for i in range(len(seq)):
        res.append(seq[ri - i])
    return res
'''
def rev_manual_pos_gen(lst):
    max_index = len(lst) - 1
    return [ lst[max_index - index] for index in range(len(lst)) ]

def rev_manual_neg_gen(lst):
    ## index is 0 to 9, but we need -1 to -10
    return [ lst[-index-1] for index in range(len(lst)) ]

def rev_manual_index_loop(lst):
    a = []
    reverse_index = len(lst) - 1
    for index in range(len(lst)):
        a.append(lst[reverse_index - index])
    return a

def rev_manual_loop(lst):
    a = []
    reverse_index = len(lst)
    for index, _ in enumerate(lst):
        reverse_index -= 1
        a.append(lst[reverse_index])
    return a
'''

# sum()
def sum(lst):
    res = 0
    for element in lst:
        res += element
    return res

'''Complex Functions'''
# bin()
def bin(x):
    start = "-0b"
    if x < 0:
        x = abs(x)
        start = "-0b"
    string = str(x%2)
    x //= 2
    while x > 0:
        string = str(x%2) + string
        x //= 2
    return start + string

# enumerate()
def enumerate(seq, start = 0):
    enum = []
    for i in range(len(seq)):
        enum.append((i+start, seq[i]))
    return enum

# filter()
def filter(function, seq):
    filt = []
    for item in seq:
        if function(item):
            filt.append(item)
    return

# map()
def map(function, seq):
    new_list = []
    for item in seq:
        new_list.append(function(item))
    return new_list

# lim_range()
def lim_range(start, stop, step = 1):
    my_range = []
    i = start
    if step > 0:
        while i < stop:
            my_range.append(i)
            i += step
    else:
        while i > stop:
            my_range.append(i)
            i += step
    return my_range

# round()
def round(number, ndigits = 0):
    # Remove all numbers but the last to be rounded using integer division
    # if ndigits = 0, number // 0.1, ndigits = 1, number // 0,01...
    # Check whether negative, and if so remove negative
    negative = number < 0
    number = abs(number)/(10**(-(ndigits + 1)))
    # Remove all extra digits
    number //= 1
    rounding = number % 10
    if rounding > 5:
        number = number // 10 + 1
    elif rounding < 5:
        number = number // 10
    else:
        number = number // 10
        if number % 10 %2 == 1:
            number += 1
    # Shift number to correct decimal places
    number /= 10 ** ndigits
    if negative:
        number *= -1
    return number

# set()
def set(aList):
    my_set = []
    for item in aList:
        if item not in my_set:
            my_set.append(item)
    return my_set
