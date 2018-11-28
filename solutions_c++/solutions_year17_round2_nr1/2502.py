#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <queue>
#define fi first
#define se second
using namespace std;
typedef long long llint;

const int N = 1;

int main() {
    int t;
//    freopen("/Users/Clair/Desktop/A-small-attempt0.in", "r", stdin);
//    freopen("/Users/Clair/Desktop/out-1-sm.txt", "w+", stdout);
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        int n, ed;
        cin >> ed >> n;
        double max_t = 0;
        for (int i = 0; i < n; i++) {
            int pos, sp;
            cin >> pos >> sp;
            int dis = ed - pos;
            max_t = max(max_t, (double)dis / sp);
        }
        printf("Case #%d: %.6lf\n", tt, ed/max_t);
    }
}
