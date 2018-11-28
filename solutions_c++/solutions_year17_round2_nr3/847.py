#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <cmath>
#include <climits>
#include <vector>
#include <queue>
#include <cstring>
#include <iterator>
#include <list>
#include <set>
#include <map>
#include <bitset>

using namespace std;

#define MEMSET(x,v) memset(x,v,sizeof(x))
template<class A, class B> inline bool mina(A &x, B y) {return (x > y)?(x=y,1):0;}
template<class A, class B> inline bool maxa(A &x, B y) {return (x < y)?(x=y,1):0;}
typedef long long int LL;

LL D[110][110];
LL dist[110][110];
LL Es[110];
LL Ss[110];
int Us[110];
int Vs[110];
double dp[110];
int main()
{
    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        int N, Q;
        scanf("%d %d", &N, &Q);

        for(int i = 1; i <= N; i++) {
            scanf("%lld %lld", Es+i, Ss+i);
        }
        for(int i = 1; i <= N; i++) {
            for(int j = 1; j <= N; j++) {
                scanf("%lld", &D[i][j]);
                if(D[i][j] == -1) {
                    D[i][j] = 2000000000000;
                }
            }
        }
        for(int i = 1; i <= Q; i++) {
            scanf("%d %d", Us+i, Vs+i);
        }


        dist[1][1] = 0;
        for(int i = 2; i <= N; i++) {
            dist[1][i] = dist[1][i-1]+D[i-1][i];
        }
        for(int i = 1; i <= N; i++) {
            for(int j = i; j <= N; j++) {
                dist[i][j] = dist[1][j]-dist[1][i];
            }
        }

        dp[N] = 0;
        for(int i = N-1; i >= 1; i--) {
            double fastestT = 1e30;
            for(int j = i+1; dist[i][j] <= Es[i] && j <= N; j++) {
                mina(fastestT, dist[i][j]/(double)Ss[i]+dp[j]);
            }
            dp[i] = fastestT;
        }
        printf("Case #%d: %lf\n", t, dp[1]);
    }
}
