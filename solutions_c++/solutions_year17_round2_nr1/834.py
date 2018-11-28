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

#define PROBLEM "A"

int main() {
    freopen(PROBLEM ".in", "rt", stdin);
    freopen(PROBLEM ".out", "wt", stdout);

    int T;
    scanf("%d\n", &T);

    for (int test = 1; test <= T; test++) {
        printf("Case #%d: ", test);
        fprintf(stderr, "Case #%d\n", test);

        int64 d, n;
        cin >> d >> n;

        double maxtime = -1;
        for (int i = 0; i < n; i++) {
            int64 k, s;
            cin >> k >> s;
            double time = (1.0 * (d - k)) / s;
            if (time > maxtime) {
                maxtime = time;
            }
        }

        double speed = d / maxtime;

        printf("%0.7lf", speed);

        printf("\n");
    }

    return 0;
}
