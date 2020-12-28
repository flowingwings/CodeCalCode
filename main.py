# coding=gbk
import os
import keyword


def isCommentLine(lt):
    # ltLine = line.strip()
    return lt[0].startswith('#')


def isWhiteLine(lt):
    # ltLine = line.strip()
    return len(lt) == 0


def nonWhiteChars(lt):
    # ltLine = line.strip()
    count = 0
    for w in lt:
        if w == '#':
            break
        count += len(w)
    return count


idleLibPath = 'C:/Users/FlowingWings/AppData/Local/Programs/Python/Python38/Lib/idlelib'
# idleLibPath = 'C:/Users/FlowingWings/AppData/Local/Programs/Python/Python38/Lib/html/__pycache__'
files = os.listdir(idleLibPath)
s = []
keyList = keyword.kwlist

cttLnCnt = 0  # content line count
cttCharCnt = 0  # content character count
d = {}
for i in keyList:
    d[i] = 0

# nosptxt = open(idleLibPath+'/no.txt', 'w')

for file in files:
    if file.endswith(".py") and not os.path.isdir(idleLibPath + '/' + file):
        f = open(idleLibPath + '/' + file, encoding='gbk', errors='ignore')
        fileLines = f.readlines()
        inCmtScp = False
        for line in fileLines:
            line = line.strip()
            ltLine = line.split()
            if line.startswith('\'\'\'') or line.startswith('\"\"\"'):
                inCmtScp = not inCmtScp
                if not inCmtScp:
                    continue
            if inCmtScp:
                continue
            if isWhiteLine(ltLine) or isCommentLine(ltLine):
                continue
            cttLnCnt += 1
            for word in ltLine:
                if word.startswith('#'):
                    break
                cttCharCnt += len(word)
                # nosptxt.write(word)
                if word in keyList:
                    d[word] += 1

print('非注释非空白行数为：%d' % (cttLnCnt))
print('非注释非空白字符数为：%d' % (cttCharCnt))
print('各关键字出现次数为：', d)
