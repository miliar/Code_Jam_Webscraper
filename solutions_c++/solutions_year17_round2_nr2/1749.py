//
//  1b_b.cpp
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
    fout.precision(7);
    fout.setf(ios::fixed);
    
    // solve cases
    uint64_t testcase_count;
    fin >> testcase_count;
    for (uint64_t tcase = 0; tcase < testcase_count; tcase++)
    {
        fout << "Case #" << (tcase + 1) << ": ";
        
        int N, R, O, Y, G, B, V;
        fin >> N >> R >> O >> Y >> G >> B >> V;
        
        // small input
        {
            int sum = Y + B + R;
            int max = ((Y > B) ? Y : B); max = (max > R) ? max : R;
            
            if ((sum > 1) && (sum < (max + max))) fout << "IMPOSSIBLE";
            else
            {
                string ans;
                vector<pair<int, char>> n { {Y, 'Y'}, {B, 'B'}, {R, 'R'} };
                sort(n.begin(), n.end(), [](pair<int, char> const& l, pair<int, char> const&  r) -> bool { return r.first < l.first; });
                
                while (n[0].first)
                {
                    int k = (n[0].first + n[1].first - n[2].first) >> 1;
                    if (k > n[1].first) k = n[1].first;
                    if (0 == k) break;
                    
                    n[0].first -= k;
                    n[1].first -= k;
                    
                    if ((0 == ans.length()) || (ans[ans.length()-2] == n[0].second))
                    {
                        for (int i = 0; i < k; i++)
                        {
                            ans.push_back(n[0].second);
                            ans.push_back(n[1].second);
                        }
                    }
                    else
                    {
                        for (int i = 0; i < k; i++)
                        {
                            ans.push_back(n[1].second);
                            ans.push_back(n[0].second);
                        }
                    }
                    
                    sort(n.begin(), n.end(), [](pair<int, char> const& l, pair<int, char> const&  r) -> bool { return r.first < l.first; });
                }
                
                if (n[2].first && (ans.front() == n[2].second)) ans.push_back(n[2].second);
                if (n[1].first && (ans.front() == n[1].second)) ans.push_back(n[1].second);
                if (n[0].first) ans.push_back(n[0].second);
                if (n[1].first && (ans.front() != n[1].second)) ans.push_back(n[1].second);
                if (n[2].first && (ans.front() != n[2].second)) ans.push_back(n[2].second);
                
                fout << ans;
            }
        }
        
        fout << '\n';
    }
    
    fin.close();
    fout.close();
    
    return 0;
}