#include<bits/stdc++.h>
using namespace std;

int req[50], pkg[50][50];
long long rl[50], rr[50];
set<pair<int,int>> pos[50];

int main()
{
    int T;
    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        int n,m, cl=1000000,cr=0;
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
            scanf("%d", req+i);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            {
                scanf("%d",pkg[i]+j);
                int tmp = (pkg[i][j]*10LL)/11/req[i] - 1;
                if(tmp < cl) cl = tmp;
                tmp = pkg[i][j]*10LL/9/req[i] + 1;
                if(tmp > cr) cr = tmp;
            }
        if(cl<1) cl = 1;
        if(cr>1000000) cr = 1000000;
        int ans = 0;
        for(long long c=1;c<=1000000;c++)
        {
            bool ok = true;
            for(int i=0;ok && i<n;i++)
            {
                pos[i].clear();
                long long l = (req[i]*c*9+9)/10, r = req[i]*c*11/10;
                for(int j=0;j<m;j++)
                {
                    if(l <=pkg[i][j] && pkg[i][j] <= r)
                        pos[i].emplace(pkg[i][j],j);
                }
                ok = !pos[i].empty();
            }
            while(ok)
            {
                for(int i=0;i<n;i++)
                {
                    int j = pos[i].begin()->second;
                    pkg[i][j] = -1;
                    pos[i].erase(pos[i].begin());
                    if(pos[i].empty()) ok = false;
                }
                ans++;
            }
        }
        printf("%d\n",ans);
    }
}
