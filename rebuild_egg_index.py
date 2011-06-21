"""
Before you run this:

  $ git submodule init eggs

After you run this:

  $ cd eggs; git add index.html; git push
  $ cd ..; git add eggs; git push

"""

import os
import time

def convert_bytes(bytes):
    bytes = float(bytes)
    if bytes >= 1099511627776:
        terabytes = bytes / 1099511627776
        size = '%.2fT' % terabytes
    elif bytes >= 1073741824:
        gigabytes = bytes / 1073741824
        size = '%.2fG' % gigabytes
    elif bytes >= 1048576:
        megabytes = bytes / 1048576
        size = '%.2fM' % megabytes
    elif bytes >= 1024:
        kilobytes = bytes / 1024
        size = '%.2fK' % kilobytes
    else:
        size = '%.2fb' % bytes
    return size

fp = open("eggs/index.html", 'w')

print >> fp, "<html><body><h1>Index of dist.socialplanning.org/eggs</h1><table><tr><th>Filename</th><th>Size</th><th>Last Modified</th></tr>"

for filename in sorted(os.listdir("eggs")):
    if filename.startswith("."):
        continue
    print >> fp, """<tr><td><a href="/eggs/%s">%s</a></td>""" % (
        filename, filename)
    stat = os.stat("eggs/" + filename)
    print >> fp, """<td>%s</td><td>%s</td></tr>""" % (
        convert_bytes(stat.st_size),
        time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(stat.st_mtime)),
        )
        
print >> fp, "</table></body></html>"
fp.close()
