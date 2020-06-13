import pandas as pd

df = pd.read_csv("1238.csv")


def getProblemName(df):
    problemName = df['problem'].unique()
    if problemName[0][0] == 'A':
        problemA = problemName[0]
        problemB = problemName[1]
    else:
        problemA = problemName[1]
        problemB = problemName[0]
    return problemA, problemB


problemNameA, problemNameB = getProblemName(df)

df_A = df.loc[df['problem'] == problemNameA]
df_B = df.loc[df['problem'] == problemNameB]

# TODO: lưu CSV
df_A.to_csv("1238-A.csv", index=False)
df_B.to_csv("1238-B.csv", index=False)
