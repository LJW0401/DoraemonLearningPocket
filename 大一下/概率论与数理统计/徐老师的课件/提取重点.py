import os
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
from reportlab.pdfgen import canvas
import datetime

start_time = datetime.datetime.now()

# 输入文件夹路径和关键字
folder_path = 'E:\\#LJW\\#PolarBear_RM\\DoraemonLearningPocket\\大一下\\概率论与数理统计'
keywords = ['小结','复习']

# 创建一个新的PDF文件
output_pdf = PdfWriter()

# 遍历文件夹中的每个PDF文件
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        if filename == '概率统计各章总结.pdf':
            break
        print('正在处理:', filename)
        filepath = os.path.join(folder_path, filename)

        # 打开PDF文件
        with open(filepath, 'rb') as f:
            pdf = PdfReader(f)
            if filename[:3] == '1-3':
                page = pdf.pages[1]
                output_pdf.add_page(page)
            elif filename[:3] == '1-5':
                page = pdf.pages[1]
                output_pdf.add_page(page)
            elif filename[:3] == '3-1':
                for i in range(1,2):
                    page = pdf.pages[1]
                    output_pdf.add_page(page)
            elif filename[:3] == '3-2':
                for i in range(1,2):
                    page = pdf.pages[1]
                    output_pdf.add_page(page)
                    
            # 遍历PDF的每一页
            for page_num in range(len(pdf.pages)):
                print('正在处理第', page_num + 1, '页')
                page = pdf.pages[page_num]

                # 提取页面文本内容
                text = page.extract_text()

                # 如果页面包含关键字，则添加到新的PDF文件中
                has_keyword = False
                for keyword in keywords:
                    if keyword in text:
                        has_keyword = True
                        break
                if has_keyword:
                    output_pdf.add_page(page)

# 保存新的PDF文件
output_filepath = os.path.join(folder_path, 'new_pdf.pdf')
# print('正在创建新的PDF文件:', output_filepath)
with open(output_filepath, 'wb') as f:
    output_pdf.write(f)

print('新的PDF文件已创建:', output_filepath)

finish_time = datetime.datetime.now()
print('\n耗时:', finish_time - start_time)