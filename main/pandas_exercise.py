# -*- coding: UTF-8 -*-
import os
import re
import pandas as pd

# file_name = "../docs/匹配规则.xlsx"
file_name = os.path.join('..', 'docs', '匹配规则.xlsx')
df = pd.read_excel(file_name)
Rules = (df['Rules'])


def string2code(string):
    if string == "N.PRBUsedOwn.DL.PLMN":
        code = "111111111"
    elif string == "N.PRBUsedOwn.DL":
        code = "222222222"
    elif string == "N.PRBUsedOther.DL.PLMN":
        code = "33333333333"
    elif string == "N.PRBUsedOther.DL":
        code = "44444444444444"
    elif string == "N.User.RRCConn.Max":
        code = "55555555555"
    elif string == "N.User.RRCConn.Min":
        code = "666666666666666"
    elif string == "N.Rcv.VoiceFB.Trig.PLMN":
        code = "7777777777777"
    elif string == "N.Rcv.VoiceFB.Trig":
        code = "88888888888888"
    else:
        code = "999999999999999"
    return code


def change_express(line):
    match_str = []
    # 找到N.开头并且结尾为<>=+-的字符串
    results = re.findall('N.*?[ <>=()\-\+]', line)
    for result in results:
        match_str.append(result[:-1])
    match_str = sorted(match_str, reverse=True)
    print(match_str)

    for match in match_str:
        rst = re.findall(match, line)
        if rst is not None:
            # 替换为找到的数值
            line = line.replace(match, string2code(match))
    # 如果不是>=或<=， 把=替换为 ==
    if re.findall('[^><]=', line):
        line = line.replace('=', '==')
    return line


print(u"开始话筒校验")
result = True
fail_details = {}
print(Rules)
for index in Rules.index:
    print(Rules[index])
    print(change_express(Rules[index]))
    print(eval(change_express(Rules[index])))
    if not eval(change_express(Rules[index])):
        result = False
        fail_details.update({Rules[index]: change_express(Rules[index])})

if not result:
    print(u"话筒校验出现异常，异常情况为{}".format(fail_details))
