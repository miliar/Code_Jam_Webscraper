class Output:
    @staticmethod
    def log(result):
        try:
            Output.file==None
        except:
            Output.file=open('solution.txt','w')
            Output.index=0
        Output.index+=1
        result=' '.join([str(i) for i in result])
        result='Case #'+str(Output.index)+': '+result
        print(result)
        Output.file.write(result+'\n')