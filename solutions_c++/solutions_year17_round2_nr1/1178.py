#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <bitset>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <cstring>
#include <queue>
#include <memory.h>
#include <cmath>

using namespace std;

#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define FOR0(i,n) for( i = 0 ; i < n ; ++i )
#define FOR1(i,n) for( i = 1 ; i <= n ; ++i )
#define FI first
#define SE second

typedef long long LL;

int T, _T;


struct h {
    int k, s;
    long double news;
    h(){}
    h(int k, int s) : k(k), s(s) {}
};


int n, d;
h hr[1001];
bool operator < (h h1, h h2) {
    return h1.k < h2.k;
}

int main() {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios::sync_with_stdio(false);
    cin >> T;
    for (_T = 1; _T <= T; ++_T) {
        cout << "Case #" << _T << ": ";
        cin >> d >> n;
        int i;
        FOR0(i, n) {
            cin >> hr[i].k >> hr[i].s;
        }
        sort(hr, hr + n);
        int bad[1000];
        FOR0(i, n)
            bad[i] = i;
        FOR0(i, n) {
            if (i == 0)
                continue;
            if (hr[i].k == hr[i-1].k) {
                hr[bad[i - 1]].s = min(hr[bad[i - 1]].s, hr[i].s);
                bad[i] = bad[i - 1];
            }
        }
        vector<h> newh;
        FOR0(i, n) {
            if (bad[i] == i)
                newh.push_back(hr[i]);
        }
        n = (int)newh.size();
        int stopped[1000];
        FOR0(i, n) {
            stopped[i] = i;
            newh[i].news = newh[i].s;
        }
        for(i = n-2; i >= 0; --i) {
            long double tr = (d - newh[i+1].k) / (newh[i+1].news);
            long double tr2 = (d - newh[i].k) / (newh[i].news);
            if (tr2 < tr) {
                newh[i].news = (d - newh[i].k) / tr;
            }
        }
        long double t = (d - newh[0].k) / newh[0].news;
        cout << setprecision(6) << fixed << d / t << endl;
    }
}