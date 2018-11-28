//#345 div.1 D 上升子序列（离线操作）
#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
#include<set>
#include<queue>
#define maxn 400009
#define inf 0x3f3f3f3f
#define mod 1000000007
#define Mat_size 11
using namespace std;
struct ee
{
    int p,v,k;
}que[maxn];
int l[maxn],r[maxn],a[maxn],t[maxn],n,m,cal[maxn],ans[maxn],ll[maxn],rr[maxn];
bool f[maxn];

bool cmp(ee a,ee b)
{
    return a.p<b.p;
}

int main()
{
    freopen("d:\\in.txt","r",stdin);
    memset(ans,0,sizeof(ans));
    memset(cal,0,sizeof(cal));
    scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)
       scanf("%d",&a[i]);
    for(int i=1;i<=m;i++)
    {
        scanf("%d%d",&que[i].p,&que[i].v);
        que[i].k=i;
    }
    sort(que+1,que+m+1,cmp);
    fill(t,t+n+3,2e9+9);
    int j=1;
    for(int i=1;i<=n;i++)
    {
        while(j<=m&&que[j].p<=i)
        {
            l[j]=lower_bound(t,t+n+3,que[j].v)-t;
            j++;
        }
        ll[i]=lower_bound(t,t+n+3,a[i])-t;
        t[lower_bound(t,t+n+3,a[i])-t]=a[i];
    }
    int len=lower_bound(t,t+n+3,2e9+9)-t;
    //printf("%d\n",len);
    fill(t,t+n+3,2e9+9);
    j=m;
    for(int i=n;i>=1;i--)
    {
        while(j>=1&&que[j].p>=i)
        {
            ans[que[j].k]=lower_bound(t,t+n+3,-que[j].v)-t+1+l[j];
            //printf("%d %d %d\n",l[j],lower_bound(t,t+n+3,-que[j].v)-t,que[j].k);
            j--;
        }
        rr[i]=lower_bound(t,t+n+1,-a[i])-t;
        t[lower_bound(t,t+n+1,-a[i])-t]=-a[i];
        //printf("%d %d %d\n",ll[i],rr[i],i);
        if(ll[i]+rr[i]+1==len)
        {
            if(cal[ll[i]+1]==0)
                cal[ll[i]+1]=i;
            else
                cal[ll[i]+1]=-1;
        }
    }
    for(int i=1;i<=n;i++)
    {
        if(cal[i]>0)
        {
            f[cal[i]]=true;
            //printf("import i=%d %d\n",i,cal[i]);
        }
    }
    for(int i=1;i<=m;i++)
    {
        if(f[que[i].p])
        {
            ans[que[i].k]=max(ans[que[i].k],len-1);
        }
        else
        {
            ans[que[i].k]=max(ans[que[i].k],len);
        }
    }
    for(int i=1;i<=m;i++)
        printf("%d\n",ans[i]);
    return 0;
}