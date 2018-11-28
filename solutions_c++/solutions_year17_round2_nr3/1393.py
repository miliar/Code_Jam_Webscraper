#pragma comment(linker, "/STACK:102400000,102400000")
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <complex>
#define LL long long
#define ULL long long
#define ls(x) tree[x].ls
#define rs(x) tree[x].rs
#define maxx(x) tree[x].maxx
#define len(p) (p.R-p.L+1)
#define keytree ch[ch[root][1]][0]
#define dis(x) dis[x.x1][x.y1][x.x2][x.y2][x.dir1][x.dir2]
using namespace std;
const int M = 100 + 5, INF = 0x3f3f3f3f, mod = 1e9 + 7;
int E[M],S[M];
LL D[M][M];
double dis[M][M];
bool mark[M][M];
LL sum[M];
int main() {
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int T,cas=1;
    scanf("%d",&T);
    while(T--){
        int n,q;
        scanf("%d%d",&n,&q);
        for(int j=1;j<=n;j++) scanf("%d%d",&E[j],&S[j]);
        for(int j=1;j<=n;j++){
            for(int k=1;k<=n;k++){
                scanf("%lld",&D[j][k]);
            }
        }
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                for(int k=1;k<=n;k++){
                    if(D[j][i]!=-1&&D[i][k]!=-1){
                        if(D[j][k]!=-1) D[j][k]=min(D[j][k],D[j][i]+D[i][k]);
                        else D[j][k]=D[j][i]+D[i][k];
                    }
                }
            }
        }
        //if(T==1) printf("D = %f\n",D[1][3]);
        double ans=0;
        printf("Case #%d:",cas++);
        while(q--){
            int u,v;
            scanf("%d%d",&u,&v);
            for(int j=1;j<=n;j++) for(int k=1;k<=n;k++) dis[j][k]=1e18;
            memset(mark,0,sizeof(mark));
            queue<pair<int,int> >Q;
            Q.push({u,u});
            dis[u][u]=0;
            while(!Q.empty()){
                auto now=Q.front();Q.pop();
                int u=now.first,st=now.second;
                mark[u][st]=0;
                for(int j=1;j<=n;j++){
                    if(D[u][j]==-1) continue;
                    if(D[u][j]<=E[u]){
                        if(dis[j][u]>dis[u][st]+1.0*D[u][j]/S[u]){
                            dis[j][u]=dis[u][st]+1.0*D[u][j]/S[u];
                            if(!mark[j][u]){
                                mark[j][u]=1;
                                Q.push({j,u});
                            }
                        }
                    }
                }
            }
//            if(T==1){
//                printf("dis = %f D = %lld\n",dis[3][1],D[1][4]);
//            }
            double ans=1e18;
            for(int j=1;j<=n;j++) ans=min(ans,dis[v][j]);
            printf(" %.12f",ans);
        }
        printf("\n");
    }
    return 0;
}
