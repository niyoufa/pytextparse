import pdb
import sys
from handlers import HTMLRenderer
from markup import BasicTextParser
pdb.set_trace()
handler = HTMLRenderer()
parser = BasicTextParser(handler)
parser.parse(sys.argv[1])