#-*- coding:utf-8 -*-
"""
" ip2region python seacher client module
"
" Autho: JerryHuang<mycheryhr@gmail.com>
" Date : 2019-05-22
" Usage: python /home/ip2region/binding/python/ip-region.py /home/ip2region/data/ip2region.db 8.8.8.8
"""
import struct, sys, os, time
from platform import python_version

from ip2Region import Ip2Region

def testSearch():
    """
    " ip2region test function
    """
    argLen     = len(sys.argv)
    version    = python_version()
    algorithms = ["binary", "b-tree", "memory"]

    if argLen < 2:
        print("Usage: python testSearcher.py [ip2region db file] [alrogrithm]")
        print("Algorithm: %s" % ", ".join(algorithms))
        return 0

    dbFile = sys.argv[1]

    if (not os.path.isfile(dbFile)) or (not os.path.exists(dbFile)):
        print("[Error]: Specified db file is not exists.")
        return 0

    if argLen > 2:
        algorithm = sys.argv[2]
    try:
        algorithms.index(algorithm)
    except Exception as e:
        algorithm = "b-tree"

    searcher = Ip2Region(dbFile)


    line = sys.argv[2].strip()

    if line == "":
        print("[Error]: Invalid ip address.")
    elif line == "quit":
        print("[Info]: Thanks for your use, Bye.")
    if not searcher.isip(line):
        print("[Error]: Invalid ip address.")

    try:
        sTime = time.time()*1000
        if algorithm == "binary":
            data = searcher.binarySearch(line)
        elif algorithm == "memory":
            data = searcher.memorySearch(line)
        else:
            data = searcher.btreeSearch(line)
        eTime = time.time()*1000
        # print("%s|%s in %5f millseconds" % (data["city_id"], data["region"].decode('utf-8'), eTime - sTime))
        print("%s|%s" % (line, data["region"].decode('utf-8')))
    except Exception as e:
        print("[Error]: %s" % e)

    searcher.close()

if __name__ == "__main__":
    testSearch()
