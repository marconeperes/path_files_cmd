#! /usr/bin/python

import os, sys, getopt

#	get the arguments
argv = sys.argv[1:]

path=""
files=""
cmd=""

#	Find arguments
try:
	opts, args = getopt.getopt(argv, "p:e:c:", ["path=", "extension=", "command="] )
	for option, value in opts:
		if option in ("-p", "--path"):
			path=value
		elif option in ("-e", "--extension"):
			files=value
		elif option in ("-c", "--command"):
			cmd=value
		else:
			print ('[FATAL1]\n\tUnknow option: ', option)

	if "" in (path, files, cmd):
		print '[FATA2]\n\tUse - path_file_cmd -p "<a root path>" -e "*.ext" -c "ls -l \%f"'
except getopt.GetoptError:
	print '[FATAL3]\n\tUse - path_file_cmd -p "<a root path>" -e "*.ext" -c "ls -l \%f"'
	sys.exit(2)

#	In this point, all arguments was setted
#print opts
