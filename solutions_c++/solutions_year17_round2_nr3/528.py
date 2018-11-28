//
//  main.cpp
//  gg2-C
//
//  Created by Ran Wang on 4/22/17.
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
#include <iomanip>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<(n);i++)
#define F1(i,n) for(int i=1;i<=(n);i++)
#define F2(i,a,b) for(int i=(a);i<=(b);i++)

const long long maxll = (long long)INT_MAX * INT_MAX;
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

vector<vector<double>> floyd(vector<vector<long long>>& D, vector<int>& E, vector<double>& S)
{
    int N = D.size();
    
    for(int i = 0; i < N; i++)
    {
        D[i][i] = 0;
    }
    
    F0(k, N)
    F0(i, N)
    F0(j, N)
    if(D[i][k] < maxll && D[k][j] < maxll && D[i][j] > D[i][k] + D[k][j])
        D[i][j] = D[i][k] + D[k][j];
    
    vector<vector<double>> t(N, vector<double>(N, 1e12));
    for(int i = 0; i < N; i++)
        for(int j = 0; j < N; j++)
        {
            if(i==j)
            {
                t[i][j] = 0;
                continue;
            }
            
            if(E[i] < D[i][j])continue;
            
            t[i][j] = D[i][j] / S[i];
        }
    
    F0(k, N)
    F0(i, N)
    F0(j, N)
    if(t[i][k] < 1e11 && t[k][j] < 1e11 && t[i][j] > t[i][k] + t[k][j])
        t[i][j] = t[i][k] + t[k][j];
    
    return t;
}


int main() {
    int T;
    cin >> T;
    for(int caset = 1; caset <= T; caset++)
    {
        int N, Q;
        cin >> N >> Q;
        
        vector<int> E;
        vector<double> S;
        vector<vector<long long>> D(N, vector<long long>(N, 0));
        
        while(N--)
        {
            int a, b;
            cin >> a >> b;
            E.push_back(a), S.push_back(b);
        }
        
        for(auto & a : D)
            for(auto & b : a)
            {
                cin >> b;
                if(b == -1)b = maxll;
            }
        
        
        vector<double> res;
        
        
        vector<vector<double>> t = floyd(D, E, S);
        while(Q--)
        {
            int a, b;
            cin >> a >> b;
            res.push_back(t[a-1][b-1]);
        }
        cout << "Case #" << caset << ":";
        
        for(auto & a : res)cout << ' ' << fixed << a;
        cout << endl;
    }
}
