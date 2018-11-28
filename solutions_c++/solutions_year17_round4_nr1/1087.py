//
//  main.cpp
//  gg3a
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


int main() {
    int T;
    cin >> T;
    for(int caset = 1; caset <= T; caset++)
    {
        int N, P;
        cin >> N >> P;
        vector<int> counts(P, 0);
        int sum = 0;
        while(N--)
        {
            int tmp;
            cin >> tmp;
            counts[tmp % P]++;
            sum += tmp;
        }
        
        int res = 0;
        res += counts[0];
        
        if(P == 2)
        {
            res += counts[1] / 2;
        }
        else if(P == 3)
        {
            int tmp = min(counts[1], counts[2]);
            counts[1] -= tmp;
            counts[2] -= tmp;
            res += tmp;

            tmp = max(counts[1], counts[2]);
            res += tmp / 3;
        }
        else if(P == 4)
        {
            res += counts[2] / 2;
            counts[2] = counts[2] % 2;
            int tmp = min(counts[1], counts[3]);
            res += tmp;
            counts[1] -= tmp;
            counts[3] -= tmp;
            tmp = max(counts[1], counts[3]);
            if(counts[2] == 1)
            {
                if(tmp >= 2)tmp -= 2, res++;
            }
            
            res += tmp / 4;
        }
        
        if(sum % P > 0)res++;
        cout << "Case #" << caset << ": " << res;
        cout << endl;
    }
}
