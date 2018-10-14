'''
Created on May 7, 2011

@author: kivson
'''

class Cast(object):
    '''
    classdocs
    '''


    def __init__(self, fusoes, excluidos):
        '''
        Constructor
        '''
        self.flags = []
        self.fusote_to_dict(fusoes)
        self.exc_to_dict(excluidos)
        
    
    def fusote_to_dict(self,fusoes):
        self.fusoes = {}
        for fusao in fusoes:
            self.fusoes[fusao[0],fusao[1]] = fusao[2]
            self.fusoes[fusao[1],fusao[0]] = fusao[2]
    
    def exc_to_dict(self,excluidos):
        self.exc = {}
        for ex in excluidos:
            self.exc[ex[1]] = ex[0]
            self.exc[ex[0]] = ex[1]
        
        
    def run(self, lista):
        self.resp = []
        for elem in lista:
            self.processa(elem)
    
    
    def processa(self, elem):
        ocorreFusao, letraFusao = self.fusao(elem)
        
        if ocorreFusao:
            self.resp.pop()
            elem = letraFusao  
              
        ocorreExc = self.exclui(elem, True)
        
        if not (ocorreExc):
            self.resp.append(elem)
            
    def exclui(self,elem, all = False):
        par = self.exc.get(elem, False)
        if par:
            pos = len(self.resp)-1
            while pos >= 0:
                if self.resp[pos] == par:
                    if all:
                        self.resp = []
                        return True
                    self.resp = self.resp[:pos]
                    return True
                pos -= 1
        return False
    
    def fusao(self,elem):
        try:
            elemento = self.fusoes.get((elem, self.resp[-1]), False)
            if elemento:
                return True, elemento
        except:
            pass
                

        return False, False     

if __name__ == '__main__':
    saida = file("Magicka.out",'w')
    entrada = file('Magicka.in','r')
    qtdCasos = int(entrada.readline())
    for ii in xrange(qtdCasos):
        elementos = entrada.readline().split()
        print elementos,
        fusoes = []
        exc = []
        
        for i in xrange(int (elementos.pop(0))):
            fusoes.append(elementos.pop(0))
        
        for i in xrange(int(elementos.pop(0))):
            exc.append(elementos.pop(0))
        
        #retira a quantidade de elemetnos da lista de ataques, que eh desnecessaria
        elementos.pop(0)
        
        
        c = Cast(fusoes, exc)
        c.run(elementos[0])
        print c.resp
        saida.write("Case #%d: " % (ii+1, ) + '[' +', '.join(c.resp) + ']\n') 
    
    entrada.close()
    saida.close()