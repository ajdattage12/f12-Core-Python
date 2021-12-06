digit_map = {
    'zero' : '0',
    'one' :'1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' :'8',
    'nine' : '9'
}

def convert(s):
    try:
        number = ''
        for token in s :
            number += digit_map[token]
        x = int(number)
        print(f"Conversion succeeded! x = {x}")
    except KeyError:
        print("Conversion failed!")
        x = -1
    except TypeError:
        print("Conversion failed!")
        x = -1
    return x

print(convert("one three three seven".split()))
print(convert("three four".split()))
print(convert("eleventeen".split()))


from math import log 

def string_log(s):
    v = convert(s)
    return log(v)

print(string_log("one two".split()))

