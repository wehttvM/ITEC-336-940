import sys
import os
import glob

file_list = glob.glob("*.png") + glob.glob("*.jpg") + glob.glob("*.jpeg")

for x in range(0, len(file_list)):
	filename, file_extension = os.path.splitext(file_list[x])
	run_str = 'ffmpeg -i "' + file_list[x] + '" -vf scale=300:300 "'  + filename + '_x300.png"'
	os.system(run_str)