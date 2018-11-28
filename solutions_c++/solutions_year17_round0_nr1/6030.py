#include <iostream>
#include <cstdio>
#include <string>

const int maxn = 1111;

using namespace std;

int a[maxn];

int main() {
    freopen("AL.in", "r", stdin);
    freopen("ALout.txt", "w", stdout);
    int T, ca = 0;
    cin >> T;
    while (T--) {
        string str;
        int K;
        cin >> str >> K;
        int n = (int)str.size();
        for (int i = 0; i < n; ++i) {
            if (str[i] == '+') {
                a[i + 1] = 1;
            } else a[i + 1] = 0;
        }
        a[0] = 1;
        int ans = 0, ok = true;
        for (int i = 1; i <= n - K + 1; ++i) {
            if (a[i - 1] == 1 and a[i] == 0) {
                ans++;
                for (int j = i; j < i + K; ++j) {
                    a[j] = a[j] ^ 1;
                }
            }
        }
        for (int i = 1; i <= n; ++i) {
            if (a[i] == 0) ok = false;
        }
        if (ok) printf("Case #%d: %d\n", ++ca, ans);
        else printf("Case #%d: IMPOSSIBLE\n", ++ca);
    }
    return 0;
}