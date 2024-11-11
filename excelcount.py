import pandas as pd
import openpyxl
import warnings

warnings.simplefilter(action='ignore', category=UserWarning)
print('输入文件名:', end='')
ans = 0
excel_file = pd.ExcelFile(input())
sheet_count = len(excel_file.sheet_names)
for i in range(1, sheet_count):
    data = pd.read_excel(excel_file, sheet_name=i, skiprows=6)
    previous_row = data.shift()
    diff = (data != previous_row).astype(int)
    diff_count = diff.sum(axis=1)
    print(diff_count.sum() - data.shape[1])
    ans += diff_count.sum() - data.shape[1]
print('总共有', ans, '条数据发生变化')


