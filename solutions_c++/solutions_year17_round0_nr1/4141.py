//
//  main.cpp
//  test
//
//  Created by Lodour on 17/3/18.
//  Copyright © 2017年 Lodour. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <iomanip>
#include <functional>
#include <cstdlib>
#include <climits>
#include <cctype>
using namespace std;
#define REP(i,x) for(int i = 0; i < (x); i++)
#define DEP(i,x) for(int i = (x) - 1; i >= 0; i--)
#define FOR(i,x) for(__typeof(x.begin())i=x.begin(); i!=x.end(); i++)
#define CLR(a,x) memset(a, x, sizeof(a))
#define MO(a,b) (((a)%(b)+(b))%(b))
#define ALL(x) (x).begin(), (x).end()
#define SZ(v) ((int)v.size())
#define UNIQUE(v) sort(ALL(v)); v.erase(unique(ALL(v)), v.end())
#define out(x) cout << #x << ": " << x << endl;
#define fastcin ios_base::sync_with_stdio(0);cin.tie(0);
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> PII;
typedef vector<int> VI;
#define INF 0x3f3f3f3f
#define MOD 1000000007
#define EPS 1e-8
#define MP(x,y) make_pair(x,y)
#define MT(x,y...) make_tuple(x,y) // c++0x only
#define PB(x) push_back(x)
#define IT iterator
#define X first
#define Y second

int solve(string& s, int k) {
    int res = 0;
    for (int i = 0; i < (int)s.size(); i++) {
        if (s[i] == '+') continue;
        if (i + k > s.size()) return -1;
        for (int j = i; j < i + k; j++)
            s[j] = (s[j] == '+') ? '-' : '+';
        res++;
    }
    return res;
}

int main(int argc, const char * argv[]) {
    freopen("/Users/Lodour/Downloads/A-large.in", "r", stdin);
    freopen("/Users/Lodour/Downloads/A-large.out", "w", stdout);
    int t, cnt = 0;
    cin >> t;
    while (t--) {
        string s;
        int k;
        cin >> s >> k;
        int ans = solve(s, k);
        if (ans == -1)
            printf("Case #%d: IMPOSSIBLE\n", ++cnt);
        else
            printf("Case #%d: %d\n", ++cnt, ans);
    }
    return 0;
}
