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

char fleepChar(char s)
{
    return s == '+' ? '-' : '+';
}

void fleap(string& S, int K, int startIndex)
{
    for (int index = startIndex ; index < startIndex + K ; ++index)
    {
        S[index] = fleepChar(S[index]);
    }
}

int findLastMinusIndex(string& S)
{
    for (int index = (int)S.length() ;  index >= 0 ; --index )
    {
        if (S[index] == '-')
        {
            return index;
        }
    }
    
    return -1;
}


int main(int argc, const char * argv[]) {
    // insert code here...
    FILE *fin = freopen("A-large.in", "r", stdin);
    
    int T = 0;
    string S = "";
    int K = 0;
    int lastIndex = 0;
    int counter = 0;
    
    cin >> T;
    
    for (int iteration = 1 ; iteration <= T ; ++iteration)
    {
        cin >> S >> K;
        
        lastIndex = findLastMinusIndex(S);
        
        counter = 0;
        
        while (lastIndex > K - 2)
        {
            int startIndex = lastIndex - K + 1;
            fleap(S, K, startIndex);
            ++counter;
            
            lastIndex = findLastMinusIndex(S);
        }
        
        if (lastIndex == -1)
        {
            cout << "Case #" << iteration << ": " << counter << endl;
        }
        else
        {
            cout << "Case #" << iteration << ": IMPOSSIBLE" << endl;
        }
        
        
    }
    
   
    return 0;
}
