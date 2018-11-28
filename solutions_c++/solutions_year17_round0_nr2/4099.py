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
#include <sstream>
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

string solve(string s) {
    int i = 0;
    // find first un-tidy position
    while (i < (int)s.size() - 1 && s[i] <= s[i + 1])
        i++;
    if (i == (int)s.size() - 1)
        return s;
    // now s[i] > s[i + 1]
    for (int j = i + 1; j < (int)s.size(); j++)
        s[j] = '9';
    s[i]--;
    while (i > 0 && s[i] < s[i - 1])
        s[--i]--;
//    if (i == 0)
        while (s[++i] != '9')
            s[i] = '9';
    // remove prefix 0
    int p = 0;
    while (s[p] == '0') p++;
    s = s.substr(p);
    return s;
}

bool chk(ll s) {
    while (s) {
        if (s % 10 < s % 100 / 10)
            return 0;
        s /= 10;
    }
    return 1;
}

string solve2(string s) {
    stringstream ss(s);
    ll a;
    ss >> a;
    while (!chk(a)) a--;
    stringstream ss2;
    string res;
    ss2 << a;
    ss2 >> res;
    return res;
}

int main(int argc, const char * argv[]) {
    freopen("/Users/Lodour/Downloads/B-large.in", "r", stdin);
    freopen("/Users/Lodour/Downloads/B-large.out", "w", stdout);
//    for (ll a = 1000000; a < 2000000; a++) {
//        string s;
//        stringstream ss;
//        ss << a;
//        ss >> s;
//        if (solve(s) != solve2(s)) {
//            cout << a << " " << solve(s) << " " << solve2(s) << endl;
//            break;
//        }
//    }
//    cout << "Y" << endl;
    int t, cnt = 0;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        string ans = solve(s);
        printf("Case #%d: %s\n", ++cnt, ans.c_str());
    }
    return 0;
}
