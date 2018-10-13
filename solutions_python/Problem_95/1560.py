import os,sys

def readlines(filename):
  input=open(filename,'r')
  gtext=[]
  english = []
  l = input.readline()
  nl=int(l )
  for ii in range(nl):
    this_line = input.readline().split('\n')[0]
    gtext.append( this_line )
 
  l = input.readline()
  while(l !='' ):
    if (l.split('\n')[0] == 'Output'):
      for ii in range(nl):
        this_line = input.readline().split('\n')[0]
        english.append( this_line[9:] )
    l = input.readline()
  return gtext,english,nl

def build_dict(filename):
  gtext,english,nl = readlines(filename)
  this_dict = {}
  this_dict['z']='q'
  this_dict['q']='z'
  this_dict['e']='o'
  for g,e in zip(gtext,english):
    ngt = len(g)
    net = len(e)
    assert( ngt == net )
    for ii in range(ngt):
      if g[ii] not in this_dict:
        this_dict[ g[ii] ] = e[ii]
  return this_dict

def run(args):
  if(len(args)>0):
    this_dict = build_dict( args[0] )
  if(len(args)>1):
    gtext,english, nl = readlines(args[1])
    ii = 1
    print "Output"
    for g in gtext:
      str=''
      for gi in g:
        str=str+this_dict[gi]
      print "Case #%d: %s"%(ii,str)
      ii = ii + 1


if __name__ == "__main__":
  args=sys.argv[1:]
  run(args)
  
    
