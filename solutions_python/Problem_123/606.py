
def main():
    fout = open("osmos.out",'w')
    with open("osmos.in",'r') as fin:
        case_numbers = int(fin.readline().strip())
        for i in range(case_numbers):
            armin,mote_num = map(int,fin.readline().split())
            motes = sorted((map(int,fin.readline().split())))
            ops = 0
            for k,mote in enumerate(motes):
                if mote < armin:
                    armin+=mote
                else:
                    counter = 0
                    carmin = armin
                    while carmin <= mote and counter < mote_num-k:
                        carmin+=carmin-1
                        counter+=1
      
              
                    if counter < mote_num - k:
                        ops+=counter
                        armin=carmin+mote
                    else:
                        ops+=1
            fout.write("Case #{}: {}\n".format(i+1,ops))
            print(i)
    fout.close()
            


if __name__=='__main__':
    main()
        
