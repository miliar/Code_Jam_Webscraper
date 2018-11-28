//
//  d.cpp
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
#include <set>
#include <algorithm>
#include <cmath>
#include <cassert>


//#define TEST


using namespace std;


static inline char pairToChar(pair<bool /* + */, bool /* x */> p)
{
    char c = '.';
    if (p.first) c = p.second ? 'o' : '+';
    else if (p.second) c = 'x';
    return c;
}

static inline pair<bool /* + */, bool /* x */> charToPair(char c)
{
    pair<bool, bool> p;
    p.first = ('+' == c) || ('o' == c);
    p.second = ('x' == c) || ('o' == c);
    return p;
}

void printGrid(int n, pair<bool, bool> const grid[100][100])
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++) cout << pairToChar(grid[i][j]) << ' ';
        cout << '\n';
    }
}


static vector<pair<int, int>>* project(int n, pair<int, int> p)
{
    static vector<pair<int, int>> v(8);
    
    int wi = 0;
#define push(i, j)   v[wi++] = {(i), (j)}

    // r = 0
    push(0, p.second + p.first);
    if (0 != p.first) push(0, p.second - p.first);
    
    // r = n-1
    push(n-1, p.second + (n-1 - p.first));
    if ((n-1) != p.first) push(n-1, p.second - (n-1 - p.first));
    
    // c = 0
    push(p.first + p.second, 0);
    if (0 != p.second) push(p.first - p.second, 0);
    
    // c = n-1
    push(p.first + (n-1 - p.second), n-1);
    if ((n-1) != p.second) push(p.first - (n-1 - p.second), n-1);
    
#undef push

    return &v;
}


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
        
        int n, m; fin >> n >> m;
        
        pair<bool /* + */, bool /* x */> grid[100][100];
            
        for (int i = 0; i < m; i++)
        {
            char ch; fin >> ch;
            int r, c; fin >> r >> c; r--; c--;
            grid[r][c] = charToPair(ch);
        }
        
#ifdef TEST
        printGrid(n, grid);
        cout << '\n';
#endif
        
        pair<bool /* + */, bool /* x */> grid2[100][100];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                grid2[i][j] = grid[i][j];
        
        
        // maximize x
        {
            vector<int> e;
            vector<bool> s(n);
            for (int i = 0; i < n; i++)
            {
                bool found = false;
                for (int j = 0; j < n; j++)
                {
                    if (grid2[i][j].second)
                    {
                        assert(false == s[j]);
                        s[j] = true;
                        found = true;
                        break;
                    }
                }
                if (false == found) e.push_back(i);
            }
            
            for (int j = 0, ei = 0; j < n; j++)
                if (false == s[j]) { assert(false == grid2[e[ei]][j].second); grid2[e[ei++]][j].second = true; }
        }
        
        
        // maximize +
        {
            set<pair<int, int>> u;
            for (int i = 0; i < n; i++)
            {
                u.insert({0, i});
                u.insert({n-1, i});
                u.insert({i, 0});
                u.insert({i, n-1});
            }
            
            for (int i = 0; i < n; i++)
                for (int j = 0; j < n; j++)
                    if (grid2[i][j].first)
                    {
                        auto proj = project(n, {i, j});
                        for (int k = 0; k < proj->size(); k++) u.erase(proj->operator[](k));
                    }
            
            while (u.size())
            {
                auto p = *u.begin();
                assert(false == grid2[p.first][p.second].first);
                grid2[p.first][p.second].first = true;
                
                auto proj = project(n, p);
                for (int k = 0; k < proj->size(); k++) u.erase(proj->operator[](k));
            }
        }
        
        
        // generate output
        int sp = 0;
        vector<pair<pair<int, int>, char>> changes;
        {
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (grid2[i][j] != grid[i][j]) changes.push_back({{i, j}, pairToChar(grid2[i][j])});
                    if (grid2[i][j].first) sp++;
                    if (grid2[i][j].second) sp++;
                }
            }
        }
        
#ifdef TEST
        printGrid(n, grid2);
        cout << '\n';
        cout << '\n';
#endif
        
        fout << sp << ' ' << changes.size();
        for (auto c : changes)
            fout << '\n' << c.second << ' ' << (c.first.first + 1) << ' ' << (c.first.second + 1);
        
        fout << '\n';
    }
    
    
    fin.close();
    fout.close();
    
    return 0;
}