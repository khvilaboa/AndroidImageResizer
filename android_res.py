import os, sys
import Image

sizes = {"xhdpi": 96, "hdpi": 72,"mdpi": 48,"ldpi": 36}

def splitFileName(name):
	sp = os.path.splitext(name)
	if len(sp)<=1: return sp[0], ""
	return sp[0], sp[1]
	
def ensureDir(f):
	d = os.path.dirname(f)
	if not os.path.exists(d):
		os.makedirs(d)

if len(sys.argv) < 2:
	print "Usage: resize.py image [more_images] android_res"
	sys.exit(0)

outdir = sys.argv[-1]
if outdir[-1]=="\\": outdir=outdir[:-1]

for file in sys.argv[1:-1]:
	for size in sizes:
		try:
			im = Image.open(file)
			
			dim = sizes[size]
			im.thumbnail((dim,dim), Image.ANTIALIAS)

			name, ext = splitFileName(file) # ...

			outpath = "%s/drawable-%s" % (outdir, size)
			
			if not os.path.exists(outpath):
				os.makedirs(outpath)
			
			im.save("%s\\%s%s" % (outpath, name, ext))
		except IOError:
			print "\nError opening %s" % file
			
			