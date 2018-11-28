#include <iostream>
#include <fstream>
#include <cstring>
#include <iomanip>
using namespace std;

#define LL long long
#define LD double

LL T,N,Q,c[110][110],e[110],s[110],d[110],dist[110][110][110];
LD dp[110][110][110];

int main(){
    ifstream fin("input.in");
    ofstream fout("output.out");
    fin >> T;

    int t;
    for (t=1; t<=T; t++){
        fout << "Case #" << t << ": ";
        fin >> N >> Q;

        LL i,j,k;
        for (i=1; i<=N; i++)
            fin >> e[i] >> s[i];

        for (i=1; i<=N; i++)
            for (j=1; j<=N; j++)
                fin >> c[i][j];


        memset(dp,0,sizeof(dp));
        memset(dist,0,sizeof(dist));
        for (i=1; i<=N; i++)
            for (j=1; j<=N; j++){
                if (i==j) continue;
                dist[i][j][0]=c[i][j];
                if (dist[i][j][0]==-1) dist[i][j][0]=(1LL<<48);
            }

        for (k=1; k<=N; k++)
            for (i=1; i<=N; i++)
                for (j=1; j<=N; j++)
                    dist[i][j][k]=min(dist[i][j][k-1],dist[i][k][k-1]+dist[k][j][k-1]);

        for (i=1; i<=N; i++)
            for (j=1; j<=N; j++){
                if (i==j) continue;
                dp[i][j][0]=(1LL<<48);
                if (e[i]>=dist[i][j][N])
                    dp[i][j][0]=1.0*dist[i][j][N]/s[i];
            }

        for (k=1; k<=N; k++)
            for (i=1; i<=N; i++)
                for (j=1; j<=N; j++)
                    dp[i][j][k]=min(dp[i][j][k-1],dp[i][k][k-1]+dp[k][j][k-1]);


        while (Q--){
            fin >> i >> j;
            fout << fixed << setprecision(9) << dp[i][j][N] << " ";
        }

        fout << "\n";
    }

    return 0;
}
