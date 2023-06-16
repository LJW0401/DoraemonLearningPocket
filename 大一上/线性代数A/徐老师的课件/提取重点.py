import os
from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter
from reportlab.pdfgen import canvas
import datetime

start_time = datetime.datetime.now()

# 输入文件夹路径和关键字
folder_path = 'E:\#LJW\#PolarBear_RM\DoraemonLearningPocket\大一上\线性代数A\徐老师的课件'
keyword = '复习'

# 创建一个新的PDF文件
output_pdf = PdfWriter()

# 遍历文件夹中的每个PDF文件
for filename in os.listdir(folder_path):
    print('正在处理:', filename)
    if filename.endswith('.pdf'):
        filepath = os.path.join(folder_path, filename)

        # 打开PDF文件
        with open(filepath, 'rb') as f:
            pdf = PdfReader(f)

            # 遍历PDF的每一页
            for page_num in range(len(pdf.pages)):
                print('正在处理第', page_num + 1, '页')
                page = pdf.pages[page_num]

                # 提取页面文本内容
                text = page.extract_text()

                # 如果页面包含关键字，则添加到新的PDF文件中
                if keyword in text:
                    output_pdf.add_page(page)

# 保存新的PDF文件
output_filepath = os.path.join(folder_path, 'new_pdf.pdf')
# print('正在创建新的PDF文件:', output_filepath)
with open(output_filepath, 'wb') as f:
    output_pdf.write(f)

print('新的PDF文件已创建:', output_filepath)

finish_time = datetime.datetime.now()
print('\n耗时:', finish_time - start_time)