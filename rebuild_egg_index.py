import os

fp = open("eggs/index.html", 'w')

print >> fp, "<html><body><h1>Index of dist.socialplanning.org/eggs</h1><ul>"

for filename in sorted(os.listdir("eggs")):
    print >> fp, """<li><a href="/eggs/%s">%s</a></li>""" % (
        filename, filename)

print >> fp, "</ul></body></html>"
fp.close()
