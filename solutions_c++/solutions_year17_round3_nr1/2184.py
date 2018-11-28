#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>

#define INF 2000000000
#define INF_LL 2000000000000000000ll
#define MOD_7 1000000007
#define MOD_9 1000000009

typedef long long ll;

using namespace std;

void rec(int r[], int h[], int n, int k, int inc, int i, double pi, double total, double* ans)
{
    if(inc==k)
    {
        if(total>(*ans))
        *ans=total;
        return;
    }

    double csa, lid, tsa;
    for(int j=i;j<n;j++)
    {
        csa=((double)2)*((double)r[j])*((double)h[j])*(pi);
        lid=(pi)*((double)r[j])*((double)r[j]);
        tsa=csa+lid;
        if(total!=0)
        {
            rec(r,h,n,k,inc+1,j+1,pi,total-lid+tsa,ans);
        }
        else
        {
            rec(r,h,n,k,inc+1,j+1,pi,total+tsa,ans);
        }
        //total-=lid;
        //total+=tsa;
        //rec(r,h,n,k,inc+1,j+1,pi,total,ans);
    }
}

void merge1(int r[], int h[], int st, int mid, int end)
{
    int e[end-st+1], f[end-st+1], i=st, j=mid+1, k=0;
    for(;i<=mid&&j<=end;)
    {
        if(r[i]>r[j])
        {
            e[k]=r[i];
            f[k]=h[i];
            k++;
            i++;
        }
        else
        {
            e[k]=r[j];
            f[k]=h[j];
            k++;
            j++;
        }
    }
    while(i<=mid)
    {
        e[k]=r[i];
        f[k]=h[i];
        k++;
        i++;
    }
    while(j<=end)
    {
        e[k]=r[j];
        f[k]=h[j];
        k++;
        j++;
    }
    for(int u=st,kl=0;u<=end;u++,kl++)
    {
        r[u]=e[kl];
        h[u]=f[kl];
    }
}

void msort(int r[], int h[], int st, int end)
{
    if(st<end)
    {
        int mid=st+(end-st)/2;
        msort(r,h,st,mid);
        msort(r,h,mid+1,end);
        merge1(r,h,st,mid,end);
    }
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t,sv,n,k,r[1010],h[1010];
    const double pi=3.14159265;
    double ans;
    scanf("%d",&t);
    sv=t;

    while(t--)
    {
        ans=0.0;
        scanf("%d%d",&n,&k);
        for(int i=0;i<n;i++)
        {
            scanf("%d%d",&r[i],&h[i]);
        }
        msort(r,h,0,n-1);
        /*for(int ip=0;ip<n;ip++)
        {
            cout<<r[ip]<<" "<<h[ip]<<"\n";
        }*/

        rec(r,h,n,k,0,0,pi,0,&ans);

        printf("Case #%d: %lf\n",sv-t,ans);
    }

    return 0;
}
