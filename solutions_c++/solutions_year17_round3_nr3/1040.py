#include <bits/stdc++.h>

#define LL long double

using namespace std;

void _solve() {
    int n, k;
    scanf("%d %d", &n, &k);

    LL u;
    scanf("%LF", &u);

    LL sum = 0;
    int nn = 0;

    vector<LL> data(n);
    for(int i = 0; i < n; i++) {
        scanf("%LF", &data[i]);

        if(data[i] != 1) {
            sum += data[i];
            nn++;
        }
    }

    sort(data.begin(), data.end());

    bool done = false;
    for(int i = 1; i < n; i++) {
        LL t = data[i];
        if(t == 0.0) break;
        // for(int j = 0; j < n; j++) {
        //     printf("%d: %.10LF\n", j, data[j]);
        // }
        // printf("\n");
        
        LL amt = 0;
        for(int j = 0; j < i; j++) {
            if(u - (t - data[j]) > 0) {
                amt += t - data[j];
            }
        }

        if(u >= amt) {
            for(int j = 0; j < i; j++) {
                if(u - (t - data[j]) > 0) {
                    u -= t - data[j];
                    data[j] = t;
                }
            }
        } else {
            LL sum = 0;
            int nn = 0;

            for(int j = 0; j < i; j++) {
                sum += data[j];
                nn++;
            }

            LL b = (sum + u) / nn;
            for(int j = 0; j < i; j++) {
                data[j] = b;
            }

            u = 0;
        }
    }

    if(u > 0) {
        // printf("HI\n");
        LL sum = 0;
        int nn = 0;

        for(int i = 0; i < n; i++) {
            sum += data[i];
            nn++;
        }

        LL b = (sum + u) / nn;
        for(int i = 0; i < n; i++) {
            data[i] = b;
        }
    }

    LL res = 1;
    for(int i = 0; i < n; i++) {
        // printf("%d: %.10LF\n", i, data[i]);
        res *= data[i];
    }

    printf("%.10LF\n", res);
}

int main() {
    int t;
    scanf("%d", &t);

    for(int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        // printf("\n");
        _solve();
    }

    return 0;
}