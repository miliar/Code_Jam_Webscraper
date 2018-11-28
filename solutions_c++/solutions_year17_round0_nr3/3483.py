//#include <bits/stdc++.h>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
using namespace std;
#define FOR(i, a, b) for(int i = a; i <= b; i ++)
#define DOW(i, a, b) for(int i = a; i >= b; i --)
#define RESET(c, val) memset(c, val, sizeof(c))
#define oo 1e9
#define eps 1e-9
#define base 1000000007
#define maxn 100005
#define maxx 10000000

map<long long, long long> mm;
set<long long> se;  

int main() {
    ios_base::sync_with_stdio(0);
    freopen("c_large.inp", "r", stdin);
    freopen("c_large.out", "w", stdout);
    
    int test;
    cin >> test;

    FOR(t, 1, test) {
        cout << "Case #" << t << ": ";

        long long n, k;
        cin >> n >> k;

        mm.clear();
        se.clear();

        se.insert(n);
        mm[n] = 1;

        long long res;

        while (!se.empty() && k >= 1) {
            long long last = *se.rbegin();
            se.erase(*se.rbegin());

            if (mm[last] < k) {
                mm[last/2] += mm[last];
                mm[last/2 - (last%2==0)] += mm[last];
                se.insert(last/2);
                se.insert(last/2 - (last%2==0));
                
                k -= mm[last];
            } else {
                res = last; break;
            }
        }

        cout << max(res/2, res/2 - (res%2==0)) << " " << min(res/2, res/2 - (res%2==0)) << endl;
    }

    return 0;
}