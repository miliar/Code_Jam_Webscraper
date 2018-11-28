#include <cstdio>
#include <algorithm>
using namespace std;

int T;
int D, N;
int K, S;
double max_time;
double ans;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    for (int z = 1; z <= T; ++z)
    {
        max_time = 0.0;
        scanf("%d%d", &D, &N);
        for (int i = 0; i < N; ++i)
        {
            scanf("%d%d", &K, &S);
            max_time = max(max_time, ((double)D - K) / S);
        }
        ans = (double)D / max_time;
        printf("Case #%d: %.6f\n", z, ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
