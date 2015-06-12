# -*- coding:utf-8 -*-

import random

code_list = []

#生成指定长度的随机字符串，由大写字母组成
def random_string(length):
	str = ""
	for i in range(length):
		ramdom_int = random.randint(0,26)
		random_char = unichr(ord('A') + ramdom_int)
		str += random_char
	return str

#拼接随机字符串	
def random_code():
	code = ""
	for i in range(4):
		code += random_string(4)
		code += "-"
	return code[0:-1]
	
#检查随机字符串是否重复
def check_repeat(code):
	if code_list.count(code) == 0:
		return True
	else:
		return False

#打印随机字符串列表		
def print_list():
	for code in code_list:
		print code
	
if __name__=="__main__":
	for i in range(200):
		code = random_code()
		if check_repeat(code):
			code_list.append(code)
	print_list()
	