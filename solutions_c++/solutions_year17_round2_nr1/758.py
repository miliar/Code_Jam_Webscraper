#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; ++kase)
    {
        int D, N;
        scanf("%d %d", &D, &N);
        double ans = 0;
        for (int i = 0; i < N; ++i)
        {
            int K, S;
            scanf("%d %d", &K, &S);
            ans = max(ans, 1.0 * (D - K) / S);
        }
        printf("Case #%d: %.6f\n", kase, D / ans);
    }
    return 0;
}