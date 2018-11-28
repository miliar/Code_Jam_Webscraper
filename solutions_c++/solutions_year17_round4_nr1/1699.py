#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100;

int n, p;
int v[MAXN];

int main()
{
    int nt;
    scanf("%d", &nt);
    for (int t = 1; t <= nt; t++) {
        int n, p, ans = 0;
        scanf("%d %d", &n, &p);
        for (int i = 0; i < n; i++) {
            scanf("%d", &v[i]);
            if (v[i] % p == 0) ans++, n--, i--;
        }

        for (int i = 0; i < n; i++) {
            v[i] %= p;
        }

        printf("Case #%d: ", t);
        if (p == 2) {
            printf("%d\n", ans + (n+1)/2);
        } else if (p == 3) {
            int c1 = 0, c2 = 0;
            for (int i = 0; i < n; i++) {
                if (v[i] == 1) c1++;
                else c2++;
            }

            int aux = min(c1, c2);
            ans += aux; c1 -= aux; c2 -= aux;

            if (c1 > 0) ans += (c1 + 2)/3;
            else ans += (c2 + 2)/3;

            printf("%d\n", ans);
        }
    }
}
