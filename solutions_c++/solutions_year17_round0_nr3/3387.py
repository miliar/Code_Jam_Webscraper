//
//  main.cpp
//  CPPTest
//
//  Created by Roi Berlin on 3/11/17.
//  Copyright © 2017 uMake. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <set>
#include <map>
#include <vector>
using namespace std;

long getMaxStall(map<long, long>& stalls)
{
    long maxStall = 0;
    
    for ( const auto &myPair : stalls ) {
        maxStall = max(maxStall, myPair.first);
    }
    
    return maxStall;
}

void removeValue(map<long, long>& stalls, long value)
{
    if (stalls[value] == 1)
    {
        stalls.erase(value);
    }
    else
    {
        stalls[value] -= 1;
    }
}

void addValue(map<long, long>& stalls, long value)
{
    if (stalls.find(value) == stalls.end())
    {
        stalls[value] = 1;
    }
    else
    {
        stalls[value] += 1;
    }
}

void step(map<long, long>& stalls)
{
    long maxStall = getMaxStall(stalls);
    
    removeValue(stalls, maxStall);
    
    if (maxStall % 2 == 1)
    {
        addValue(stalls, (maxStall - 1) /2);
        addValue(stalls, (maxStall - 1) /2);
    }
    else
    {
        addValue(stalls, (maxStall / 2));
        addValue(stalls, (maxStall / 2) - 1);
    }
}

void outputLastStep(map<long, long>& stalls, int iteration)
{
    long maxStall = getMaxStall(stalls);
    
    if (maxStall % 2 == 1)
    {
        cout << "Case #" << iteration << ": " << (maxStall - 1) / 2 << " " << (maxStall - 1) / 2 << endl;
    }
    else
    {
        cout << "Case #" << iteration << ": " << (maxStall / 2) << " " << (maxStall / 2) - 1 << endl;
    }
}


int main(int argc, const char * argv[]) {
    // insert code here...
    FILE *fin = freopen("C-small-2-attempt0.in", "r", stdin);
    
    int T = 0;
    long N = 0;
    long K = 0;
    
    map<long, long> stalls;
    
    
    cin >> T;
    
    for (int iteration = 1 ; iteration <= T ; ++iteration)
    {
        cin >> N >> K;
        
        stalls.clear();
        
        stalls[N] = 1;
        
        while (K > 1)
        {
            step(stalls);
            --K;
        }
        
        outputLastStep(stalls, iteration);
    }
    
    return 0;
}
