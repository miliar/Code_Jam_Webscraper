
#include <iostream>
#include<cstring>
#include <cstdio>
#include <algorithm>
#include<queue>
#include<cmath>
#define N 1500
#define M 750000
#define INF 2000000000
using namespace std;
int n,c,m;
int x[N];
int p[N],b[N];
int cnt[N],sum[N];
int main(int argc, const char * argv[])
{
    
    
    freopen("1.txt","r",stdin);
    freopen("1.out","w",stdout);
    int  tt,ans;
    int l,r;
    cin>>tt;
    for(int cas=1;cas<=tt;cas++)
    {
        memset(x,0,sizeof(x));
        memset(cnt,0,sizeof(cnt));
        cin>>n>>c>>m;
        for(int i=1;i<=m;i++)
        {
            cin>>p[i]>>b[i];
            x[p[i]]++;
            cnt[b[i]]++;
        }
        ans=0;
        for(int i=1;i<=c;i++)ans=max(ans,cnt[i]);
        for(int i=1;i<=n;i++)
        {
            sum[i]=sum[i-1]+x[i];
            ans=max(ans,(sum[i]+i-1)/i);
        }
        int tot=0;
        for(int i=1;i<=n;i++)if(x[i]>ans)tot+=x[i]-ans;
        printf("Case #%d: %d %d\n",cas,ans,tot);
    }
    
}
 //2 2 2
// 1 1
//1 2
