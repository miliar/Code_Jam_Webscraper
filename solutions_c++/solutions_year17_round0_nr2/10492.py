//
//  main.cpp
//  Codejam
//
//  Created by nitendra on 08/04/17.
//  Copyright © 2017 nit. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>

bool isSorted(std::string& str)
{
    short sz = str.length();
    if(sz <= 1)
        return true;
    
    for (short i=1; i<sz; ++i)
    {
        if(str[i]<str[i-1])
            return false;
    }
    return true;
}

std::string getSortedNumber(std::string& str)
{
    while(!isSorted(str))
    {
        long long num = atoll(str.c_str());
        --num;
        str = std::to_string(num);
        //std::cout<<str<<std::endl;
    }
    return str;
}

int main(int argc, const char * argv[])
{
    short T;
    std::string inp;
    std::ifstream is("B-small-attempt1.in.txt");
    std::ofstream os("out.txt");
    
    is>>T;
    int cnt =1;
    while(T--)
    {
        is>>inp;
        //std::cout<<getSortedNumber(inp)<<std::endl;;
        os<<"Case #"<<cnt<<": "<<getSortedNumber(inp)<<std::endl;
        ++cnt;
    }
    return 0;
}




