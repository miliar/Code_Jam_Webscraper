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
typedef pair<int, int> pii;

// const int MNOGO = 0x3fffffff;

#define PROBLEM "C"

inline int findpos(vector<int64> &v, vector<int64> &c, int64 target, int start) {
    int j = start;
    for (; j < v.size() && v[j] != target; j++);
    if (j == v.size()) {
        v.PB(target);
        c.PB(0);

        assert(v[j-1] > v[j]);
    }
    return j;
}

int main() {
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    scanf("%d\n", &T);

    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);
        fprintf(stderr, "Case #%d\n", test);

        int64 n, k;
        cin >> n >> k;

        vector<int64> v;
        vector<int64> c;

        v.PB(n);
        c.PB(1);

        int64 step = 0;
        int i = 0;
        int answer = -1;
        while (v[i] > 0) {
            if (v[i] % 2 == 0) {
                int j1 = findpos(v, c, v[i] / 2, i);
                c[j1] += c[i];
                int j2 = findpos(v, c, v[i] / 2 - 1, i);
                c[j2] += c[i];
            } else {
                int j1 = findpos(v, c, v[i] / 2, i);
                c[j1] += 2*c[i];
            }
            step += c[i];
            if (k <= step) {
                answer = i;
                break;
            }
            i++;
        }

//         for (int p = 0; p < v.size(); p++) {
//             printf("%lld ", v[p]);
//         }
//         printf("\n");
//
//         for (int p = 0; p < c.size(); p++) {
//             printf("%lld ", c[p]);
//         }
//         printf("\n");

//         cout << answer << " " << v[answer] << " " << v[answer] / 2 << " " << (v[answer] - 1) / 2;

        cout << v[answer] / 2 << " " << (v[answer] - 1) / 2;

        printf("\n");
    }

    return 0;
}
