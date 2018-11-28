#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

int main() {
//    freopen("B-small-attempt0.in", "r", stdin);
//    freopen("B-small-attempt0.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T;
    LL N;

    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        scanf("%lld", &N);
        string str = to_string(N);
        int n = (int)str.size();
        for (int i = 1; i < n; i++) {
            if (str[i] < str[i - 1]) {
                for (int j = i + 1; j < n; j++) {
                    str[j] = '9';
                }
                for (int j = i - 1; j >= 0; j--) {
                    if (str[j] > str[j + 1]) {
                        str[j] -= 1;
                        str[j + 1] = '9';
                    }
                }
            }
        }
        printf("Case #%d: %lld\n", t, atoll(str.c_str()));
    }

    return 0;
}

