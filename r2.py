def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	allen_pic_count = 0
	allen_sticker_count = 0
	allen_msg_count = 0
	viki_sticker_count = 0
	viki_pic_count = 0
	viki_msg_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count = allen_sticker_count + 1
			elif s[2] == '圖片':
				allen_pic_count = allen_pic_count + 1
			else:
				for msg in s[2:]:
					allen_msg_count = allen_msg_count + len(msg)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_pic_count += 1
			else:
				for msg in s[2:]:
					viki_msg_count += len(msg)
	print('Allen 傳了', allen_sticker_count, '張貼圖')
	print('Allen 傳了', allen_pic_count, '張圖片')
	print('Allen 傳了', allen_msg_count, '個字')
	print('Viki 傳了', viki_sticker_count, '張貼圖')
	print('Viki 傳了', viki_pic_count, '張圖片')
	print('Viki 傳了', viki_msg_count, '個字')



def main():
	lines = read_file('LINE-Viki.txt')
	convert(lines)


main()