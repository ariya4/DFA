# Aria Code
# DFA code

Q = ['q0', 'q1', 'q2']  # ! States
E = ['0', '1']  # ! Alphabet
F = ['q0', 'q2']  # ! final States
s = [['q1', 'q2'], ['q1', 'q0'], ['q1', 'q0']]  # ! Pattern
route = []


def AAA(q, end):
    route.append(s[Q.index(q)][E.index(end)])
    return s[Q.index(q)][E.index(end)]


while 1 == 1:
    route = []
    start = Q[0]
    reza = (input("what's the string bro: "))
    for i in reza:
        star = AAA(start, i)
    if route[-1] in F:
        print('Accepted')
    else:
        print('Not Accepted')
#kaka
