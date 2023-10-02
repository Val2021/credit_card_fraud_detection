# !/usr/bin/python3
# -*- coding: utf-8 -*-\
"""
Ref and Copy with Pandas
	https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
"""
import pandas as pd
from tabulate import tabulate

MARK = '+++++++++++'


def example1():
    data = {'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50]}
    df = pd.DataFrame(data)

    df_slice = df

    df_slice['A'] = df_slice['A'] * 2

    return df, df_slice


def example2():
    data = {'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50]}
    df = pd.DataFrame(data)

    df_slice = df.copy()

    df_slice['A'] = df_slice['A'] * 2

    return df, df_slice


def example3():
    data = {'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50]}
    df = pd.DataFrame(data)

    df_slice = df.iloc[0:2, :]

    df_slice['A'] = df_slice['A'] * 2

    return df, df_slice


def example4():
    data = {'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50]}
    df = pd.DataFrame(data)

    df_slice = df.loc[0:2, ['A', 'B']]

    df_slice['A'] = df_slice['A'] * 2

    return df, df_slice


if __name__ == '__main__':
    examples = [example1, example2, example3, example4]

    for idx, example in enumerate(examples, start=1):
        df, df_slice = example()
        print(f"{MARK} EXAMPLE{idx} {MARK}\n"
              + "Original DataFrame:\n"
              + tabulate(df, headers='keys', tablefmt='pretty', showindex=False)
              + "\nModified Slice:\n"
              + tabulate(df_slice, headers='keys', tablefmt='pretty', showindex=False)
              + "\n")
