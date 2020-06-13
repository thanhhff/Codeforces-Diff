import sys
import numpy as np
import pandas as pd
import difflib
from difflib import unified_diff

# TODO: Read file
df = pd.read_csv("./data/data-clean/1238-A.csv")


# TODO: 1. nhóm các user cùng tên | phải có program OK và program WRONG
# Chương trình thoả mãn điều kiên có 2 problem trở lên và có cả OK lân WRONG để tạo thành 1 cặp dữ liệu
def checkProgram(df):
    groupByUserNameVerdict = df.groupby(['user_name', 'verdict']).size().reset_index(name='counts')
    groupByUserName = groupByUserNameVerdict.groupby(['user_name']).size().reset_index(name='count name').to_numpy()

    userName = []
    for name in groupByUserName:
        if name[1] > 1:
            userName.append(name[0])

    df_copy = df.copy()
    index = -1
    for row in df.iloc():
        index += 1
        if row[1] not in userName:
            df_copy.drop(df_copy.index[index], inplace=True)
            index -= 1

    return df_copy  # .to_numpy()
    # df_copy.to_csv("dfOK.csv", index=False)


df_copy = checkProgram(df)

# TODO: lấy ra các ok program | đồng thời xoá khỏi programCheckedNumpy

programCheckedNumpy = df_copy.to_numpy()
uniqueIdProgram = df_copy['user_name'].unique()

okProgram = []
wrongProgram = []
for program in programCheckedNumpy:
    if program[1] in uniqueIdProgram and program[-2] == 'OK':
        okProgram.append(program)
    else:
        wrongProgram.append(program)


def diffProgram(programWrongSource, programOkSource):
    for line in unified_diff(programWrongSource, programOkSource, fromfile=str(j[0]), tofile=str(i[0]), n=0,
                             lineterm=''):
        print(line)


for i in okProgram:
    programName = i[1]
    programOkSource = i[2]
    if '\r\n' in programOkSource:
        programOkSource = i[2].split('\r\n')
    else:
        programOkSource = i[2].split('\n')
    for j in wrongProgram:
        if programName == j[1]:
            programWrongSource = j[2]
            if '\r\n' in programWrongSource:
                programWrongSource = j[2].split('\r\n')
            else:
                programWrongSource = j[2].split('\n')
            diffProgram(programWrongSource, programOkSource)
