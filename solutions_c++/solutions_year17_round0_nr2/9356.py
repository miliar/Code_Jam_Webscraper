//
//  main.cpp
//  Tidy Numbers
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

bool changeTidy(uint64_t& iNumber)
{
    std::string aString = std::to_string(iNumber);
    uint32_t aTest = aString[0] - '0';
    for(size_t i=0; i<aString.size(); ++i)
    {
        if(aTest > (aString[i]-'0'))
        {
            if(i-1 == 0 && aString[i]=='0')
            {
                iNumber = (aString[0]-'0') * std::pow(10, aString.size()-1);
                iNumber = iNumber - 1;
                std::cout << iNumber << std::endl;
                return true;
            }
            aString[i-1] = aString[i];
            iNumber = std::stol(aString);
            return false;
        }
        
        aTest = aString[i] - '0';
    }
    
    return true;
}

bool isTidy(uint64_t iNumber)
{
    std::string aString = std::to_string(iNumber);
    uint32_t aTest = aString[0] - '0';
    for(size_t i=0; i<aString.size(); ++i)
    {
        if(aTest > (aString[i]-'0'))
        {
            return false;
        }
        
        aTest = aString[i] - '0';
    }
    
    return true;
}

uint64_t aLong(uint64_t N)
{
    uint64_t aResult = N;
    while(!changeTidy(aResult))
    {
        std::string aString = std::to_string(aResult);
        aString[aString.size()-1] = '9';
        size_t aSecond = std::stol(aString);
        if(aSecond < N)
            aResult = aSecond;
    }
    
    return aResult;
}

uint64_t aShort(uint64_t N)
{
    uint64_t aResult = 0;
    for(uint64_t i=N; i>0; --i)
    {
        if(isTidy(i))
        {
            aResult = i;
            break;
        }
    }
    return aResult;
}

int main(int argc, const char * argv[]) {
    std::ifstream aStream(argv[1]);
    std::ofstream aOutput(argv[2]);
    if(aStream.is_open() && aOutput.is_open())
    {
        uint64_t T;
        aStream >> T;
        std::cout << T << std::endl;
        
        for(uint64_t i=1; i<=T; ++i)
        {
            std::cout << "###########################" << std::endl;
            aOutput << "Case #" << i << ": ";
            uint64_t N;
            aStream >> N;

            uint64_t aResult = aShort(N);
            
            aOutput << aResult << std::endl;
            std::cout << "N = " << N  << "  Result = " << aResult << std::endl;
            std::cout << "###########################" << std::endl;
        }
    }
}
