//
//  a.cpp
//  CodeJam17
//
//  Created by Ahmed Mohammed on 4/8/17.
//  Copyright © 2017 Akhmed. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <stdlib.h>
#include <fstream>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>

using namespace std;


int main(int argc, const char * argv[])
{
    if (argc < 3) { printf("Usage: %s <input file> <output file>\n", argv[0]); exit(1);}
    
    ifstream fin(argv[1], ios::in|ios::ate);
    if (!fin.is_open()) { printf("Unable to open input file\n"); exit(1);}
    fin.seekg(0);
    
    ofstream fout(argv[2], ios::out|ios::ate);
    if (!fout.is_open()) { printf("Unable to open output file\n"); exit(1);}
    fout.seekp(0);
    
    fout.precision(7);
    fout.setf(ios::fixed);
    
    
    // solve cases
    uint64_t testcase_count;
    fin >> testcase_count;
    for (uint64_t tcase = 0; tcase < testcase_count; tcase++)
    {
        fout << "Case #" << (tcase + 1) << ": ";
        
        string s; int k; fin >> s >> k;
        
        int ans = 0;
        for (int i = 0; i <= (s.length() - k); i++)
        {
            if ('+' != s[i])
            {
                ans++;
                for (int j = i; j < (i+k); j++)
                    s[j] = ('+' == s[j]) ? '-' : '+';
            }
        }
        
        bool fail = false;
        for (int i = (int)(s.length() - k + 1); i < s.length(); i++)
        {
            if ('+' != s[i])
            {
                fail = true;
                break;
            }
        }
        
        if (fail) fout << "IMPOSSIBLE";
        else fout << ans;
        
        fout << '\n';
    }
    
    
    fin.close();
    fout.close();
    
    return 0;
}
