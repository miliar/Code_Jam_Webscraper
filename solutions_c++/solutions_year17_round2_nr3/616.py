#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <queue>
#include <map>

using namespace std;
string ans;
long long D[200][200];
int E[200], S[200];
double P[200][200];
int main()
{
    freopen( "in.txt", "r", stdin);
    freopen( "out.txt", "w", stdout);
	int T, cas = 0;
	cin>>T;
	while ( T -- )
	{
	    int N,Q;
	    cin>>N>>Q;
	    for (int i=0;i<N;i++)
        {
            cin>>E[i]>>S[i];
        }
        for (int i=0;i<N;i++)
            for (int j=0;j<N;j++)
            cin>>D[i][j];
        for (int k=0;k<N;k++)
            for (int i=0;i<N;i++)
                for (int j=0;j<N;j++)
                if (D[i][k]!=-1 && D[k][j]!=-1 && (D[i][k]+D[k][j] < D[i][j]|| D[i][j]==-1))
        D[i][j]=D[i][k]+D[k][j];
        for (int i=0;i<N;i++)
                for (int j=0;j<N;j++)
                {
                    P[i][j]=1e100;
                    if (E[i] >= D[i][j] && D[i][j]>0){
                        P[i][j] = D[i][j] / (S[i]+.0);
                    }
                }
        for (int i=0;i<N;i++)
                P[i][i]=0;
        for (int k=0;k<N;k++)
            for (int i=0;i<N;i++)
                for (int j=0;j<N;j++)
                if (P[i][k] + P[k][j] < P[i][j])
                    P[i][j] = P[i][k] + P[k][j];
  //  for (int i=0;i<N;i++)
  //              for (int j=0;j<N;j++)
  //                  printf("%.8f%c", P[i][j], j==N-1?'\n':' ');
        printf("Case #%d:", ++cas);
        while (Q--){
            int u,v;
            cin>>u>>v;
            u--;v--;
            printf(" %.8f", P[u][v]);
        }
        printf("\n");
	}
	return 0;
}
