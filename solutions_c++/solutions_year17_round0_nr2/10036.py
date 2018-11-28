//
//  main.cpp
//  TidyNumbers
//
//  Created by Anirudh Mendiratta on 4/7/17.
//  Copyright © 2017 anirudh. All rights reserved.
//

#include <iostream>
#include <string>
#include <ctime>
#include <vector>

typedef unsigned long long uint64;

using namespace std;

bool isTidy(string number)
{
    if(number.size()==1)
    {
        return true;
    }
    for(size_t i=1; i<number.size(); i++)
    {
        if(number[i] < number[i-1])
        {
            return false;
        }
    }
    return true;
}

uint64 largestTidyNumberLessThan(uint64 number)
{
    uint64 answer = 1;
    for(uint64 i=number; i>1; i--)
    {
        if(isTidy(to_string(i)))
        {
            return i;
        }
    }
    return answer;
}

int main(int argc, const char * argv[]) {
    
    size_t numTestCases;
    cin >> numTestCases;
    vector<uint64> allTidyNums(numTestCases);
    
    for(size_t i=0; i<numTestCases; i++)
    {
        uint64 currentNumber;
        cin >> currentNumber;
        allTidyNums[i] = largestTidyNumberLessThan(currentNumber);
    }
    
    cout << endl << "End of input " << endl << endl;
    
    cout << "Begin output " << endl << endl;
    
    for(size_t i=0; i<numTestCases; i++)
    {
        cout << "Case #" << i+1 << ": " << allTidyNums[i] << endl;
    }

    return 0;
}
