from random import randint

PERMITTED_WALL_NOS = [3, 4, 6, 8, 10, 12, 20, 100]


def decipher_code(code: str = ''):
    if code == '':
        raise Exception('The code is an empty string')
    s = code.split('D')
    if len(s) != 2:
        raise Exception('The code contains the wrong number of "Ds"')
    if not s[0].isdigit():
        raise Exception('The number before D is not an integer')
    no_of_dice = int(s[0])
    op = '+'
    s1 = [s[1]]
    for c in ['+', '-']:
        if s[1].find(c) > 0:
            op = c
            s1 = s[1].split(c, maxsplit=1)
    if not s1[0].isdigit():
        raise Exception('The number after D is not an integer')
    no_of_walls = int(s1[0])
    if not no_of_walls in PERMITTED_WALL_NOS:
        raise Exception(f'The number of walls can be {PERMITTED_WALL_NOS}')
    if len(s1) > 1:
        if not s1[1].isdigit():
            raise Exception(f'The number after {op} is not an integer')
        modifier = int(s1[1])
    else:
        modifier = 0
    if op == '-':
        modifier *= -1
    return no_of_dice, no_of_walls, modifier


def throw_dice(no_of_dice: int = 1, no_of_walls: int = 6, modifier: int = 0):
    res = modifier
    throws = []
    for i in range(0,no_of_dice):
        n = randint(1, no_of_walls)
        throws.append(n)
        res += n
    return res, throws

for i in range(0,100):
    print(throw_dice(*decipher_code("15D20")))

# print(decipher_code('5D20'))
# print(decipher_code('5D13'))
# print(decipher_code('5D2D0'))
# print(decipher_code('5D12-8'))
# print(decipher_code('5D100-13'))
# print(decipher_code('5D100-1-3'))
# print(decipher_code())
