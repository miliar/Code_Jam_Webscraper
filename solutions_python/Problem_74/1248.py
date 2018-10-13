
def read_file( path ):
    readFile = open( path, 'r' )
    lines = readFile.readlines()
    return lines

# content je lista
def write_file( path, content ):
    writeFile = open( path, 'w' )
    writeFile.writelines( content )

