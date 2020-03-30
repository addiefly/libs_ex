# -*- coding: UTF-8 -*-
import os
import re
import pandas as pd

# file_name = "../docs/匹配规则.xlsx"
file_name = os.path.join('..', 'docs', '匹配规则.xlsx')
sheet_name = 'l3traffic'
df = pd.read_excel(file_name, sheet_name)
Rules = (df['Rules'])


# 实际业务实际中，会找到对应指标的数据，目前先随便做个用于测试
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


def handle_express(line):
    """
    对字符串公式进行处理，获取数值并替换，得到计算结果
    :param line:
    :return:
    """
    match_str = []
    # 找到N.开头并且结尾为<>=+-的字符串
    results = re.findall('[A-z].*?[ <>=()\-\+]', line)
    for result in results:
        match_str.append(result[:-1])
    # 做一个倒序排列，防止后面替换的时候因为有重复，短的把长的部分也覆盖了，所以把长的放前面先进行替换处理
    match_str = sorted(match_str, reverse=True)

    for match in match_str:
        rst = re.findall(match, line)
        if rst is not None:
            # 替换为找到的数值
            line = line.replace(match, string2code(match))
    # 如果不是>=或<=， 把=替换为 ==
    if re.findall('[^><]=', line):
        line = line.replace('=', '==')
    return eval(line)


print(u"开始话统校验")
result = True
fail_details = {}
print(Rules)
for index in Rules.index:
    # print(Rules[index])
    # print(handle_express(Rules[index]))
    if not handle_express(Rules[index]):
        result = False
        fail_details.update({Rules[index]: handle_express(Rules[index])})

if not result:
    print(u"话统校验出现异常，异常情况为{}".format(fail_details))
