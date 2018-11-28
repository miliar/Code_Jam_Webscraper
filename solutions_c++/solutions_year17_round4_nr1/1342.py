#include <bits/stdc++.h>
#define LL long long
#define INF 0x3f3f3f3f
using namespace std;

template<class T> inline
void read(T& x) {
    int f = 1; x = 0;
    char ch = getchar();
    while (ch < '0' || ch > '9')   {if (ch == '-') f = -1; ch = getchar();}
    while (ch >= '0' && ch <= '9') {x = x * 10 + ch - '0'; ch = getchar();}
    x *= f;
}

/*============ Header Template ============*/

const int N = 100 + 5;

int n, P;
int a[N], c[N], p[N];

int main() {
    int T, kas = 0;
    read(T);
    while (T--) {
        read(n), read(P);
        for (int i = 1; i <= n; i++) read(a[i]);
        if (P == 2) {
            int ans = 0, tmp = 0;
            for (int i = 1; i <= n; i++) if ((a[i] & 1) == 0) ans++;
                else tmp++;
            ans = ans + tmp / 2 + (tmp & 1);
            printf("Case #%d: %d\n", ++kas, ans);
        }
        if (P == 3) {
            memset(c, 0, sizeof c);
            for (int i = 1; i <= n; i++) c[a[i] % 3]++;
            int ans = c[0], tmp = min(c[1], c[2]);
            ans += tmp;
            c[1] -= tmp; c[2] -= tmp;
            ans += c[1] / 3 + (c[1] % 3 ? 1 : 0);
            ans += c[2] / 3 + (c[2] % 3 ? 1 : 0);
            printf("Case #%d: %d\n", ++kas, ans);
        }
        if (P == 4) {
            memset(c, 0, sizeof c);
            for (int i = 1; i <= n; i++) c[a[i] % 4]++;
            int ans = 0;
            // 1   c[1] + c[3]
            // 2   c[2] + c[2]
            // 3   2 * c[1] + c[2]
            // 4   c[2] + 2 * c[3]
            // 5   c[1]
            // 6   c[2]
            // 7   c[3]
            for (int i = 1; i <= 7; i++) p[i] = i;
            do {
                int A = c[1], B = c[2], C = c[3], fuck = 0;
                for (int i = 1; i <= n; i++) {
                    if (p[i] == 1) {
                        int tmp = min(A, C);
                        fuck += tmp;
                        A -= tmp;
                        C -= tmp;
                    }
                    if (p[i] == 2) {
                        int tmp = B / 2;
                        fuck += tmp;
                        B = B % 2;
                    }
                    if (p[i] == 3) {
                        int t = min(A / 2, B);
                        fuck += t;
                        A -= t * 2;
                        B -= t;
                    }
                    if (p[i] == 4) {
                        int t = min(B, C / 2);
                        fuck += t;
                        B -= t;
                        C -= t * 2;
                    }
                    if (p[i] == 5) {
                        fuck += A / 4;
                        A %= 4;
                    }
                    if (p[i] == 6) {
                        fuck += B / 4;
                        B %= 4;
                    }
                    if (p[i] == 7) {
                        fuck += C / 4;
                        C %= 4;
                    }
                }
                if (A || B || C) fuck++;
                ans = max(ans, fuck);
            } while (next_permutation(p + 1, p + 7 + 1));
            ans += c[0];
            printf("Case #%d: %d\n", ++kas, ans);
        }
    }
    return 0;
}