#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<algorithm>
using namespace std;
const int MAXN=1005;
int p[MAXN],b[MAXN],cnt[MAXN];
int od[MAXN][MAXN],nw[MAXN][MAXN];
pair<int,int> check(int n,int m,int c,int r)
{
    memset(od,0,sizeof(od));
    memset(nw,0,sizeof(nw));
    memset(cnt,0,sizeof(cnt));
    for(int i=1;i<=m;i++)
        nw[b[i]][p[i]]++;
    int sum=0;
    for(int j=n;j>=1;j--)
    {
        int cur=r;
        for(int i=1;i<=c;i++)
        {
            if(nw[i][j]>=min(cur,r-cnt[i]))
            {
                int t=min(cur,r-cnt[i]);
                cur-=t;
                nw[i][j]-=t;
                cnt[i]+=t;
            }
            else
            {
                cur-=nw[i][j];
                cnt[i]+=nw[i][j];
                nw[i][j]=0;
            }
        }
        for(int i=1;i<=c;i++)
        {
            if(od[i][j]>=min(cur,r-cnt[i]))
            {
                int t=min(cur,r-cnt[i]);
                cur-=t;
                od[i][j]-=t;
                cnt[i]+=t;
            }
            else
            {
                cur-=od[i][j];
                cnt[i]+=od[i][j];
                od[i][j]=0;
            }
        }
        for(int i=1;i<=c;i++)
            sum+=nw[i][j];
        for(int i=1;i<=c;i++)
            od[i][j-1]=od[i][j]+nw[i][j];
    }
    for(int i=1;i<=c;i++)
        if(od[i][0])return make_pair(0,sum);
    return make_pair(1,sum);
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int ca=1;ca<=T;ca++)
    {
        int n,c,m;
        scanf("%d%d%d",&n,&c,&m);
        for(int i=1;i<=m;i++)
            scanf("%d%d",&p[i],&b[i]);
        int tl=1,tr=n*m;
        while(tl<tr)
        {
            int tm=(tl+tr)/2;
            pair<int,int> tmp=check(n,m,c,tm);
            if(tmp.first)tr=tm;
            else tl=tm+1;
        }
        printf("Case #%d: %d %d\n",ca,tl,check(n,m,c,tl).second);
    }
    return 0;
}
