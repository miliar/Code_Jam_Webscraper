class shortest():

    def __init__(self, C, F, X):
        self.C = C
        self.F = F
        self.X = X
        self.n_farm = 0        

    def speed(self, n:int):
        return (2 + n * self.F)

    def t_farm_sum(self, n:int):
        t = 0
        for i in range(n):
            t += self.t_farm_current(i)
        return t

    def t_farm_current(self, i:int):
        return self.C/(2 + i * self.F)

    def t_click(self, n):
        return self.X/self.speed(n)

    def t_total(self, n:int):
        t = self.t_farm_sum(n) + self.t_click(n)
        return t
        
    def find_n(self):
        while True:
            if self.t_total(self.n_farm) > self.t_total(self.n_farm+1):
                if self.t_total(self.n_farm + 2) >= self.t_total(self.n_farm+1):
                    return (self.n_farm + 1)
                else:
                    self.n_farm += 1               
            else:
                    return self.n_farm

    def find_shortest_time(self):
        n = self.find_n()
        return self.t_total(n)


def cookie_clicker():
    infile = open('input.txt', 'r')
    content = infile.read()
    infile.close()
    content_list = content.split()

    counter = 0
    T = int(content_list[0])
    counter += 1

    outfile = open('output.txt', 'w')

    for i in range(T):
        C = float(content_list[counter])
        counter += 1

        F = float(content_list[counter])
        counter += 1

        X = float(content_list[counter])
        counter += 1

    
        t = shortest(C,F,X).find_shortest_time()
        t_str = str('{:.7f}'.format(t))

        s = 'Case #{0}: {1}'.format(i+1, t_str)
        print(s)


        
    outfile.close()    

if __name__ == '__main__':
    cookie_clicker()
