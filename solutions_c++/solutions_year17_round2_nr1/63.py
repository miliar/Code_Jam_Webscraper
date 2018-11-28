#include <cstdio>
#include <algorithm>

int main()
{
    int T;
    scanf("%d", &T);
    for (int tt = 1; tt <= T; tt++)
    {
        int N, D;
        scanf("%d%d", &D, &N);
        double res = 0;
        for (int i = 0; i < N; i++)
        {
            int K, S;
            scanf("%d%d", &K, &S);
            res = std::max(res, 1.0*(D-K)/S);
        }
        printf("Case #%d: %.9f\n", tt, D/res);
    }
}
