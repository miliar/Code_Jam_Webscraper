// A C program to implement Ukkonen's Suffix Tree Construction
// Here we build generalized suffix tree for two strings
// And then we find longest common substring of the two input strings
#include <stdio.h>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <vector>
#include <cmath>
using namespace std;

typedef long long ll;
#define MAXN 2005

ll n, m, t;

ll solve(ll ind){
    if (ind == 1){
        return n;
    }
    auto parind = ind/2;
    ll par = solve(ind/2);
    ll res = par/2;
    if (ind % 2 && (par % 2 == 0)){
        res--;
    }
    return res;
}


int main()
{
    cin >> t;
    for (int cse = 1; cse <= t; cse++){
        cin >> n >> m;
        ll res = -1;
        ll cnt = 0;
        vector<ll> v;
        map<ll, ll> mp;
        v.push_back(n);
        mp[n] = 1;
        ll ind = 0;
        while (ind < v.size()){
            auto next = v[ind];
            if (mp[next] + cnt >= m){
                res = next;
                break;
            }
            cnt += mp[next];
            if (mp.count(next/2) == 0){
                v.push_back(next/2);
            }
            mp[next/2] += mp[next];
            if (mp.count((next-1)/2) == 0){
                v.push_back((next-1)/2);
            }
            mp[(next-1)/2] += mp[next];
            ind++;
        }
        cout << "Case #" << cse << ": " << res/2 << " " << (res - 1)/2 << endl;
    }
    return 0;
}

