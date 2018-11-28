//created by missever

#include<bits/stdc++.h>
#define MAX 1000000007
using namespace std;
typedef long long LL;
typedef pair<double,int> P;

const int maxn = 103;
int e[maxn],s[maxn];
LL p[maxn][maxn];
double g[maxn][maxn];

int main(){
    //freopen("C-large.in","r",stdin);
    //freopen("C-small-attempt.out","w",stdout);
    int n,t,i,j,k,q;
    scanf("%d",&t);
    for(int cas = 1;cas <= t; cas++)
    {
        printf("Case #%d: ",cas);
        scanf("%d%d",&n,&q);
        for(i = 1;i <= n; i++) scanf("%d%d",&e[i],&s[i]);
        for(i = 1;i <= n; i++)
        {
            for(j = 1;j <= n; j++)
            {
                scanf("%I64d",&p[i][j]);
                //if(j == i) p[i][j] = 0;
                g[i][j] = -1.0;
            }
        }
        for(i = 1;i <= n; i++)
        {
            for(j = 1;j <= n; j++)
            {
                for(k = 1;k <= n; k++)
                {
                    if(p[j][i] != -1 && p[i][k] != -1 && (p[j][k] > p[j][i] + p[i][k] || p[j][k] == -1)) p[j][k] = p[j][i] + p[i][k];
                }
            }
        }
        for(i = 1;i <= n; i++)
        {
            for(j = 1;j <= n; j++)
            {
                if(p[i][j] == -1 || p[i][j] > e[i]) g[i][j] = -1.0;
                else g[i][j] = 1.0 * p[i][j] / s[i];
                //cout<<p[i][j]<<" ";
            }
            //cout<<endl;
        }
        for(i = 1;i <= n; i++)
        {
            for(j = 1;j <= n; j++)
            {
                for(k = 1;k <= n; k++)
                {
                    if(g[j][i] != -1.0 && g[i][k] != -1.0 && (g[j][k] > g[j][i] + g[i][k] || g[j][k] == -1.0)) g[j][k] = g[j][i] + g[i][k];
                }
            }
        }
        for(i = 1;i <= q; i++)
        {
            scanf("%d%d",&j,&k);
            printf("%.8f%c",g[j][k]," \n"[i == q]);
        }
    }
    return 0;
}
