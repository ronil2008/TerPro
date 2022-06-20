---
id: hth2x
name: Adding a New programming language IDE
file_version: 1.0.2
app_version: 0.8.9-1
file_blobs:
  TerPro.py: 21b3679719df7e182a5a9b4f48b4b02ed9355f4e
---

Source of programming language
<!-- NOTE-swimm-snippet: the lines below link your snippet to Swimm -->
### 📄 TerPro.py
<!-- collapsed -->

```python
🟩 1      #here is source of this programming language
🟩 2      import re
🟩 3      from colorama import Fore
🟩 4      
🟩 5      
🟩 6      def remove_str(lst):
🟩 7          nlst = []
🟩 8          for i in range(len(lst)):
🟩 9              if type(lst[i]) == tuple:
🟩 10                 nlst2 = []
🟩 11                 for j in range(len(lst[i])):
🟩 12                     if lst[i][j] != '':
🟩 13                         nlst2.append(lst[i][j])
🟩 14                 nlst.append(tuple(nlst2))
🟩 15             else:
🟩 16                 if lst[i] != '':
🟩 17                     nlst.append(lst[i])
🟩 18         return nlst
🟩 19     
🟩 20     #21:you opening file that has TP format
🟩 21     code: str = open('filename.TP', 'r').read()
🟩 22     lex = re.findall(
🟩 23         r'(:)?(\w*)\s?(=)\s?(.*)|(:)?(print)\s?(.*)|(:)?(\w*)\s?(=)\s?(input)\s?(.*)|(:)?(if)\s?(.*)|(:)?(else)|(:)?(\w*)\s?(\+=|-=|\*=|/=)\s?(.*)|(while)\s?(.*)',
🟩 24         code)
🟩 25     lex = remove_str(lex)
🟩 26     variables = {}
🟩 27     dir = str(__file__).replace('main.py', 'main.TP')
🟩 28     i = 0
🟩 29     while i != len(lex):
🟩 30         try:
🟩 31             if lex[i][0] == 'while':
🟩 32                 while eval(str(lex[i][1]), variables.copy()):
🟩 33                     k = 0
🟩 34                     i += 1
🟩 35                     try:
🟩 36                         while lex[i + k][0] == ':':
🟩 37                             if lex[i + k][1] == 'print':
🟩 38                                 if lex[i + k][2][0] == '"' and lex[i + k][2][len(lex[i + k][2]) - 1] == '"':
🟩 39                                     print(lex[i + k][2][1:len(lex[i + k][2]) - 1])
🟩 40                                     k += 1
🟩 41                                 elif lex[i + k][2].isdigit():
🟩 42                                     print(int(lex[i + k][2]))
🟩 43                                     k += 1
🟩 44                                 elif lex[i + k][2].isdigit() or '.' in lex[i + k][1]:
🟩 45                                     print(float(lex[i + k][2]))
🟩 46                                     k += 1
🟩 47                                 else:
🟩 48                                     try:
🟩 49                                         a = lex[i + k][2].split(',')
🟩 50                                         for z in range(len(a)):
🟩 51                                             a[z] = a[z].replace(' ', '')
🟩 52                                         for z in range(len(a)):
🟩 53                                             a[z] = eval(str(a[z]), variables.copy())
🟩 54                                         for a in a:
🟩 55                                             print(a)
🟩 56                                             k += 1
🟩 57                                     except KeyError:
🟩 58                                         print(f'Line {i}')
🟩 59                                         print(
🟩 60                                             Fore.RED + f'Error: Name {Fore.GREEN}"{lex[i + k][2]}{Fore.GREEN}"{Fore.RED} is not defined')
🟩 61                                         k += 1
🟩 62                             elif lex[i + k][2] == '=':
🟩 63                                 if 'input' not in lex[i + k][3][:5]:
🟩 64                                     variables[lex[i + k][1]] = lex[i + k][3]
🟩 65                                     variables[lex[i + k][1]] = eval(str(variables[lex[i + k][1]]), variables.copy())
🟩 66                                     k += 1
🟩 67                                 else:
🟩 68                                     j = 0
🟩 69                                     while True:
🟩 70                                         if lex[i + k][3][j] == 'i':
🟩 71                                             j += 1
🟩 72                                             if lex[i + k][3][j] == 'n':
🟩 73                                                 j += 1
🟩 74                                                 if lex[i + k][3][j] == 'p':
🟩 75                                                     j += 1
🟩 76                                                     if lex[i + k][3][j] == 'u':
🟩 77                                                         j += 1
🟩 78                                                         if lex[i + k][3][j] == 't':
🟩 79                                                             j += 1
🟩 80                                                             if lex[i + k][3][j] == ' ':
🟩 81                                                                 j += 1
🟩 82                                                                 break
🟩 83                                                             else:
🟩 84                                                                 break
🟩 85                                                         else:
🟩 86                                                             j += 1
🟩 87                                                     else:
🟩 88                                                         j += 1
🟩 89                                                 else:
🟩 90                                                     j += 1
🟩 91                                             else:
🟩 92                                                 j += 1
🟩 93                                         else:
🟩 94                                             j += 1
🟩 95                                     n = input(lex[i + k][3][6:])
🟩 96                                     if type(n) == int:
🟩 97                                         variables[lex[i + k][1]] = int(n)
🟩 98                                     elif type(n) == float:
🟩 99                                         variables[lex[i + k][1]] = float(n)
🟩 100                                    elif type(n) == str:
🟩 101                                        variables[lex[i + k][1]] = str(n)
🟩 102                                    k += 1
🟩 103                            elif lex[i + k][2] == '+=':
🟩 104                                variables[lex[i + k][1]] += int(lex[i + k][3])
🟩 105                                k += 1
🟩 106                            elif lex[i + k][2] == '-=':
🟩 107                                variables[lex[i + k][1]] -= int(lex[i + k][3])
🟩 108                                k += 1
🟩 109                            elif lex[i + k][2] == '*=':
🟩 110                                variables[lex[i + k][1]] *= int(lex[i + k][3])
🟩 111                                k += 1
🟩 112                            elif lex[i + k][2] == '/=':
🟩 113                                variables[lex[i + k][1]] /= int(lex[i + k][3])
🟩 114                                k += 1
🟩 115                    except IndexError:
🟩 116                        k = 0
🟩 117                        continue
🟩 118            elif lex[i][1] == '=':
🟩 119                if 'input' not in lex[i][2]:
🟩 120                    variables[lex[i][0]] = lex[i][2]
🟩 121                    variables[lex[i][0]] = eval(str(variables[lex[i][0]]), variables.copy())
🟩 122                else:
🟩 123                    j = 0
🟩 124                    while True:
🟩 125                        if lex[i][2][j] == 'i':
🟩 126                            j += 1
🟩 127                            if lex[i][2][j] == 'n':
🟩 128                                j += 1
🟩 129                                if lex[i][2][j] == 'p':
🟩 130                                    j += 1
🟩 131                                    if lex[i][2][j] == 'u':
🟩 132                                        j += 1
🟩 133                                        if lex[i][2][j] == 't':
🟩 134                                            j += 1
🟩 135                                            if lex[i][2][j] == ' ':
🟩 136                                                j += 1
🟩 137                                                break
🟩 138                                            else:
🟩 139                                                break
🟩 140                                        else:
🟩 141                                            j += 1
🟩 142                                    else:
🟩 143                                        j += 1
🟩 144                                else:
🟩 145                                    j += 1
🟩 146                            else:
🟩 147                                j += 1
🟩 148                        else:
🟩 149                            j += 1
🟩 150                    n = input(lex[i][2][j:])
🟩 151                    if n.isdigit():
🟩 152                        variables[lex[i][0]] = int(n)
🟩 153                    elif n.isdigit() or '.' in n:
🟩 154                        variables[lex[i][0]] = float(n)
🟩 155                    else:
🟩 156                        variables[lex[i][0]] = str(n)
🟩 157            elif lex[i][0] == 'print':
🟩 158                if lex[i][1][0] == '"' and lex[i][1][len(lex[i][1]) - 1] == '"':
🟩 159                    print(lex[i][1][1:len(lex[i][1]) - 1])
🟩 160                elif lex[i][1].isdigit():
🟩 161                    print(int(lex[i][1]))
🟩 162                elif lex[i][1].isdigit() or '.' in lex[i][1]:
🟩 163                    print(float(lex[i][1]))
🟩 164                else:
🟩 165                    try:
🟩 166                        a = lex[i][1].split(',')
🟩 167                        for z in range(len(a)):
🟩 168                            a[z] = a[z].replace(' ', '')
🟩 169                        for z in range(len(a)):
🟩 170                            a[z] = eval(str(a[z]), variables.copy())
🟩 171                        for a in a:
🟩 172                            print(a)
🟩 173                    except KeyError:
🟩 174                        print(Fore.RED + f'Error: Name {Fore.GREEN}"{lex[i][1]}{Fore.GREEN}"{Fore.RED} is not defined')
🟩 175            elif lex[i][0] == 'if':
🟩 176                a = eval(str(lex[i][1]), variables.copy())
🟩 177                if a:
🟩 178                    k = 0
🟩 179                    i += 1
🟩 180                    try:
🟩 181                        while lex[i + k][0] == ':':
🟩 182                            if lex[i + k][1] == 'print':
🟩 183                                if lex[i + k][2][0] == '"' and lex[i + k][2][len(lex[i + k][2]) - 1] == '"':
🟩 184                                    print(lex[i + k][2][1:len(lex[i + k][2]) - 1])
🟩 185                                    k += 1
🟩 186                                elif lex[i + k][2].isdigit():
🟩 187                                    print(int(lex[i + k][2]))
🟩 188                                    k += 1
🟩 189                                elif lex[i + k][2].isdigit() or '.' in lex[i + k][1]:
🟩 190                                    print(float(lex[i + k][2]))
🟩 191                                    k += 1
🟩 192                                else:
🟩 193                                    try:
🟩 194                                        a = lex[i + k][2].split(',')
🟩 195                                        for z in range(len(a)):
🟩 196                                            a[z] = a[z].replace(' ', '')
🟩 197                                        for z in range(len(a)):
🟩 198                                            a[z] = eval(str(a[z]), variables.copy())
🟩 199                                        for a in a:
🟩 200                                            print(a)
🟩 201                                            k += 1
🟩 202                                    except KeyError:
🟩 203                                        print(f'Line {i}')
🟩 204                                        print(
🟩 205                                            Fore.RED + f'Error: Name {Fore.GREEN}"{lex[i + k][2]}{Fore.GREEN}"{Fore.RED} is not defined')
🟩 206                                        k += 1
🟩 207                            elif lex[i + k][2] == '=':
🟩 208                                if 'input' not in lex[i + k][3][:5]:
🟩 209                                    variables[lex[i + k][1]] = lex[i + k][3]
🟩 210                                    variables[lex[i + k][1]] = eval(str(variables[lex[i + k][1]]), variables.copy())
🟩 211                                    k += 1
🟩 212                                else:
🟩 213                                    j = 0
🟩 214                                    while True:
🟩 215                                        if lex[i + k][3][j] == 'i':
🟩 216                                            j += 1
🟩 217                                            if lex[i + k][3][j] == 'n':
🟩 218                                                j += 1
🟩 219                                                if lex[i + k][3][j] == 'p':
🟩 220                                                    j += 1
🟩 221                                                    if lex[i + k][3][j] == 'u':
🟩 222                                                        j += 1
🟩 223                                                        if lex[i + k][3][j] == 't':
🟩 224                                                            j += 1
🟩 225                                                            if lex[i + k][3][j] == ' ':
🟩 226                                                                j += 1
🟩 227                                                                break
🟩 228                                                            else:
🟩 229                                                                break
🟩 230                                                        else:
🟩 231                                                            j += 1
🟩 232                                                    else:
🟩 233                                                        j += 1
🟩 234                                                else:
🟩 235                                                    j += 1
🟩 236                                            else:
🟩 237                                                j += 1
🟩 238                                        else:
🟩 239                                            j += 1
🟩 240                                    n = input(lex[i + k][3][6:])
🟩 241                                    if type(n) == int:
🟩 242                                        variables[lex[i + k][1]] = int(n)
🟩 243                                    elif type(n) == float:
🟩 244                                        variables[lex[i + k][1]] = float(n)
🟩 245                                    elif type(n) == str:
🟩 246                                        variables[lex[i + k][1]] = str(n)
🟩 247                                    k += 1
🟩 248                    
🟩 249                    except IndexError:
🟩 250                        continue
🟩 251                else:
🟩 252                    i += 1
🟩 253                    while lex[i][0] == ':':
🟩 254                        i += 1
🟩 255                    if lex[i][0] == 'else':
🟩 256                        k = 0
🟩 257                        i += 1
🟩 258                        try:
🟩 259                            while lex[i + k][0] == ':':
🟩 260                                if lex[i + k][1] == 'print':
🟩 261                                    if lex[i + k][2][0] == '"' and lex[i + k][2][len(lex[i + k][2]) - 1] == '"':
🟩 262                                        print(lex[i + k][2][1:len(lex[i + k][2]) - 1])
🟩 263                                        k += 1
🟩 264                                    elif lex[i + k][2].isdigit():
🟩 265                                        print(int(lex[i + k][2]))
🟩 266                                        k += 1
🟩 267                                    elif lex[i + k][2].isdigit() or '.' in lex[i + k][1]:
🟩 268                                        print(float(lex[i + k][2]))
🟩 269                                        k += 1
🟩 270                                    elif lex[i][1] == '+=':
🟩 271                                        variables[lex[i][0]] += int(lex[i][2])
🟩 272                                    elif lex[i][1] == '-=':
🟩 273                                        variables[lex[i][0]] -= int(lex[i][2])
🟩 274                                    elif lex[i][1] == '*=':
🟩 275                                        variables[lex[i][0]] *= int(lex[i][2])
🟩 276                                    elif lex[i][1] == '/=':
🟩 277                                        variables[lex[i][0]] /= int(lex[i][2])
🟩 278                                    else:
🟩 279                                        try:
🟩 280                                            a = lex[i + k][2].split(',')
🟩 281                                            for z in range(len(a)):
🟩 282                                                a[z] = a[z].replace(' ', '')
🟩 283                                            for z in range(len(a)):
🟩 284                                                a[z] = eval(str(a[z]), variables.copy())
🟩 285                                            for a in a:
🟩 286                                                print(a)
🟩 287                                                k += 1
🟩 288                                        except KeyError:
🟩 289                                            print(f'Line {i}')
🟩 290                                            print(
🟩 291                                                Fore.RED + f'Error: Name {Fore.GREEN}"{lex[i + k][2]}{Fore.GREEN}"{Fore.RED} is not defined')
🟩 292                                            k += 1
🟩 293                                elif lex[i + k][2] == '=':
🟩 294                                    if 'input' not in lex[i + k][0]:
🟩 295                                        variables[lex[i + k][1]] = lex[i + k][3]
🟩 296                                        variables[lex[i + k][1]] = eval(str(variables[lex[i + k][1]]), variables.copy())
🟩 297                                        k += 1
🟩 298                                    else:
🟩 299                                        k = 0
🟩 300                                        while True:
🟩 301                                            if lex[i][2][k] == 'i':
🟩 302                                                k += 1
🟩 303                                                if lex[i][2][k] == 'n':
🟩 304                                                    k += 1
🟩 305                                                    if lex[i][2][k] == 'p':
🟩 306                                                        k += 1
🟩 307                                                        if lex[i][2][k] == 'u':
🟩 308                                                            k += 1
🟩 309                                                            if lex[i][2][k] == 't':
🟩 310                                                                k += 1
🟩 311                                                                if lex[i][2][k] == ' ':
🟩 312                                                                    k += 1
🟩 313                                                                    break
🟩 314                                                                else:
🟩 315                                                                    break
🟩 316                                                            else:
🟩 317                                                                k += 1
🟩 318                                                        else:
🟩 319                                                            k += 1
🟩 320                                                    else:
🟩 321                                                        k += 1
🟩 322                                                else:
🟩 323                                                    k += 1
🟩 324                                            else:
🟩 325                                                k += 1
🟩 326                                        variables[lex[i][0]] = int(input(lex[i][2][k:]))
🟩 327                        except IndexError:
🟩 328                            continue
🟩 329            if lex[i][1] == '+=':
🟩 330                variables[lex[i][0]] += int(lex[i][2])
🟩 331            elif lex[i][1] == '-=':
🟩 332                variables[lex[i][0]] -= int(lex[i][2])
🟩 333            elif lex[i][1] == '*=':
🟩 334                variables[lex[i][0]] *= int(lex[i][2])
🟩 335            elif lex[i][1] == '/=':
🟩 336                variables[lex[i][0]] /= int(lex[i][2])
🟩 337        except IndexError:
🟩 338            pass
🟩 339        i += 1
⬜ 340    
```

<br/>

This file was generated by Swimm. [Click here to view it in the app](https://app.swimm.io/repos/Z2l0aHViJTNBJTNBVGVyUHJvJTNBJTNBcm9uaWwyMDA4/docs/hth2x).