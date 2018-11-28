//
//  main.cpp
//  gg1-C
//
//  Created by Ran Wang on 4/14/17.
//  Copyright © 2017 Ran Wang. All rights reserved.
//

#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<(n);i++)
#define F1(i,n) for(int i=1;i<=(n);i++)
#define F2(i,a,b) for(int i=(a);i<=(b);i++)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

bool all_q1(int a, int c, int d, vector<string>& res)
{
    F2(j, c, d)
    if(res[a][j] != '?')return false;
    return true;
}

bool all_q2(int c, int a, int b, vector<string>& res)
{
    F2(i, a, b)
    if(res[i][c] != '?')return false;
    return true;
}

void fill(int a, int b, int c, int d, vector<string>& res, char ch)
{
    while(a > 0 && all_q1(a-1,c,d,res))a--;
    while(b + 1 < res.size() && all_q1(b+1,c,d,res))b++;
    while(c > 0 && all_q2(c-1,a,b,res))c--;
    while(d + 1 < res[0].size() && all_q2(d+1,a,b,res))d++;
    
    F2(i, a, b)
    F2(j, c, d)
    res[i][j] = ch;
}

int main() {
    int T;
    cin >> T;
    for(int caset = 1; caset <= T; caset++)
    {
        unordered_map<char, pii> m1_, m2_;
        int R, C;
        cin >> R >> C;
        vector<string> data;
        while(R--)
        {
            string tmp;
            cin >> tmp;
            data.push_back(tmp);
        }
        
        for(int i = 0; i < data.size(); i++)
            for(int j = 0; j < data[0].size(); j++)
            {
                char c = data[i][j];
                if(data[i][j] == '?')continue;
                if(m1_.count(data[i][j]))
                {
                    m1_[c] = {min(m1_[c].first, i), max(m1_[c].second, i)};
                    m2_[c] = {min(m2_[c].first, j), max(m1_[c].second, j)};
                    
                }
                else
                {
                    m1_[c] = {i, i};
                    m2_[c] = {j, j};
                }
            }
        
        for(auto & a : m1_)
        {
            char c = a.first;
            fill(a.second.first, a.second.second, m2_.at(c).first, m2_.at(c).second, data, c);
            
        }
        cout << "Case #" << caset << ": " << endl;
        
        for(auto & a : data)cout << a << endl;
    }
}
