"""
整体是一段拟合，数据集大小浓度等比例扩充
"""
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt  # 用于画图
import os
from pandas import DataFrame

def to_pkl(path):
    # Read excel files
    df1 = DataFrame(pd.read_excel(path))
    dir_name = os.path.dirname(path)
    base_name = os.path.basename(path)
    suffix = base_name.split(".")[0]
    path_ = dir_name + "/" + suffix + ".pkl"
    df1.to_pickle(path_)
    return path_


def expansion_one_section_fitting(temperature, diff_all):
    absor = np.array(diff_all)
    temperature = temperature.squeeze()
    temperature_all = np.linspace(min(temperature), max(temperature), 1000)
    absor_new = np.empty((len(temperature_all), absor.shape[1]))
    for row_index in range(0, absor.shape[1]):
        row = absor[:,row_index]
        coefficients = np.polyfit(temperature, row, 4)
        poly_equation = np.poly1d(coefficients)
        y = poly_equation(temperature_all)
        absor_new[:,row_index] = y
        plt.figure(1)
        plt.plot(temperature, row, 'o', label='point')
        plt.draw()
    plt.plot(temperature_all, absor_new, '-', label='fit line')
    plt.show()

    df_temperature_new = pd.DataFrame(temperature_all)
    df_absor_new = pd.DataFrame(absor_new)
    new_row_length = df_absor_new.shape[1]
    new_row_data = pd.Series(range(1, new_row_length + 3))
    new_row_df = new_row_data.to_frame().T
    constant_value = 550
    new_column_data1 = pd.Series([constant_value] * df_absor_new.shape[0])
    with pd.ExcelWriter('Processed_SO2_data129/Extended129.xlsx') as writer:
        new_row_df.to_excel(writer, sheet_name="temperature_new", startrow=0, index=False, header=False)
        df_absor_new.to_excel(writer, sheet_name='temperature_new', startrow=1,index=False, header=False)
        df_temperature_new.to_excel(writer, sheet_name='temperature_new',startrow=1,startcol=df_absor_new.shape[1],index=False, header=False)
        new_column_data1.to_excel(writer, sheet_name='temperature_new', startrow=1,startcol=df_absor_new.shape[1] + 1, index=False, header=False)
    print(f"数据扩展已完成")

    to_pkl("Processed_SO2_data129/Extended129.xlsx")
    return temperature_all, absor_new

def run(path3):
    absorbance = pd.read_excel(path3, sheet_name='all', header=None)
    absorbance = absorbance.iloc[2:, :-1]
    temperature = pd.read_excel(path3, sheet_name='all', header=None)
    temperature = temperature.iloc[2:,-1]
    absorbance = np.array(absorbance)
    temperature = np.array(temperature)
    temperature_all, absor_new = expansion_one_section_fitting(temperature, absorbance)






