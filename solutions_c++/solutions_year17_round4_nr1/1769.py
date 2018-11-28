#include <bits/stdc++.h>
using namespace std;

int t,n,p,x;
int g[5];

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    scanf("%d",&t);
    for(int tc = 1; tc <= t; tc++){
        scanf("%d%d",&n,&p);
        int sol = 0;
        g[0] = g[1] = g[2] = g[3] = 0;
        for(int i = 0; i < n; i++){
            scanf("%d",&x);
            if(x%p==0) sol++;
            else g[x%p]++;
        }
        if(p == 2) sol += (g[1]+1)/2;
        if(p == 3){
            int mg = min(g[1],g[2]);
            sol += mg;
            g[1] -= mg;
            g[2] -= mg;
            sol += (max(g[1],g[2])+2)/3;
        }
        printf("Case #%d: %d\n",tc,sol);
    }
}