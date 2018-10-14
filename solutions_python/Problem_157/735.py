import sys
import math

mul = {'11':'1','1i':'i','1j':'j','1k':'k','12':'2','1l':'l','1m':'m','1n':'n',
       'i1':'i','ii':'2','ij':'k','ik':'m','i2':'l','il':'1','im':'n','in':'j',
       'j1':'j','ji':'n','jj':'2','jk':'i','j2':'m','jl':'k','jm':'1','jn':'l',
       'k1':'k','ki':'j','kj':'l','kk':'2','k2':'n','kl':'m','km':'i','kn':'1',
       '21':'2','2i':'l','2j':'m','2k':'n','22':'1','2l':'i','2m':'j','2n':'k',
       'l1':'l','li':'1','lj':'n','lk':'j','l2':'i','ll':'2','lm':'k','ln':'m',
       'm1':'m','mi':'k','mj':'1','mk':'l','m2':'j','ml':'n','mm':'2','mn':'i',
       'n1':'n','ni':'m','nj':'i','nk':'1','n2':'k','nl':'j','nm':'l','nn':'2'}

uul = {'11':'1','1i':'i','1j':'j','1k':'k','12':'2','1l':'l','1m':'m','1n':'n',
       'i1':'l','ii':'1','ij':'n','ik':'j','i2':'i','il':'2','im':'k','in':'m',
       'j1':'j','ji':'n','jj':'2','jk':'i','j2':'m','jl':'k','jm':'1','jn':'l',
       'k1':'k','ki':'j','kj':'l','kk':'2','k2':'n','kl':'m','km':'i','kn':'1',
       '21':'2','2i':'l','2j':'m','2k':'n','22':'1','2l':'i','2m':'j','2n':'k',
       'l1':'l','li':'1','lj':'n','lk':'j','l2':'i','ll':'2','lm':'k','ln':'m',
       'm1':'m','mi':'k','mj':'1','mk':'l','m2':'j','ml':'n','mm':'2','mn':'i',
       'n1':'n','ni':'m','nj':'i','nk':'1','n2':'k','nl':'j','nm':'l','nn':'2'}
 
lines = sys.stdin.read().split('\n')

result = ''

for k in range( 0, int(lines[0]) ):
  repeat = int( lines[k*2+1].split(' ')[1] )

  edsger = lines[k*2+2]

  product = '1'

  if repeat * len( edsger ) < 3:
    result = 'NO'
  else:

    p1 = '1'
    p2 = '1'
    p3 = '1'

    for l in range( 0, len( edsger ) ):
      product = mul[ product + edsger[l] ]
      #print(product)

    #print('FIRST')
    if product=='1' or (product=='i' or product=='j' or product=='k' or product=='l' or product=='m' or product=='n') and repeat%4!=2 or product=='2' and repeat%2!=1: #
      result = 'NO'
    else:
      result = 'MAYBE'

  if result == 'MAYBE':
    #index1 = 0
    #index2 = 1
    #split1 = (index1%len(edsger),index1/len(edsger))
    #split2 = (index2%len(edsger),index2/len(edsger))
    #print( split1)
    #print(split2)
    #prod1 = edsger[split1[0]]
    #prod2 = edsger[split2[0]]
    #prod12 = mul[ prod1+prod2]
    #prod3 = mul[ prod12 + product ]
    #if prod12 != '1' and prod12 != '2':
    #  prod3 = mul[ '2'+ prod3 ]
    
    #print( prod1 + ' ' + prod2 + ' ' + mul[ prod1+prod2 ] + ' ' + prod3 )

    prod1 = '1'
    prod2 = '1'
    product = '2'
    prod3 = product
    for m in range( 0, len(edsger)*repeat-2):
      split1 = (m%len(edsger),m/len(edsger))
      prod1 = mul[ prod1 + edsger[ split1[0] ] ]
      #split2 = ((m+1)%len(edsger),(m+1)/len(edsger))
      #prod2 = edsger[ split2[0] ]
      #prod12 = mul[ prod1 + prod2 ]
      #prod3 = mul[ prod12 + product ]
      #if prod12 != '1' and prod12 != '2':
      #  prod3 = mul[ '2'+ prod3 ]

      #print( prod1 + ' ' + prod2 + ' ' + mul[ prod1+prod2 ] + ' ' + prod3 + ' ' + product )
      prod2 = '1'
      if prod1 == 'i':
        #print('YAY?')
        for n in range( m+1, len(edsger)*repeat-1):

          split2 = (n%len(edsger),n/len(edsger))
          prod2 = mul[ prod2 + edsger[ split2[0] ] ]
          prod12 = mul[ prod1+prod2]
          prod3 = mul[ prod12 + product ]
          if prod12 != '1' and prod12 != '2':
            prod3 = mul[ '2'+ prod3 ]

          #print( ' ' + prod1 + ' ' + prod2 + ' ' + mul[ prod1+prod2 ] + ' ' + prod3 + ' ' + product)
          if prod2 == 'j' and prod3 == 'k':
            result = 'YES'
            break

        if result == 'YES':
          break


  if result == 'MAYBE':
    result = 'NO'

  sys.stdout.write( 'Case #' + str(k+1) + ': ' )

  print( result )

#len 1 -> (0,1)
#len x -> (1,0)

#len 1 -> (0,2)
#len 2 -> (0,1)
#len x -> (2,0)


