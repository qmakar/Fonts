# -*- coding: utf-8 -*-   
  

#---------------------------------Settings------------------------------#

# Directory containing fonts  
font_dir = '/Users/mak/Documents/Programming/Data/RUS_BDGT/'  
  
# Output  
out_dir = '/Users/mak/Documents/Programming/Data/Font-hand-written-russian-images/'  

# Characters to print
characters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
# characters = ['№','!', ')',',','.',':',';','@', '#','\'','\"','/','?', '<','>','%','&','*','(','$','-','|','[',']','{','}','+', '=', '\\', '~']
# characters = list(string.ascii_lowercase)
# characters = list(string.ascii_uppercase)
# characters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я' ]


# Background color   
background_colors = (0,)

# Character sizes  
font_sizes = (20, )  

# Distinct string between Upper\Lower case
padding = "_"

#-------------------------------- Imports ------------------------------#  
  
from PIL import Image  
from PIL import ImageDraw  
from PIL import ImageFont  
  
import os  
import string
from random import randint  
  
#-------------------------------- Cleanup ------------------------------#  
                      
def Cleanup():      
    # Delete ds_store file  
    if os.path.isfile(font_dir + '.DS_Store'):  
        os.unlink(font_dir + '.DS_Store')  
      
    # Delete all files from output directory  
    for file in os.listdir(out_dir):  
        file_path = os.path.join(out_dir, file)  
        if os.path.isfile(file_path):  
            os.unlink(file_path)  
    return  
  
#--------------------------- Generate Characters -----------------------#  
  
def GenerateCharacters():  
    k = 1  
    for dirname, dirnames, filenames in os.walk(font_dir):  
        # For each font do  
        for filename in filenames:  
            font_resource_file = os.path.join(dirname, filename)  
            if filename[0] == '.':
                continue
            for char in characters:  
                for font_size in font_sizes:  
                    if font_size > 0:  
                        for background_color in background_colors:  
                            character = unicode(char, 'utf-8')  
                            font = ImageFont.truetype(font_resource_file, font_size)  
                  
                            try:
                                (font_width, font_height) = font.getsize(character)  
                                image_size = font_height + 2
                                char_image = Image.new('L', (image_size, image_size), background_color)  
                  
                                draw = ImageDraw.Draw(char_image)  
                  
                                x = (image_size - font_width)/2 - 1 
                                y = (image_size - font_height)/2 - 1
                      
                                draw.text((x, y), character, (245 - background_color) + randint(0, 10) , font=font)  

                                # Final file name     
                                if character == ':':                 
                                    file_name = out_dir + "colon" + '/'+ str(k) + '-F' + str(font_size) + "-C" + str(background_color)  + '.jpg'
                                elif character == '.':  
                                    file_name = out_dir + "dot" + '/'+ str(k) + '-F' + str(font_size) + "-C" + str(background_color)  + '.jpg'
                                elif character == '/':  
                                    file_name = out_dir + "slash" + '/'+ str(k) + '-F' + str(font_size) + "-C" + str(background_color)  + '.jpg'
                                elif character == '\\':  
                                    file_name = out_dir + "back_slash" + '/'+ str(k) + '-F' + str(font_size) + "-C" + str(background_color)  + '.jpg'
                                elif character == '>':  
                                    file_name = out_dir + "greater" + '/'+ str(k) + '-F' + str(font_size) + "-C" + str(background_color)  + '.jpg'
                                elif character == '<':  
                                    file_name = out_dir + "less" + '/'+ str(k) + '-F' + str(font_size) + "-C" + str(background_color)  + '.jpg'
                                elif character == '?':  
                                    file_name = out_dir + "question" + '/'+ str(k) + '-F' + str(font_size) + "-C" + str(background_color)  + '.jpg'
                                elif character == '\"':  
                                    file_name = out_dir + "quotation_mark" + '/'+ str(k) + '-F' + str(font_size) + "-C" + str(background_color)  + '.jpg'
                                elif character == '*':  
                                    file_name = out_dir + "star" + '/'+ str(k) + '-F' + str(font_size) + "-C" + str(background_color)  + '.jpg'
                                elif character == '|':  
                                    file_name = out_dir + "vertical_line" + '/'+ str(k) + '-F' + str(font_size) + "-C" + str(background_color)  + '.jpg'
                                else: 
                                   file_name = out_dir  + character + padding +'/' + str(k) + '-F' + str(font_size) + "-C" + str(background_color)  + '.jpg'
                           
                                # Save image  
                                char_image.save(file_name, "JPEG")  
                                print file_name;  
                          
                            except:
                                pass
            k = k + 1  
    return  

#---------------------------------- Create folders -------------------------------#  
for elem in characters:
    if elem == ':':
        directory = out_dir + "colon"
    elif elem == '.':  
        directory = out_dir + "dot"
    elif elem == '/':  
        directory = out_dir + "slash"
    elif elem == '\\':  
        directory = out_dir + "back_slash"
    elif elem == '>':  
        directory = out_dir + "greater"
    elif elem == '<':  
        directory = out_dir + "less"
    elif elem == '?':  
        directory = out_dir + "question"
    elif elem == '\"':  
        directory = out_dir + "quotation_mark"
    elif elem == '*':  
        directory = out_dir + "star"
    elif elem == '|':  
        directory = out_dir + "vertical_line"
    else:
        directory = out_dir + elem + padding
    if not os.path.exists(directory):
        os.makedirs(directory)

         
#----------------------------------- Main --------------------------------#  
  
Cleanup()  
  
GenerateCharacters() 



