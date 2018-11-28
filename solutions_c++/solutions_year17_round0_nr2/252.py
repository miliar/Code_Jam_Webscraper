#include <bits/stdc++.h>
using namespace std;

int a[20];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        string s;
        cin >> s;
        int n = s.size();
        for (int i = 0; i < n; i++) {
            a[i] = s[i] - '0';
        }
        while (true) {
            int err = -1;
            for (int i = 0; i + 1 < n; i++) {
                if (a[i] > a[i + 1]) {
                    err = i;
                    break;
                }
            }
            if (err == -1) {
                break;
            }
            a[err]--;
            for (int i = err + 1; i < n; i++) {
                a[i] = 9;
            }
        }
        long long res = 0;
        for (int i = 0; i < n; i++) {
            res = res * 10 + a[i];
        }
        cerr << res << endl;
        printf("Case #%d: %I64d\n", cas, res);
    }
    return 0;
}

