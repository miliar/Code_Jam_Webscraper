from __future__ import division

filename = "B-large.in"
out_filename = filename.split(".")[0] + ".out"


out_f = file(out_filename, "w")
f = file(filename, "r")
cases = int(f.readline())

def should_buy(coeff, produce, target, F):
        #print "coeff: " + str(coeff)
        #print "produce: " + str(produce)
        #print "target: " + str(target)
        
        if target/produce >= coeff + target/(produce + F):
                return True
        return False


for i in range(0,cases):
        args = f.readline().split(" ")
        C = float(args[0])
        F = float(args[1])
        X = float(args[2])

        farm_coef = C/F
        
        production_rate = float(2)
        t = 0
        while True:
                if should_buy(C/production_rate, production_rate, X, F):
                        t += C/production_rate
                        production_rate += F
                else:
                        t += X/production_rate
                        break
        out_f.write("Case #" + str(i+1) + ": " + str(t) + "\n")
out_f.close()


out_f.close()

