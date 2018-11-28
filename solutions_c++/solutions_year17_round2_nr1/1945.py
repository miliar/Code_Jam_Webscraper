//
//  1b_a.cpp
//  CodeJam17
//
//  Created by Ahmed Mohammed on 4/22/17.
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
    ifstream fin(argv[1], ios::in); if (!fin) { printf("Unable to open input file\n"); exit(1);}
    ofstream fout(argv[2], ios::out|ios::trunc); if (!fout) { printf("Unable to open output file\n"); exit(1);}
    fout.precision(8);
    fout.setf(ios::fixed);

    // solve cases
    uint64_t testcase_count;
    fin >> testcase_count;
    for (uint64_t tcase = 0; tcase < testcase_count; tcase++)
    {
        fout << "Case #" << (tcase + 1) << ": ";
        
        int d, n; fin >> d >> n;
        vector<pair<int, int>> ks(n); for (int i = 0; i < n; i++) { fin >> ks[i].first >> ks[i].second; }
        
        double t = 0.0;
        for (int i = 0; i < n; i++)
        {
            double tt = double(d - ks[i].first) / ks[i].second;
            if (tt > t) t = tt;
        }
        
        fout << double(d) / t;
    
        fout << '\n';
    }

    fin.close();
    fout.close();

    return 0;
}