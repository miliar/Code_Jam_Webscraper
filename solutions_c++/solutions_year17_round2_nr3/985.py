#include <bits/stdc++.h>

using namespace std;

//int dirs[4][2]={{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
//int dirs[8][2]={{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

long long inf=1e18;

int main()
{
    //ios::sync_with_stdio(false);
    freopen("inp.in", "r", stdin);
    freopen("outp.out", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for(int case_no=1; case_no<=tc; case_no++)
    {
        printf("Case #%d:", case_no);
        //cout << "Case #" << case_no << ":";
        cerr << "Start geval " << case_no << endl;
        int N, Q;
        scanf("%d %d", &N, &Q);
        vector<long long> max_dist(N);
        vector<long long> speed(N);
        for(int i=0; i<N; i++)
        {
            scanf("%lld %lld", &max_dist[i], &speed[i]);
        }
        vector< vector<long long> > afstand(N, vector<long long>(N, inf));
        for(int i=0; i<N; i++)
        {
            for(int j=0; j<N; j++)
            {
                scanf("%lld", &afstand[i][j]);
                if(afstand[i][j]==-1) afstand[i][j]=inf;
                if(i==j) afstand[i][j]=0;
            }
        }
        for(int via=0; via<N; via++)
        {
            for(int from=0; from<N; from++)
            {
                for(int to=0; to<N; to++)
                {
                    afstand[from][to]=min(afstand[from][to], afstand[from][via]+afstand[via][to]);
                }
            }
        }

        for(int query_no=1; query_no<=Q; query_no++)
        {
            int from, to_ultimate;
            scanf("%d %d", &from, &to_ultimate);
            from--;
            to_ultimate--;
            vector< vector<double> > best(N+1, vector<double>(N+1, inf));
            for(int i=0; i<N; i++)
            {
                if(i==from) continue;
                if(afstand[from][i] <= max_dist[from])
                {
                    best[1][i]=(1.0*afstand[from][i])/speed[from];
                }
            }

            //cerr << "REACHED" << endl;
            for(int nb_horses=2; nb_horses<=N; nb_horses++)
            {
                for(int dest=0; dest<N; dest++)
                {
                    if(dest==from) continue;
                    for(int via=0; via<N; via++)
                    {
                        if(via==dest) continue;
                        if(afstand[via][dest] <= max_dist[via])
                        {
                            best[nb_horses][dest]=min(best[nb_horses][dest], best[nb_horses-1][via]+((1.0*afstand[via][dest])/speed[via]));
                        }
                    }
                }
            }
            double ans=inf;
            for(int nb_horses=1; nb_horses<=N; nb_horses++)
            {
                ans = min(ans, best[nb_horses][to_ultimate]);
            }
            printf(" %.12f", ans);
        }
        printf("\n");
    }
    return 0;
}
