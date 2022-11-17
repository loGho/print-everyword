import random
import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def print_every_word(article_path, ttf_path, result_path, background_path,
                     font_size, row_length, column_length,
                     upper_margin, left_margin,
                     left_ascii_margin, up_down_uniformity):
    font = ImageFont.truetype(ttf_path, font_size)
    article_file = open(article_path, 'r', encoding='utf-8')
    article_buf = article_file.read()
    # print(article_buf[3])
    article_file.close()
    article_length = len(article_buf)
    # 首个字符所处的竖向起始像素位置
    top_loc = 33
    # 首个字符所处的横向起始像素位置
    left_loc = 50
    # 当前页编码
    page_index = 1
    word_index = 0
    # 对字母数字的像素位置的重新处理的变量
    ascii_indent_bias = 0
    while word_index < article_length:
        top_loc = 33
        left_loc = 50
        background_img = Image.open(background_path)
        draw = ImageDraw.Draw(background_img)
        for i in range(row_length):
            if i == 1:
                top_loc += 10
            j = 0
            while j < column_length:
                mess_top_loc = top_loc
                if word_index >= article_length:
                    break
                if article_buf[word_index] == '\n':
                    word_index += 1
                    break
                print("i", i, "j", j, "top_loc", top_loc, "left_loc",
                      left_loc, "cur_char ", article_buf[word_index])
                mess_top_loc += random.random() * up_down_uniformity / 2
                draw.text((left_loc, mess_top_loc),
                          article_buf[word_index], (0, 0, 0),
                          font=font)
                if article_buf[word_index].isascii():
                    left_loc += left_ascii_margin
                    ascii_indent_bias += 1
                    j += 1 if ascii_indent_bias % 2 == 0 else 0

                else:
                    left_loc += left_margin
                    j += 1
                word_index += 1
            top_loc += upper_margin + random.random() * up_down_uniformity / 2
            left_loc = 50

            if word_index >= article_length:
                break
        background_img.save(result_path + str(page_index) + ".png")
        background_img.show()
        # time.sleep(20000)
        page_index += 1


if __name__ == "__main__":
    # 文字存放的文件位置
    txt_path = 'resources/text.txt'
    # 文字所采用的字体，可查找ttf手写字体资源进行替换
    ttf_path = "resources/normal-hand.TTF"
    # 输出文件位置
    save_path = "./result/"
    # 背景图片文件位置
    background_path = './resources/background-a4-recommend.jpg'
    # 每个字符的大小
    font_size = 30
    # 整个页面的行数
    row_length = 39
    # 每行的字符数(非ASCII码字符)
    column_length = 39
    # 每个字符占的纵向像素
    upper_margin = 34
    # 每个非ASCII字符占的横向像素
    left_margin = 24
    # 每个ASCII字符占的横向像素
    left_ascii_margin = 14
    # 一行中每个字符的上下偏离程度,建议0-10,数值越大越不整齐
    up_down_uniformity = 2

    print_every_word(txt_path, ttf_path, save_path,background_path, font_size, row_length, column_length, upper_margin, left_margin,
                     left_ascii_margin, up_down_uniformity)
    print("Success, Check your homework in the result directory!")
