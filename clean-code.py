import pandas as pd
import re

# TODO: Mở file
df = pd.read_csv("data/1238-B.csv")

# TODO: Sắp xếp theo tên
df = df.sort_values('user_name')

# df.to_csv("./data/data-clean/sort-name.csv", index=False)

# TODO: Xoá các dòng trống và xoá comment đầu dòng

def removeEmptyLines(string):
    # Xoá các dòng trống
    string = re.sub(re.compile("\n\s*\n"), "\n", string)
    return string


def removeComments(string):
    # Xoá các dòng comment có kiểu: (/*COMMENT */)
    string = re.sub(re.compile("/\*.*?\*/", re.DOTALL), "", string)

    # Xoá các dòng comment có kiểu: //
    string = re.sub(re.compile("//.*?\n"), "\n", string)
    return string


def cleanCode(string):
    string = removeComments(string)
    string = removeEmptyLines(string)
    return string


### TODO: START

# df = pd.read_csv("./data/data-clean/sort-name.csv")

for i in range(len(df['code'])):
    df['code'][i] = cleanCode(df['code'][i])

df.to_csv("./data/data-clean/1238-B.csv", index=False)

