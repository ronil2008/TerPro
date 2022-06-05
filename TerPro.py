#here is source of this programming language
import re
from colorama import Fore


def remove_str(lst):
    nlst = []
    for i in range(len(lst)):
        if type(lst[i]) == tuple:
            nlst2 = []
            for j in range(len(lst[i])):
                if lst[i][j] != '':
                    nlst2.append(lst[i][j])
            nlst.append(tuple(nlst2))
        else:
            if lst[i] != '':
                nlst.append(lst[i])
    return nlst

#21:you opening file that has TP format
code: str = open('filename.TP', 'r').read()
lex = re.findall(
    r'(:)?(\w*)\s?(=)\s?(.*)|(:)?(print)\s?(.*)|(:)?(\w*)\s?(=)\s?(input)\s?(.*)|(:)?(if)\s?(.*)|(:)?(else)|(:)?(\w*)\s?(\+=|-=|\*=|/=)\s?(.*)|(while)\s?(.*)',
    code)
lex = remove_str(lex)
variables = {}
dir = str(__file__).replace('main.py', 'main.TP')
i = 0
while i != len(lex):
    try:
        if lex[i][0] == 'while':
            while eval(str(lex[i][1]), variables.copy()):
                k = 0
                i += 1
                try:
                    while lex[i + k][0] == ':':
                        if lex[i + k][1] == 'print':
                            if lex[i + k][2][0] == '"' and lex[i + k][2][len(lex[i + k][2]) - 1] == '"':
                                print(lex[i + k][2][1:len(lex[i + k][2]) - 1])
                                k += 1
                            elif lex[i + k][2].isdigit():
                                print(int(lex[i + k][2]))
                                k += 1
                            elif lex[i + k][2].isdigit() or '.' in lex[i + k][1]:
                                print(float(lex[i + k][2]))
                                k += 1
                            else:
                                try:
                                    a = lex[i + k][2].split(',')
                                    for z in range(len(a)):
                                        a[z] = a[z].replace(' ', '')
                                    for z in range(len(a)):
                                        a[z] = eval(str(a[z]), variables.copy())
                                    for a in a:
                                        print(a)
                                        k += 1
                                except KeyError:
                                    print(f'Line {i}')
                                    print(
                                        Fore.RED + f'Error: Name {Fore.GREEN}"{lex[i + k][2]}{Fore.GREEN}"{Fore.RED} is not defined')
                                    k += 1
                        elif lex[i + k][2] == '=':
                            if 'input' not in lex[i + k][3][:5]:
                                variables[lex[i + k][1]] = lex[i + k][3]
                                variables[lex[i + k][1]] = eval(str(variables[lex[i + k][1]]), variables.copy())
                                k += 1
                            else:
                                j = 0
                                while True:
                                    if lex[i + k][3][j] == 'i':
                                        j += 1
                                        if lex[i + k][3][j] == 'n':
                                            j += 1
                                            if lex[i + k][3][j] == 'p':
                                                j += 1
                                                if lex[i + k][3][j] == 'u':
                                                    j += 1
                                                    if lex[i + k][3][j] == 't':
                                                        j += 1
                                                        if lex[i + k][3][j] == ' ':
                                                            j += 1
                                                            break
                                                        else:
                                                            break
                                                    else:
                                                        j += 1
                                                else:
                                                    j += 1
                                            else:
                                                j += 1
                                        else:
                                            j += 1
                                    else:
                                        j += 1
                                n = input(lex[i + k][3][6:])
                                if type(n) == int:
                                    variables[lex[i + k][1]] = int(n)
                                elif type(n) == float:
                                    variables[lex[i + k][1]] = float(n)
                                elif type(n) == str:
                                    variables[lex[i + k][1]] = str(n)
                                k += 1
                        elif lex[i + k][2] == '+=':
                            variables[lex[i + k][1]] += int(lex[i + k][3])
                            k += 1
                        elif lex[i + k][2] == '-=':
                            variables[lex[i + k][1]] -= int(lex[i + k][3])
                            k += 1
                        elif lex[i + k][2] == '*=':
                            variables[lex[i + k][1]] *= int(lex[i + k][3])
                            k += 1
                        elif lex[i + k][2] == '/=':
                            variables[lex[i + k][1]] /= int(lex[i + k][3])
                            k += 1
                except IndexError:
                    k = 0
                    continue
        elif lex[i][1] == '=':
            if 'input' not in lex[i][2]:
                variables[lex[i][0]] = lex[i][2]
                variables[lex[i][0]] = eval(str(variables[lex[i][0]]), variables.copy())
            else:
                j = 0
                while True:
                    if lex[i][2][j] == 'i':
                        j += 1
                        if lex[i][2][j] == 'n':
                            j += 1
                            if lex[i][2][j] == 'p':
                                j += 1
                                if lex[i][2][j] == 'u':
                                    j += 1
                                    if lex[i][2][j] == 't':
                                        j += 1
                                        if lex[i][2][j] == ' ':
                                            j += 1
                                            break
                                        else:
                                            break
                                    else:
                                        j += 1
                                else:
                                    j += 1
                            else:
                                j += 1
                        else:
                            j += 1
                    else:
                        j += 1
                n = input(lex[i][2][j:])
                if n.isdigit():
                    variables[lex[i][0]] = int(n)
                elif n.isdigit() or '.' in n:
                    variables[lex[i][0]] = float(n)
                else:
                    variables[lex[i][0]] = str(n)
        elif lex[i][0] == 'print':
            if lex[i][1][0] == '"' and lex[i][1][len(lex[i][1]) - 1] == '"':
                print(lex[i][1][1:len(lex[i][1]) - 1])
            elif lex[i][1].isdigit():
                print(int(lex[i][1]))
            elif lex[i][1].isdigit() or '.' in lex[i][1]:
                print(float(lex[i][1]))
            else:
                try:
                    a = lex[i][1].split(',')
                    for z in range(len(a)):
                        a[z] = a[z].replace(' ', '')
                    for z in range(len(a)):
                        a[z] = eval(str(a[z]), variables.copy())
                    for a in a:
                        print(a)
                except KeyError:
                    print(Fore.RED + f'Error: Name {Fore.GREEN}"{lex[i][1]}{Fore.GREEN}"{Fore.RED} is not defined')
        elif lex[i][0] == 'if':
            a = eval(str(lex[i][1]), variables.copy())
            if a:
                k = 0
                i += 1
                try:
                    while lex[i + k][0] == ':':
                        if lex[i + k][1] == 'print':
                            if lex[i + k][2][0] == '"' and lex[i + k][2][len(lex[i + k][2]) - 1] == '"':
                                print(lex[i + k][2][1:len(lex[i + k][2]) - 1])
                                k += 1
                            elif lex[i + k][2].isdigit():
                                print(int(lex[i + k][2]))
                                k += 1
                            elif lex[i + k][2].isdigit() or '.' in lex[i + k][1]:
                                print(float(lex[i + k][2]))
                                k += 1
                            else:
                                try:
                                    a = lex[i + k][2].split(',')
                                    for z in range(len(a)):
                                        a[z] = a[z].replace(' ', '')
                                    for z in range(len(a)):
                                        a[z] = eval(str(a[z]), variables.copy())
                                    for a in a:
                                        print(a)
                                        k += 1
                                except KeyError:
                                    print(f'Line {i}')
                                    print(
                                        Fore.RED + f'Error: Name {Fore.GREEN}"{lex[i + k][2]}{Fore.GREEN}"{Fore.RED} is not defined')
                                    k += 1
                        elif lex[i + k][2] == '=':
                            if 'input' not in lex[i + k][3][:5]:
                                variables[lex[i + k][1]] = lex[i + k][3]
                                variables[lex[i + k][1]] = eval(str(variables[lex[i + k][1]]), variables.copy())
                                k += 1
                            else:
                                j = 0
                                while True:
                                    if lex[i + k][3][j] == 'i':
                                        j += 1
                                        if lex[i + k][3][j] == 'n':
                                            j += 1
                                            if lex[i + k][3][j] == 'p':
                                                j += 1
                                                if lex[i + k][3][j] == 'u':
                                                    j += 1
                                                    if lex[i + k][3][j] == 't':
                                                        j += 1
                                                        if lex[i + k][3][j] == ' ':
                                                            j += 1
                                                            break
                                                        else:
                                                            break
                                                    else:
                                                        j += 1
                                                else:
                                                    j += 1
                                            else:
                                                j += 1
                                        else:
                                            j += 1
                                    else:
                                        j += 1
                                n = input(lex[i + k][3][6:])
                                if type(n) == int:
                                    variables[lex[i + k][1]] = int(n)
                                elif type(n) == float:
                                    variables[lex[i + k][1]] = float(n)
                                elif type(n) == str:
                                    variables[lex[i + k][1]] = str(n)
                                k += 1
                
                except IndexError:
                    continue
            else:
                i += 1
                while lex[i][0] == ':':
                    i += 1
                if lex[i][0] == 'else':
                    k = 0
                    i += 1
                    try:
                        while lex[i + k][0] == ':':
                            if lex[i + k][1] == 'print':
                                if lex[i + k][2][0] == '"' and lex[i + k][2][len(lex[i + k][2]) - 1] == '"':
                                    print(lex[i + k][2][1:len(lex[i + k][2]) - 1])
                                    k += 1
                                elif lex[i + k][2].isdigit():
                                    print(int(lex[i + k][2]))
                                    k += 1
                                elif lex[i + k][2].isdigit() or '.' in lex[i + k][1]:
                                    print(float(lex[i + k][2]))
                                    k += 1
                                elif lex[i][1] == '+=':
                                    variables[lex[i][0]] += int(lex[i][2])
                                elif lex[i][1] == '-=':
                                    variables[lex[i][0]] -= int(lex[i][2])
                                elif lex[i][1] == '*=':
                                    variables[lex[i][0]] *= int(lex[i][2])
                                elif lex[i][1] == '/=':
                                    variables[lex[i][0]] /= int(lex[i][2])
                                else:
                                    try:
                                        a = lex[i + k][2].split(',')
                                        for z in range(len(a)):
                                            a[z] = a[z].replace(' ', '')
                                        for z in range(len(a)):
                                            a[z] = eval(str(a[z]), variables.copy())
                                        for a in a:
                                            print(a)
                                            k += 1
                                    except KeyError:
                                        print(f'Line {i}')
                                        print(
                                            Fore.RED + f'Error: Name {Fore.GREEN}"{lex[i + k][2]}{Fore.GREEN}"{Fore.RED} is not defined')
                                        k += 1
                            elif lex[i + k][2] == '=':
                                if 'input' not in lex[i + k][0]:
                                    variables[lex[i + k][1]] = lex[i + k][3]
                                    variables[lex[i + k][1]] = eval(str(variables[lex[i + k][1]]), variables.copy())
                                    k += 1
                                else:
                                    k = 0
                                    while True:
                                        if lex[i][2][k] == 'i':
                                            k += 1
                                            if lex[i][2][k] == 'n':
                                                k += 1
                                                if lex[i][2][k] == 'p':
                                                    k += 1
                                                    if lex[i][2][k] == 'u':
                                                        k += 1
                                                        if lex[i][2][k] == 't':
                                                            k += 1
                                                            if lex[i][2][k] == ' ':
                                                                k += 1
                                                                break
                                                            else:
                                                                break
                                                        else:
                                                            k += 1
                                                    else:
                                                        k += 1
                                                else:
                                                    k += 1
                                            else:
                                                k += 1
                                        else:
                                            k += 1
                                    variables[lex[i][0]] = int(input(lex[i][2][k:]))
                    except IndexError:
                        continue
        if lex[i][1] == '+=':
            variables[lex[i][0]] += int(lex[i][2])
        elif lex[i][1] == '-=':
            variables[lex[i][0]] -= int(lex[i][2])
        elif lex[i][1] == '*=':
            variables[lex[i][0]] *= int(lex[i][2])
        elif lex[i][1] == '/=':
            variables[lex[i][0]] /= int(lex[i][2])
    except IndexError:
        pass
    i += 1
