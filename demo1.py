# 将多个xlsx文件合并成一个xlsx文件     是对于同一温度下不同浓度的
import pandas as pd
import os

# 定义一个包含所有.xlsx文件路径的列表
file_paths = [
    'Processed_SO2_data100/Extended100.xlsx',
    'Processed_SO2_data101/Extended101.xlsx',
    'Processed_SO2_data102/Extended102.xlsx',
    'Processed_SO2_data103/Extended103.xlsx',
    'Processed_SO2_data104/Extended104.xlsx',
    'Processed_SO2_data105/Extended105.xlsx',
    'Processed_SO2_data106/Extended106.xlsx',
    'Processed_SO2_data107/Extended107.xlsx',
    'Processed_SO2_data108/Extended108.xlsx',
    'Processed_SO2_data109/Extended109.xlsx',
    'Processed_SO2_data110/Extended110.xlsx',
    # 添加更多文件路径
]
dataframes = []
for file_path in file_paths:
    df = pd.read_excel(file_path, header=None)
    dataframes.append(df)
df_combined = pd.concat(dataframes, ignore_index=True)
print(df_combined.head())
output_file_path = 'Demo/1.xlsx'
df_combined.to_excel(output_file_path,index=False,header=False)
print(f"合并后的文件已保存至：{output_file_path}")


# # 将file_path路径中的xlsx表格的最后两列数据进行交换     是对同一浓度下不同温度的       将生成的xlsx的最后两列数据进行交换     是为了保证所有的最后一列为温度值，倒数第二列为浓度值
# import pandas as pd
# file_path = 'Processed_SO2_data129/Extended129.xlsx'
# output_file_path = 'Processed_SO2_data129/Extended129-1.xlsx'
# df = pd.read_excel(file_path,header=None)
# columns = df.columns.tolist()
# if len(columns) > 1:
#     last_col_name = columns[-1]
#     second_last_col_name = columns[-2]
#     temp = df[last_col_name].copy()  # 使用copy()以避免设置值时的链式赋值警告
#     df[last_col_name] = df[second_last_col_name]
#     df[second_last_col_name] = temp
# df.to_excel(output_file_path, index=False, header=False)
#
# # 如果你想要覆盖原文件，请取消注释下一行，并确保你已经做好了备份
# # df.to_excel(file_path, index=False)


#
# # 将多个xlsx文件合并成一个xlsx文件     是对于同一浓度下不同温度的
# import pandas as pd
# import os
#
# # 定义一个包含所有.xlsx文件路径的列表
# file_paths = [
#     'Processed_SO2_data120/Extended120-1.xlsx',
#     'Processed_SO2_data121/Extended121-1.xlsx',
#     'Processed_SO2_data122/Extended122-1.xlsx',
#     'Processed_SO2_data123/Extended123-1.xlsx',
#     'Processed_SO2_data124/Extended124-1.xlsx',
#     'Processed_SO2_data125/Extended125-1.xlsx',
#     'Processed_SO2_data126/Extended126-1.xlsx',
#     'Processed_SO2_data127/Extended127-1.xlsx',
#     'Processed_SO2_data128/Extended128-1.xlsx',
#     'Processed_SO2_data129/Extended129-1.xlsx',
#
# ]
#
# dataframes = []
# for file_path in file_paths:
#     df = pd.read_excel(file_path, header=None)
#     dataframes.append(df)
# df_combined = pd.concat(dataframes, ignore_index=True)
# print(df_combined.head())
# output_file_path = 'Demo/2.xlsx'
# df_combined.to_excel(output_file_path,index=False,header=False)
# print(f"合并后的文件已保存至：{output_file_path}")



# # 将多个xlsx文件合并成一个xlsx文件                是将所有同一温度下不同浓度合在一起的1.xlsx和所有同一浓度下不同温度合在一起的2.xlsx在一块合并到一起为3.xlsx
# import pandas as pd
# import os
#
# # 定义一个包含所有.xlsx文件路径的列表
# file_paths = [
#     'demo/1.xlsx',
#     'demo/2.xlsx',
# ]
#
# dataframes = []
# for file_path in file_paths:
#     df = pd.read_excel(file_path, header=None)
#     dataframes.append(df)
# df_combined = pd.concat(dataframes, ignore_index=True)
# print(df_combined.head())
# output_file_path = 'Demo/3.xlsx'
# df_combined.to_excel(output_file_path,index=False,header=False)
# print(f"合并后的文件已保存至：{output_file_path}")






# 以下都是测试数据    没有扩充

# # 将多个xlsx文件合并成一个xlsx文件     是对于同一温度下不同浓度的
# import pandas as pd
# import os
#
# # 定义一个包含所有.xlsx文件路径的列表
# file_paths = [
#     'Processed_SO2_data40/25-SO2_average_removebd.xlsx',
#     'Processed_SO2_data41/150-SO2_average_removebd.xlsx',
#     'Processed_SO2_data42/200-SO2_average_removebd.xlsx',
#     'Processed_SO2_data43/250-SO2_average_removebd.xlsx',
#     'Processed_SO2_data44/300-SO2_average_removebd.xlsx',
#     'Processed_SO2_data45/350-SO2_average_removebd.xlsx',
#     'Processed_SO2_data46/400-SO2_average_removebd.xlsx',
#     'Processed_SO2_data47/450-SO2_average_removebd.xlsx',
#     'Processed_SO2_data48/500-SO2_average_removebd.xlsx',
#     'Processed_SO2_data49/550-SO2_average_removebd.xlsx',
#     'Processed_SO2_data50/600-SO2_average_removebd.xlsx',
#     # 添加更多文件路径
# ]
# dataframes = []
# for file_path in file_paths:
#     df = pd.read_excel(file_path, header=None)
#     dataframes.append(df)
# df_combined = pd.concat(dataframes, ignore_index=True)
# print(df_combined.head())
# output_file_path = 'Demo/4.xlsx'
# df_combined.to_excel(output_file_path,index=False,header=False)
# print(f"合并后的文件已保存至：{output_file_path}")




# import pandas as pd
# import os
#
# # 定义一个包含所有.xlsx文件路径的列表
# file_paths = [
#     'Processed_SO2_data51/200-SO2_average_removebd.xlsx',
#     'Processed_SO2_data52/100-SO2_average_removebd.xlsx',
#     'Processed_SO2_data53/300-SO2_average_removebd.xlsx',
#     'Processed_SO2_data54/400-SO2_average_removebd.xlsx',
#     'Processed_SO2_data55/500-SO2_average_removebd.xlsx',
#     'Processed_SO2_data56/150-SO2_average_removebd.xlsx',
#     'Processed_SO2_data57/250-SO2_average_removebd.xlsx',
#     'Processed_SO2_data58/350-SO2_average_removebd.xlsx',
#     'Processed_SO2_data59/450-SO2_average_removebd.xlsx',
#     'Processed_SO2_data60/550-SO2_average_removebd.xlsx',
#     # 添加更多文件路径
# ]
# dataframes = []
# for file_path in file_paths:
#     df = pd.read_excel(file_path, header=None)
#     dataframes.append(df)
# df_combined = pd.concat(dataframes, ignore_index=True)
# print(df_combined.head())
# output_file_path = 'Demo/5.xlsx'
# df_combined.to_excel(output_file_path,index=False,header=False)
# print(f"合并后的文件已保存至：{output_file_path}")




# # 将多个xlsx文件合并成一个xlsx文件                是将所有同一温度下不同浓度合在一起的4.xlsx和所有同一浓度下不同温度合在一起的5.xlsx在一块合并到一起为6.xlsx
# import pandas as pd
# import os
#
# # 定义一个包含所有.xlsx文件路径的列表
# file_paths = [
#     'demo/4.xlsx',
#     'demo/5.xlsx',
# ]
#
# dataframes = []
# for file_path in file_paths:
#     df = pd.read_excel(file_path, header=None)
#     dataframes.append(df)
# df_combined = pd.concat(dataframes, ignore_index=True)
# print(df_combined.head())
# output_file_path = 'Demo/6.xlsx'
# df_combined.to_excel(output_file_path,index=False,header=False)
# print(f"合并后的文件已保存至：{output_file_path}")



