//
//  main.cpp
//  Oversized Pancake Flipper
//
//  Created by Alexandre Duong on 08/04/2017.
//  Copyright © 2017 Alexandre Duong. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iterator>
#include <vector>
#include <list>
#include <cmath>

int main(int argc, const char * argv[]) {
    std::ifstream aStream(argv[1]);
    std::ofstream aOutput(argv[2]);
    if(aStream.is_open() && aOutput.is_open())
    {
        uint32_t T;
        aStream >> T;
        std::cout << T << std::endl;
        
        for(uint32_t i=1; i<=T; ++i)
        {
            std::cout << "###########################" << std::endl;
            std::string aPancakes;
            uint32_t S;
            aStream >> aPancakes >> S;
            std::cout << aPancakes << " "<< S << std::endl;
            aOutput << "Case #" << i << ": ";
            uint32_t aCount = 0;
            bool aImpossible = false;
            for(uint32_t j=0; j<aPancakes.size(); ++j)
            {
                std::cout << aPancakes << std::endl;
                if(aPancakes[j] == '-')
                {
                    if(j+S-1 >= aPancakes.size())
                    {
                        aOutput << "IMPOSSIBLE" << std::endl;
                        aImpossible = true;
                        break;
                    }
                    else
                    {
                        for(uint32_t k=j; k<j+S; ++k)
                        {
                            if(aPancakes[k] == '-')
                                aPancakes[k] = '+';
                            else
                                aPancakes[k] = '-';
                        }
                        ++ aCount;
                    }
                }
            }
            if(aImpossible == false)
            {
                aOutput << aCount << std::endl;
            }
            std::cout << "###########################" << std::endl;
        }
    }
}
