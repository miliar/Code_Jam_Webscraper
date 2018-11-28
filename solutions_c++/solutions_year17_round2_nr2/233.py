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
#define maxn 30

int a[500];
int n;
map<char, char> mm;

string to_str(char c) {
    string s = "";
    s += c;
    return s;
}

pair<bool, string> check() {
    mm['R'] = 'G';
    mm['B'] = 'O';
    mm['Y'] = 'V';

    if (a['R'] < 0 || a['B'] < 0 || a['Y'] < 0) return make_pair(false, "");

    string str = "RBY";
    FOR(i, 0, str.length() - 1) {
        if (a[str[i]] + a[mm[str[i]]] * 2 == n) {
            if (a[str[i]] == 0) {
                string res = "";
                FOR(j, 1, a[mm[str[i]]]) res += str[i], res += mm[str[i]];
                return (make_pair(true, res));
            } else {
                return make_pair(false, "");
            }
        }
    }

    FOR(i, 0, str.length() - 1) {
        if (a[str[i]] == 0 && a[mm[str[i]]] != 0 && n != a[mm[str[i]]] * 2) {
            return make_pair(false, "");
        }
    }

    string res = "";

    char id[3];
    id[0] = 'R', id[1] = 'B', id[2] = 'Y';
    FOR(i, 0, 2) FOR(j, i+1, 2) if (a[id[i]] < a[id[j]]) swap(id[i], id[j]);

    FOR(i, 1, a[id[0]]) res += id[0];
    FOR(i, 0, a[id[1]] - 1) {
        res = res.insert(i*2, to_str(id[1]));
    }
    int k = res.length();
    DOW(i, k-1, k - a[id[2]]) {
        res = res.insert(i, to_str(id[2]));
    }

    FOR(i, 1, (int)res.length() - 1)
        if (res[i] == res[i-1]) return make_pair(false, res);
    if (res.length() >= 2 && res[0] == res[res.length() - 1]) 
        return make_pair(false, res);

    string res2 = "";
    FOR(i, 0, (int)res.length() - 1) {
        res2 += res[i];
        if (res[i] == 'B' && a['O'] > 0) {
            FOR(j, 1, a['O']) res2 += "OB";
            a['O'] = 0;
        } else if (res[i] == 'R' && a['G'] > 0) {
            FOR(j, 1, a['G']) res2 += "GR";
            a['G'] = 0;
        } else if (res[i] == 'Y' && a['V'] > 0) {
            FOR(j, 1, a['V']) res2 += "VY";
            a['V'] = 0;
        }
    }
    return make_pair(true, res2);
}

int main() {
    ios_base::sync_with_stdio(0);
    freopen("b_large.inp", "r", stdin);
    freopen("b_large.out", "w", stdout);
    
    int test;
    cin >> test;

    FOR(t, 1, test) {
        cout << "Case #" << t << ": ";

        cin >> n >> a['R'] >> a['O'] >> a['Y'] >> a['G'] >> a['B'] >> a['V'];

        a['R'] -= a['G'];
        a['B'] -= a['O'];
        a['Y'] -= a['V'];
        pair<bool, string> res = check();
        if (res.first) 
            cout << res.second << endl;
        else 
            cout << "IMPOSSIBLE" << endl;
    }

    return 0;
}