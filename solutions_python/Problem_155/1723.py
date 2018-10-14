fp = r"C:\Yam\input.txt"
ofp = r"C:\Yam\output.txt"
with open(fp, 'rb') as reader:
    content = reader.read().splitlines()
writer = open(ofp, 'wb')

tests = int(content[0])
reader = 1
while reader <= tests:
    line = content[reader]
    ##################
    line = line.split()
    length, crowd = int(line[0]), line[1]
    crowd = crowd[:length+1]
    shy = 0
    standing = 0
    attending = 0
    while shy < len(crowd):
        if int(crowd[shy]) > 0:
            attending += max(0, shy-(standing+attending))
        standing += int(crowd[shy])
        print(crowd, shy, standing, attending)
        shy += 1
    ##################
    writer.write("Case #{x}: {y}\n".format(x=reader, y=attending))
    reader += 1
    
writer.close()