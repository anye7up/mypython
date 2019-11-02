#coding:utf-8
'''
将当前文件夹下（包含子目录）的若干个表格汇到一张表格上。
仅为初步版本，须根据需要进行改写。
'''

import os
import xlrd
import xlwt

# 读取表格
# 文件名 = 班级名
# 文件夹名 = 年段 + 系名
dirs = os.listdir()

# 新建工作簿
ntb = xlwt.Workbook()
# 创建工作表
ntb_st=ntb.add_sheet(u'sheet1', cell_overwrite_ok=True)
a = [u'学（工）号',u'一级部门',u'二级部门',u'三级部门',u'四级部门']
ii = 1    # 索引
# 表格第一行字段
for i in range(0,5):
    ntb_st.write(0,i,a[i])


for folder in dirs:
    #print(os.listdir(tb))
    p = os.path.join( os.getcwd(), folder)
    # print( p)
    if os.path.isdir(p):
        fils = os.listdir(p)
        for tb in fils:
            filename = os.path.join( p , os.path.basename(tb))
            print(filename)
            # 打开工作薄
            wb = xlrd.open_workbook(filename)
            # 打开工作表
            st = wb.sheet_by_index(0)
            # 获取Sheet表名、行、列
            print(st.name, st.nrows, st.ncols)
            # 获取学工号，以及将路径分解成四级部门名
            for i in range(1,st.nrows):
                print(str(st.cell(i,0))[5:-1], folder[:5], folder[5:], tb[:-4])
                ntb_st.write(ii,0, str(st.cell(i,0))[6:-1])
                ntb_st.write(ii,1,folder[:5])
                ntb_st.write(ii,2,folder[5:])
                ntb_st.write(ii,3,tb[:-4])
                ii = ii + 1

# 将表格所在目录写入表格
ntb.save('all.xls')

