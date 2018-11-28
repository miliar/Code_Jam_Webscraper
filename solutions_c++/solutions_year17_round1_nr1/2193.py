//
//  a.cpp
//  CodeJam17
//
//  Created by Ahmed Mohammed on 4/15/17.
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
        
        int r, c; fin >> r >> c;
        vector<string> b(r);
        for (int i = 0; i < r; i++) fin >> b[i];
        
        int fr = r;
        for (int i = 0; i < r; i++)
        {
            int fc = c;
            for (int j = 0; j < c; j++)
            {
                if ('?' == b[i][j])
                {
                    if (fc != c) b[i][j] = b[i][j-1];
                }
                else if (fc == c) fc = j;
            }
            
            if (fc == c)
            {
                if (fr != r)
                {
                    for (int j = 0; j < c; j++) b[i][j] = b[i-1][j];
                }
            }
            else
            {
                if (fr == r) fr = i;
                for (int j = 0; j < fc; j++) b[i][j] = b[i][fc];
            }
        }
        
        for (int i = 0; i < fr; i++)
            for (int j = 0; j < c; j++) b[i][j] = b[fr][j];
        
        for (int i = 0; i < r; i++) fout << '\n' << b[i];
        fout << '\n';
    }
    
    
    fin.close();
    fout.close();
    
    return 0;
}
