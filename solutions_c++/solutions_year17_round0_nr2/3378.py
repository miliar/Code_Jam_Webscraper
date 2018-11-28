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

int nto[maxx];
int a, b, k;

int main() {
    ios_base::sync_with_stdio(0);
    freopen("b_small.inp", "r", stdin);
    freopen("b_small.out", "w", stdout);
    
    int test;
    cin >> test;

    FOR(t, 1, test) {
        cout << "Case #" << t << ": ";

        long long n;
        cin >> n;

        int a[20], k = 0;
        long long x = n, res = 0;
        while (x != 0) a[++k] = x % 10, x /= 10;

        bool flag = true;
        DOW(i, k, 2) if (a[i] >= a[i-1]) {
            res = res * 10 + a[i] - 1;
            DOW(j, i-1, 1) res = res * 10 + 9;
            flag = false;
            break;
        } else {
            res = res * 10 + a[i];
        }

        bool flag2 = true;
        DOW(i, k, 2) if (a[i] > a[i-1]) flag2 = false;

        if (flag || flag2) cout << n << endl;
        else cout << res << endl;
    }

    return 0;
}