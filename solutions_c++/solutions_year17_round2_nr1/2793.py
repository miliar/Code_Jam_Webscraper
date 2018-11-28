#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

struct on {
        double k, s;
        bool operator < (const on &A) const {
                return k != A.k ? k < A.k : s > A.s;
        }
}no[1010];

int main ()
{
        freopen ("in.txt", "r", stdin);
        freopen ("out.txt", "w", stdout);
        int T;
        scanf ("%d", &T);
        for (int cas = 1; cas <= T; cas++) {
                int D, N;
                scanf ("%d%d", &D, &N);
                for (int i = 1; i <= N; i++) {
                        scanf ("%lf%lf", &no[i].k, &no[i].s);
                }
                sort (no + 1, no + N + 1);
                double ans = 1e15;
                for (int i = 1; i <= N; i++) {
                        ans = min (ans, 1.0 * D / (D - no[i].k) * no[i].s);
                }
                printf ("Case #%d: %.6f\n", cas, ans);
        }
        return 0;
}
