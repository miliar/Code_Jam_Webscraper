#include <bits/stdc++.h>
using namespace std;
#define MUL 2500

void preprocess() {
}

bool okay(long long real, long long needed) {
    long long guess = real / needed;
    for (long long m = max(1ll, guess-MUL); m <= guess+MUL && needed*m <= 2*real; ++m) {
        bool x = 10*real >= needed*m*9;
        bool y = 10*real <= needed*m*11;
        if (x && y) {
            //printf("\t((real = %lld => deu m=%lld, entre %.2lf e %.2lf))\n", real, m, m*needed*0.9f, m*needed*1.1f);
            return true;
        }
    }
    return false;
}

bool okay(long long real, long long needed, long long real2, long long needed2) {
    long long guess = real / needed;
    for (long long m = max(1ll, guess-MUL); m <= guess+MUL && needed*m <= 2*real; ++m) {
        bool x = 10*real >= needed*m*9;
        bool y = 10*real <= needed*m*11;
        bool x2 = 10*real2 >= needed2*m*9;
        bool y2 = 10*real2 <= needed2*m*11;
        if (x && y && x2 && y2) {
            //printf("\t((real = %lld => deu m=%lld, entre %.2lf e %.2lf))\n", real, m, m*needed*0.9f, m*needed*1.1f);
            return true;
        }
    }
    return false;
}

void process_testcase(const int testcase, const int should_run) {
    int n, p;
    scanf("%d%d", &n, &p);
    long long needed[n];
    for (int i = 0; i < n; ++i)
        scanf("%lld", needed+i);
    long long ing[n][p];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < p; ++j)
            scanf("%lld", &ing[i][j]);

    if (should_run) {
        int ans = -1;
        if (n == 1) {
            int cnt = 0;
            for (int i = 0; i < p; ++i)
                if (okay(ing[0][i], needed[0]))
                    ++cnt;
            ans = cnt;
        } else if (n == 2) {
            int vec[p];
            for (int i = 0; i < p; ++i)
                vec[i] = i;
            ans = 0;
            do {
                int cnt = 0;
                for (int i = 0; i < p; ++i)
                    if (okay(ing[0][i], needed[0], ing[1][vec[i]], needed[1]))
                        //printf("\t((%d vs %d))\n", (int) ing[0][i], (int) ing[1][vec[i]]),
                        ++cnt;
                ans = max(ans, cnt);
                //printf("(achei %d)\n", cnt);
            } while (next_permutation(vec, vec+p));
        }
        printf("Case #%d: %d\n", testcase, ans);
    }
}
