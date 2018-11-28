//
//  1c_a.cpp
//  CodeJam17
//
//  Created by Ahmed Mohammed on 4/30/17.
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

typedef long long ll;

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
        
        int n, k; fin >> n >> k;
        vector<pair<ll, ll>> rh(n); for (int i = 0; i < n; i++) { fin >> rh[i].first >> rh[i].second; }
        
        sort(rh.begin(), rh.end(), [](pair<ll, ll> const& l, pair<ll, ll> const& r) -> bool { return r.first < l.first; });
        
        ll ans = 0;
        for (int i = 0; i <= n-k; i++)
        {
            ll c = rh[i].first * rh[i].first + 2 * rh[i].first * rh[i].second;
            if (k > 1)
            {
                vector<pair<ll, ll>> rh2 = rh;
                sort(rh2.begin()+i+1, rh2.end(), [](pair<ll, ll> const& l, pair<ll, ll> const& r) -> bool
                {
                    return r.first * r.second < l.first * l.second;
                });
                for (int j = 1; j < k; j++) c += 2 * rh2[i+j].first * rh2[i+j].second;
            }
            if (c > ans) ans = c;
        }
        
        fout << M_PI * ans;
        
        fout << '\n';
    }
    
    fin.close();
    fout.close();
    
    return 0;
}