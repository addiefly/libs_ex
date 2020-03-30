# -*- coding: UTF-8 -*-
import re
import xlrd

def string2code(string):
    if string == "N.PRBUsedOwn.DL.PLMN":
        code = "222222222222"
    else:
        code = "111111111111"
    return code

a = "(N.PRBUsedOwn.DL-N.PRBUsedOwn.DL.PLMN)>0"

def change_express(line):
    match_str = []
    results = re.findall('N.*?[ <>=()\-\+]', line)
    for result in results:
        match_str.append(result[:-1])
    print(match_str)
    match_str = sorted(match_str, reverse=True)
    print(match_str)

    # print(sorted(match_str, reverse=True))

    for match in match_str:
        m = match+'[^.]'
        rsts = re.findall(m, line)
        print("aaaaaaaaaa")
        print(rsts)
        if rsts is not None:
            for rst in rsts:
                line = line.replace(rst[:-1], string2code(match))
                print(line)
    return line

print(change_express(a))


print(re.findall('[A-z].*?[><=()\+\-]', a))