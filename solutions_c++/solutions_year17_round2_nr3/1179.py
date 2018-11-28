#include <cstdio>
#include <algorithm>

using namespace std;

typedef long long ll;

int N, Q;
ll e[128], s[128];
ll dist[128][128];

double cost[128];

double opt(int city)
{
    if(city == N-1)
        return 0;

    if(cost[city] > -0.5)
        return cost[city];

    cost[city] = 1e18;

    //on prend l'actuel
    long long S = 0;
    for(int i = city+1; (i < N); i++)
    {
        S += dist[i-1][i];
        if(S > e[city])
            break;

        double time = (double)S/(double)s[city] + opt(i);
        cost[city] = min(cost[city], time);
    }

    //printf("%d -> %f\n", city, cost[city]);
    return cost[city];
}

int main()
{
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("C-small-attempt1.out", "w", stdout);

    int nbT;
    scanf("%d", &nbT);

    for(int ct = 1; ct <= nbT; ct++)
    {
        scanf("%d%d", &N, &Q);
        for(int i = 0; i < N; i++)
        {
            scanf("%lld%lld", &e[i], &s[i]);
            cost[i] = -1;
        }

        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
                scanf("%lld", &dist[i][j]);

        printf("Case #%d: ", ct);
        while(Q--)
        {
            int u, v;
            scanf("%d%d", &u, &v);
            printf("%.07f", opt(0));
        }

        printf("\n");
    }

    return 0;
}
