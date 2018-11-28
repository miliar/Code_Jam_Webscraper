#include <bits/stdc++.h>
using namespace std;

const int MAXN = 1e3+10;
bool v[MAXN];

int main()
{
    int tt;
    scanf("%d", &tt);
    for (int t = 1; t <= tt; t++) {
        int n = 0; char c;
        scanf(" %c", &c);
        while (c == '-' || c == '+') {
            if (c == '-') v[n++] = 0;
            else v[n++] = 1;
            c = getchar();
        }

        int m;
        scanf("%d", &m);

        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (v[i]) continue;
            if (n - i < m) { ans = -1; break; }

            ans++;
            for (int k = i; k - i < m; k++) {
                v[k] ^= 1;
            }
        }

        printf("Case #%d: ", t);
        if (ans < 0) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
}
