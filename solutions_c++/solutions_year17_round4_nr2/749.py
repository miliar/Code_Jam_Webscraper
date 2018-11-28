#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>

using namespace std;

#ifdef __linux__
    #define I64d "%lld"
#else
    #define I64d "%I64d"
#endif

typedef long long int int64;

int check(vector<int> &cp, int level) {
    int s = 0;
    int res = 0;
    for (int i = 0; i < int(cp.size()); i++) {
        if (cp[i] <= level) {
            s += cp[i];
            continue;
        }
        if (cp[i] - level > i * level) {
            return -1;
        }
        else {
            res += cp[i] - level;
        }
        s += cp[i];
    }
    return res;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; test++) {
        int N, C, M;
        scanf("%d %d %d", &N, &C, &M);
        //vector<pair<int, int> > v;
        vector<int> cb(C, 0);
        vector<int> cp(N, 0);
        int mx = 0;
        for (int i = 0; i < M; i++) {
            int p, b;
            scanf("%d %d", &p, &b);
            p--; b--;
            //v.push_back(make_pair(p, b));
            cp[p] += 1;
            cb[b] += 1;
            mx = max(mx, cb[b]);
        }
        int l = mx - 1;
        int r = 1000;
        while (r - l > 1) {
            int m = (l + r) / 2;
            if (check(cp, m) != -1) {
                r = m;
            }
            else {
                l = m;
            }
        }
        int v = check(cp, r);
        printf("Case #%d: %d %d\n", test + 1, r, v);
    }
    return 0;
}
