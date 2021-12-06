# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import jieba.analyse
import numpy as np
from PIL import Image
import random


# 01-英文分词测试
# 打开文本
# text = open('constitution.txt').read()
# # 生成对象
# wc = WordCloud().generate(text)
# # 显示词云
# plt.imshow(wc, interpolation='bilinear')
# plt.axis('off')
# plt.show()
#
# # 保存到文件
# wc.to_file("01-worldcloud.png")

#02-西游记分词测试
# text2 = open('xyj.txt').read()
# text2 = ' '.join(jieba.cut(text2))  #结巴中文分词
# # print(text2[:100])
# wc2 = WordCloud(font_path='Hiragino.ttf',width=800,height=600,mode='RGBA',background_color=None).generate(text2)
# plt.imshow(wc2,interpolation='bilinear')
# plt.axis('off')
# plt.show()
# wc2.to_file("02-xyj-wordcloud.png")

#03-蒙版
# text3 = open('xyj.txt').read()
# text3 = " ".join(jieba.cut(text3))
#
# mask = np.array(Image.open("black_mask.png"))
# wc3 = WordCloud(mask=mask, font_path="Hiragino.ttf", mode='RGBA', background_color=None).generate(text3)
# plt.imshow(wc3, interpolation='bilinear')
# plt.show()
# wc3.to_file("03-xyj-wordcloud.png")

#04-从蒙版提取颜色
# text4 = open('xyj.txt').read()
# text4 = " ".join(jieba.cut(text3))
#
# mask = np.array(Image.open("color_mask.png"))
# wc4 = WordCloud(mask=mask, font_path="Hiragino.ttf", mode='RGBA', background_color=None).generate(text4)
# #从图片中生成颜色
# image_colors = ImageColorGenerator(mask)
# wc4.recolor(color_func=image_colors)
#
# plt.imshow(wc4, interpolation='bilinear')
# plt.show()
# wc4.to_file("04-xyj-wordcloud.png")


#05-从蒙版提取颜色
# text5 = open('xyj.txt').read()
# text5 = " ".join(jieba.cut(text5))
# # 颜色函数
# def random_color(word,font_size,position,orientation,font_path,random_state):
#     s = 'hsl(0,%d%%,%d%%)' % (random.randint(60,80), random.randint(60,80))
#     # print(s)
#     return s
#
#
# mask = np.array(Image.open("color_mask.png"))
# wc5 = WordCloud(color_func=random_color,mask=mask, font_path="Hiragino.ttf", mode='RGBA', background_color=None).generate(text5)
# #从图片中生成颜色
# image_colors = ImageColorGenerator(mask)
# wc5.recolor(color_func=image_colors)
#
# plt.imshow(wc5, interpolation='bilinear')
# plt.show()
# wc5.to_file("05-xyj-wordcloud.png")

#06-提取关键词和权重
text6 = open('xyj.txt').read()

# 提取关键词和权重
freq = jieba.analyse.extract_tags(text6, topK = 200, withWeight = True)
print(freq[:20])
freq = {i[0]: i[1] for i in freq}  #转换为字典
print(freq)
# text6 = " ".join(jieba.cut(text5))
# 颜色函数
# def random_color(word,font_size,position,orientation,font_path,random_state):
#     s = 'hsl(0,%d%%,%d%%)' % (random.randint(60,80), random.randint(60,80))
#     # print(s)
#     return s

mask = np.array(Image.open("color_mask.png"))
wc6 = WordCloud(mask=mask, font_path="Hiragino.ttf", mode='RGBA', background_color=None).generate_from_frequencies(freq)
#从图片中生成颜色
image_colors = ImageColorGenerator(mask)
wc6.recolor(color_func=image_colors)

plt.imshow(wc6, interpolation='bilinear')
plt.show()
wc6.to_file("06-xyj-wordcloud.png")

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
