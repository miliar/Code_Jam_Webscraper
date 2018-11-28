#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
#define MAXN 1003
#define MAXM 1003
#define MAXC 1003
int n, m, c;
int a[MAXC][MAXN];
struct Tt {
    int num0, num1;
    Tt(int x, int y): num0(x), num1(y) {}
};
int a2[MAXN], sum[MAXN];
int main()
{
    int T;
    scanf("%d", &T);
    for (int Ti = 1; Ti <= T; ++Ti) {
        scanf("%d%d%d", &n, &c, &m);
        memset(a, 0, sizeof(a));
        memset(a2, 0, sizeof(a2));
        memset(sum, 0, sizeof(sum));
        for (int i = 0; i < m; ++i) {
            int p, b;
            scanf("%d%d", &p, &b);
            b--, p--;
            a[b][p]++;
            a2[p]++;
        }
        sum[0] = a2[0];
        for (int i = 1; i < n; ++i)
            sum[i] = a2[i] + sum[i - 1];
        int n1[2] = {}, n2[2] = {};
        int ans1 = 0, ans2 = 0;
        n1[0] = a[0][0], n1[1] = a[1][0];
        for (int i = 1; i < n; ++i)
            n2[0] += a[0][i], n2[1] += a[1][i];
        int t = min(n1[0], n2[1]);
        ans1 += t, n1[0] -= t, n2[1] -= t;
        t = min(n1[1], n2[0]);
        ans1 += t, n1[1] -= t, n2[0] -= t;
        t = max(n2[0], n2[1]);
        ans1 += t;
        ans1 += n1[0] + n1[1];
        for (int i = 0; i < n; ++i)
            if (a2[i] > ans1)
                ans2 += a2[i] - ans1;
        printf("Case #%d: %d %d\n", Ti, ans1, ans2);
    }
    return 0;
}
