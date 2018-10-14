# Rubens Pessoa de Barros Filho from Arapiraca, Brazil

numberOfTestCases = int(raw_input())

test = 1

while test <= numberOfTestCases:
    
    productionRate = 2
    factoryCost, increaseInProduction, objective = map(float, raw_input().split())
    secs = 0
    
    while (factoryCost/productionRate) + objective/(productionRate + increaseInProduction) < objective/productionRate:
        secs += factoryCost/productionRate
        productionRate += increaseInProduction
        
    secs = secs + objective/productionRate
    
    print "Case #" + str(test) + ": %.7f" % (secs)
    test = test + 1

        
        
        
        