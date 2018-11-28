//
//  main.cpp
//  qr
//
//  Created by Ran Wang on 4/7/17.
//  Copyright © 2017 Ran Wang. All rights reserved.
//

#include <iostream>
#include <unordered_map>
#include <map>
#include <vector>
#include <unordered_set>
#include <string>

using namespace std;

char flip(char c)
{
    return c == '-' ? '+' : '-';
}

int main(int argc, const char * argv[]) {
    long long T, N, K;
    cin >> T;
    
    for(int caset = 1; caset <= T; caset++)
    {
        cin >> N >> K;
        
        map<long long, long long> counti;
        
        counti[N] = 1;
        long long r1, r2;
        
        while(K)
        {
            auto it = counti.rbegin();
            
            
            long long key = it->first - 1;

            if(it->second <= K)
            {
                if(key % 2 == 0)
                    counti[key / 2] += it->second * 2, r1 = r2 = key / 2;
                else
                {
                    counti[key / 2] += it->second;
                    counti[key / 2 + 1] += it->second;
                    r1 = key / 2;
                    r2 = key / 2 + 1;
                }
                
                K -= it->second;
                counti.erase(it->first);
            }
            else
            {
                if(key % 2 == 0)
                    counti[key / 2] += it->second * 2, r1 = r2 = key / 2;
                else
                {
                    counti[key / 2] += it->second;
                    counti[key / 2 + 1] += it->second;
                    r1 = key / 2;
                    r2 = key / 2 + 1;
                }
                
                //counti[it->first] -= K;
                K = 0;
            }
        }
        
        if(counti.empty())counti[0] = 0;
        
        cout << "Case #" << caset << ": " << r2 << ' ' << r1 << endl;
    }
}
