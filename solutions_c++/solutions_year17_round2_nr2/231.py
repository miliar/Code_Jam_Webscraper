#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <algorithm>

using namespace std;

#ifdef __linux__
    #define I64d "%lld"
#else
    #define I64d "%I64d"
#endif

typedef long long int int64;

const string fuu = "IMPOSSIBLE";


string walk3(int r, int y, int b) {
    string s = "";
    vector<pair<int, char> > a = {make_pair(r, 'R'), make_pair(y, 'Y'), make_pair(b, 'B')};
    sort(a.rbegin(), a.rend());
    if (a[0].first > a[1].first + a[2].first) {
        return s;
    }
    int cnt = a[0].first;
    for (int i = 0; i < cnt; i++) {
        s += a[0].second;
        a[0].first -= 1;
        s += a[1].second;
        a[1].first -= 1;
        int cur = 1;
        while (a[1].first + a[2].first > a[0].first) {
            cur = 1 + (2 - cur);
            s += a[cur].second;
            a[cur].first -= 1;
        }
        if (a[1].first < a[2].first) {
            swap(a[1], a[2]);
        }
    }
    return s;
}


int main() {
    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; test++) {
        int n, r, o, y, g, b, v;
        scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
        printf("Case #%d: ", test + 1);
        bool fail = false;
        if (v > y || o > b || g > r)
            fail = true;
        if (v > 0 && v == y) {
            if (v + y == n) {
                for (int i = 0; i < v; i++) {
                    printf("YV");
                }
                printf("\n");
                continue;
            }
            fail = true;
        }
        if (o > 0 && o == b) {
            if (o + b == n) {
                for (int i = 0; i < o; i++) {
                    printf("BO");
                }
                printf("\n");
                continue;
            }
            fail = true;
        }
        if (g > 0 && r == g) {
            if (r + g == n) {
                for (int i = 0; i < r; i++) {
                    printf("RG");
                }
                printf("\n");
                continue;
            }
            fail = true;
        }
        if (fail) {
            printf("%s\n", fuu.c_str());
            continue;
        }
        y -= v;
        b -= o;
        r -= g;
        string ans = walk3(r, y, b);
        if (ans.size() == 0) {
            printf("%s\n", fuu.c_str());
            continue;
        }
        for (int i = 0; i < int(ans.size()); i++) {
            printf("%c", ans[i]);
            if (ans[i] == 'R' && g > 0) {
                for (int j = 0; j < g; j++) {
                    printf("GR");
                }
                g = 0;
            }
            if (ans[i] == 'Y' && v > 0) {
                for (int j = 0; j < v; j++) {
                    printf("VY");
                }
                v = 0;
            }
            if (ans[i] == 'B' && o > 0) {
                for (int j = 0; j < o; j++) {
                    printf("OB");
                }
                o = 0;
            }
        }
        printf("\n");
    }
    return 0;
}
