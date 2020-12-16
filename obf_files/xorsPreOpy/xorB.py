inputfile = open('malware','rb')
outputfile = open('decode', 'w+b')
byte = inputfile.read(1)
counter = 0
oper = 7
operr = 7
while byte != "":
    byte = ord(byte)
    oper = counter
    if 1 ==1:
      if counter % 5 ==1:
          operr = counter % 17
          operr += 1
          operr = operr * 4
          byte = byte ^ operr
      if counter % 3 ==1:
          operr = counter % 19
          operr += 1
          operr = operr * 5
          byte = byte ^ operr
      if counter % 2 ==1:
          operr = counter % 47
          operr += 1
          operr = operr * 2
          byte = byte ^ operr
      else:
          operr = counter % 31
          operr += 1
          operr = operr + 6
          byte = byte ^ operr
    outputfile.write('%c' % byte)
    byte = inputfile.read(1)
    counter += 1
outputfile.close()
