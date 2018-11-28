#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int T;
long long n, m, ans;
int main() {
    cin >> T;
    for (int C = 1, k; C <= T; C++) {
        cin >> n >> m;
        if (n == 1) {
            printf("Case #%d: 0 0\n", C);
            continue;
        }
        long long small = 1, large = 0;
        while (1) {
            if (m <= small + large) {
                if (m <= large) ans = n + 1; else ans = n;
                break;
            } else {
                m -= small + large;
                if (n & 1) small = small * 2 + large;
                else large = large * 2 + small;
                n = (n - 1) / 2;
            }
        }
        printf("Case #%d: %lld %lld\n", C, ans/2, (ans-1)/2);
    }
}