#include <stdio.h>
#include <vector>
#include <algorithm>
std::vector<double> V;
int main()
{
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("C-small-1-attempt0.out", "w", stdout);
    int T, t;
    scanf("%d", &T);
    int i, j;
    int N, K;
    double U, P;
    double ans;
    for (t = 1; t <= T; t++)
    {
        scanf("%d %d", &N, &K);
        scanf("%lf", &U);
        V.clear();
        for (i = 0; i < N; i++)
        {
            scanf("%lf", &P);
            V.push_back(P);
        }
        std::sort(V.begin(), V.end());
        while (1)
        {
            for (i = 1; i < N; i++)
                if (V[i] != V[i - 1])
                    break;
            if (i == N)
            {
                if (U/((double) i) + V[i - 1] <= 1.0)
                {
                    for (j = 0; j < N; j++)
                        V[j] += U/((double) i);
                    ans = 1.0;
                    for (j = 0; j < N; j++)
                        ans *= V[j];
                    printf("Case #%d: %lf\n", t, ans);
                    break;
                }
                else
                {
                    printf("Case #%d: %lf\n", t, 1.0);
                    break;
                }
            }
            if (U/((double) i) + V[i - 1] <= V[i])
            {
                for (j = 0; j < i; j++)
                    V[j] += U/((double) i);
                ans = 1.0;
                for (j = 0; j < N; j++)
                    ans *= V[j];
                printf("Case #%d: %lf\n", t, ans);
                break;
            }
            else
            {
                for (j = 0; j < i; j++)
                {
                    U -= V[i] - V[j];
                    V[j] = V[i];
                }
            }
        }
        // for (j = 0; j < N; j++)
        //     printf("end%lf\n", V[j]);
    }
}
