#! /usr/bin/env python
import urllib2
from xml.dom.minidom import parseString

#list of series
series_list = {'Newsroom': "http://showrss.karmorra.info/feeds/455.rss"}
series_list['Warehouse 13'] = "http://showrss.karmorra.info/feeds/182.rss"

# read
url = "http://showrss.karmorra.info/feeds/455.rss"


def read(url):
    content = urllib2.urlopen(url).read()

    d = parseString(content)

    item_elements = str(d.getElementsByTagName("item")[0].toxml())
    #print item_elements
    start_tag = "<link>"
    end_tag = "</link>"
    start = item_elements.find(start_tag)
    end = item_elements.find(end_tag)
    #print item_elements[start + len(start_tag): end]
    return item_elements[start + len(start_tag): end]  # first_link_line

#w_file.write(urllib2.urlopen(item_elements[start + len(start_tag): end]).read())
# write
#w_file = open("Downloads/newsroom.torrent", "w")
#print read(url)

w_file = open("series.torrent", "w")
w_file.write(read(url))
w_file.write(read(url))
w_file.close()
