# #!/usr/bin/env python3

import os
import sys
import plistlib

xml_file = sys.argv[0]

f = plistlib.readPlist(xml_file)

tp_dict = {}

tableplus_favorites_dir = os.path.expanduser('~') + "/Library/Application Support/com.tinyapp.TablePlus/Cache/Favorite/SequelPro"

print("Reading Sequel Pro Favorites file...")
for dict in f["queryFavorites"]:
	tp_dict[dict["name"]] = dict["query"]

print("Writing favorites files for TablePlus...")
for fav, query in tp_dict.items():
	filename = fav + ".sql"
	with open(filename, 'w') as file:
		file.write(query)

if not os.path.exists(tableplus_favorites_dir):
	os.makedirs(tableplus_favorites_dir)

print("Moving sql files to {}".format(tableplus_favorites_dir))
all_files = os.listdir('.')
for f in all_files:
	if f.endswith('.sql'):
		os.rename(f, tableplus_favorites_dir + "/" + f)

print("Done.")
