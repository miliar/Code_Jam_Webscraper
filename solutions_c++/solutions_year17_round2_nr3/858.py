#include <bits/stdc++.h>

using namespace std;

const int maxN = 1e2+10;
int test, N, Q, src, des;
int dist[maxN], speed[maxN];
double L[maxN], F[maxN];

int main()
{
    freopen("googlejam.inp","r",stdin);
    freopen("googlejam.out","w",stdout);
    cin >> test;
    for (int t=1; t <= test; t++)
    {
        printf("Case #%d: ",t);
        cin >> N >> Q;
        for (int i=1; i <= N; i++) cin >> dist[i] >> speed[i];
        for (int i=1; i <= N; i++)
            for (int j=1,x; j <= N; j++)
            {
                cin >> x;
                if (i+1 == j) L[j] = x;
            }
        cin >> src >> des;
        memset(F,0,sizeof(F));
        F[2] = L[2]/speed[1];
        for (int i=3; i <= N; i++)
        {
            double w = L[i];
            for (int j=i-1; j; j--)
            {
                if (w <= dist[j])
                    if (F[i] == 0) F[i] = F[j] + w/speed[j];
                    else F[i] = min(F[i], F[j] + w/speed[j]);
                w += L[j];
            }
        }
        printf("%.9lf\n",F[N]);
    }
}
