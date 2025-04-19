import os
 
backup_list = [
['//mnt/Movies3/Jellyfin Library/Kids Movies', 'Kids_Movies.txt', 'subfolders'],
['//mnt/Movies3/Jellyfin Library/Kids TV Shows', 'Kids_TV_Shows.txt', 'folders'],
['//mnt/Movies1/', 'Movies.txt', 'subfolders'],
['//mnt/Movies3/Jellyfin Library/Music', 'Music.txt', 'subfolders'],
['//mnt/Media/Video/TV SHOWS','TV_Shows.txt', 'folders']
]

for item in backup_list:

	f = open(item[1], "w").close()	# erase contents of file

	if item[2] == 'folders':

		for dirs in os.listdir(item[0]):
			with open(item[1], "a") as f:
				f.write(dirs)
				f.write("\r\n")

	elif item[2] == 'files':

		for root, dirs, files in os.walk(item[0]):

			for name in files:
				with open(item[1], "a") as f:
					f.write(name)
					f.write("\r\n")

	elif item[2] == 'subfolders':

		for dirpath, dirnames, filenames in os.walk(item[0]):
			for dirname in dirnames:
				with open(item[1], "a") as f:
					f.write(dirname)
					f.write("\r\n")