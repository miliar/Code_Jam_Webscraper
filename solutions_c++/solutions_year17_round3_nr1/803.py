#include <stdio.h>
#include <vector>
#include <algorithm>
#define PI 3.14159265358979
typedef struct node node;
struct node
{
    double r, h;
};
std::vector<node> V;
int compareR(node a, node b)
{
    return (a.r < b.r);
}
double DP[1005][1005];
double max(double a, double b)
{
    return (a > b)?a:b;
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, t;
    scanf("%d", &T);
    int N, K;
    double r, h;
    double ans;
    int i, j, k;
    for (t = 1; t <= T; t++)
    {
        scanf("%d %d", &N, &K);
        V.clear();
        for (i = 0; i < N; i++)
        {
            scanf("%lf %lf", &r, &h);
            V.push_back({r, h});
        }
        std::sort(V.begin(), V.end(), compareR);
        // for (i = 0; i < N; i++)
        //     printf("sorted %lf %lf\n", V[i].r, V[i].h);
        ans = 0;
        for (i = 0; i < K; i++)
        {
            for (j = 0; j < N; j++)
            {
                if (i == 0)
                    DP[i][j] = 2*PI*V[j].r*V[j].h + PI*V[j].r*V[j].r;
                else
                {
                    DP[i][j] = 0;
                    for (k = 0; k < j; k++)
                        DP[i][j] = max(DP[i][j], DP[i - 1][k] + 2*PI*V[j].r*V[j].h + PI*V[j].r*V[j].r - PI*V[k].r*V[k].r);
                }
                // printf("i%d j%d %lf\n", i, j, DP[i][j]);
                if (i == K - 1 && DP[i][j] > ans)
                    ans = DP[i][j];
            }
        }
        printf("Case #%d: %lf\n", t, ans);
    }
}
