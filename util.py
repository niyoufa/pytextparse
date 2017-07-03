import sys
import pdb

def lines(file):
    """
    生成器,在文本最后加一空行
    """
    for line in file: yield line
    yield '\n'

def blocks(file):
    """
    生成器,生成单独的文本块
    """
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

if __name__ == "__main__":
    f = open("case.txt")
    paras = []
    for block in blocks(f):
        paras.append(block)
    print(paras, len(paras))
