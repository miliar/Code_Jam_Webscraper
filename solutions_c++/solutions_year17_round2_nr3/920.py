#include <cstdio>
#include <algorithm>
#include <queue>
using namespace std;
typedef pair<int, int> ii; // dleft, speed
typedef pair<int, ii> iii; // location, ii
typedef pair<double, iii> di;
int n, q;
int e[101], s[101];
double d[101][101];
bool v[101];
int main()
{
    freopen("cin.txt", "r", stdin);
    freopen("cout.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int z = 1; z <= t; z++)
    {
        printf("Case #%d: ", z);
        scanf("%d%d", &n, &q);
        for (int i = 0; i < n; i++)
            scanf("%d%d", &e[i], &s[i]);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                scanf("%lf", &d[i][j]);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                for (int k = 0; k < n; k++)
                    if (d[j][i] >= -0.0000000000001 && d[i][k] >= -0.0000000000001)
                        d[j][k] = d[j][k] < 0 ? d[j][i] + d[i][k] : min(d[j][k], d[j][i] + d[i][k]);

        /*for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
                printf("%d ", d[i][j]);
            printf("\n");
        }*/


        for (int i = 0; i < q; i++)
        {
            int a, b;
            scanf("%d%d", &a, &b);
            a--; b--;
            for (int j = 0; j < n; j++)
            {
                v[j] = false;
            }
            priority_queue<di> pq;
            pq.push(di(0, iii(a, ii(0, 10000))));
            while (!pq.empty())
            {
                di next = pq.top();
                pq.pop();
                double time = -next.first;
                int loc = next.second.first;
                int left = next.second.second.first;
                int spd = next.second.second.second;
                if (v[loc]) continue;
                v[loc] = true;
                //printf("\n:%lf, %d, %d:", time, loc, left);
                if (loc == b)
                {
                    printf("%.7lf ", time);
                    break;
                }
                for (int j = 0; j < n; j++)
                {
                    if (v[j]) continue;
                    if (d[loc][j] == -1) continue;
                    if (d[loc][j] <= left)
                    {
                        pq.push(di(-(time + ((double)d[loc][j])/spd),
                                   iii(j,
                                       ii(left - d[loc][j],
                                          spd))));

                    }
                    if (d[loc][j] <= e[loc])
                    {
                        pq.push(di(-(time + ((double)d[loc][j])/s[loc]),
                                   iii(j,
                                       ii(e[loc] - d[loc][j],
                                          s[loc]))));
                    }
                }
            }
            //printf(";");
        }
        printf("\n");
    }
    return 0;
}
