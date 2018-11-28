#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define PB(x) push_back(x)
#define MP(a, b) make_pair(a, b)

typedef long long int64;
typedef long double ldouble;
typedef pair<int64, int64> pii;

// const int MNOGO = 0x3fffffff;
const double PI = 3.141592653589793;

#define PROBLEM "A"

inline bool cmppc(pii a, pii b) {
    return a.first < b.first;
}

inline int64 sqr(int64 a) {
    return a * a;
}

inline void bubble(vector<int64> &a) {
    int k = a.size() - 1;
    while (k > 0 && a[k-1] > a[k]) {
        int64 t = a[k-1];
        a[k-1] = a[k];
        a[k] = t;
        k--;
    }
}

inline void shift(vector<int64> &a) {
    for (int k = 0; k < a.size() - 1; k++) {
        a[k] = a[k+1];
    }
    a.pop_back();
}

int main() {
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    scanf("%d\n", &T);

    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);
        fprintf(stderr, "Case #%d\n", test);

        int n, k;
        cin >> n >> k;

        vector<pii> pc;

        for (int i = 0; i < n; i++) {
            int64 r, h;
            cin >> r >> h;
            pc.PB(MP(r, h));
        }

        stable_sort(pc.begin(), pc.end(), cmppc);

        vector<int64> sides;

        int64 area = 0;
        for (int i = 0; i < k-1; i++) {
            int64 sidearea = 2 * pc[i].first * pc[i].second;
            sides.PB(sidearea);
            bubble(sides);
            area += sidearea;
        }

        int64 maxarea = 0;

        for (int i = k-1; i < n; i++) {
            int64 flatarea = sqr(pc[i].first);
            int64 sidearea = 2 * pc[i].first * pc[i].second;

            if (area + flatarea + sidearea > maxarea) {
                maxarea = area + flatarea + sidearea;
            }

            sides.PB(sidearea);
            bubble(sides);
            area += sidearea;
            int64 minarea = sides[0];
            shift(sides);
            area -= minarea;
        }

        printf("%0.7lf", PI * maxarea);

        printf("\n");
    }

    return 0;
}
