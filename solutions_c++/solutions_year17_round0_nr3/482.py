//
//  c.cpp
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

typedef unsigned long long ull;

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
        
        ull n, k; fin >> n >> k;
        
        ull p = k;
        for (int i = 0; p & ~(1ULL << i); i++) p &= ~(1ULL << i);
        p--;
        
        k -= p;
        ull r = (n - p) % (p + 1);
        ull s = ((n - p) / (p + 1)) + (k > r ? 0 : 1);
        
        fout << (s >> 1) << ' ' << ((s-1) - (s >> 1));
        
        fout << '\n';
    }
    
    
    fin.close();
    fout.close();
    
    return 0;
}