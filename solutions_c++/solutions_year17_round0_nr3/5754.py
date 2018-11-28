#include<bits/stdc++.h>
using namespace std;
typedef unsigned long long int ull;
int main()
{
   freopen("c.in","r",stdin);
   freopen("c.txt","w",stdout);
    int t;
    cin>>t;
    int i,j,x,y;
    for(i=1;i<=t;i++)
    {
        ull n,k;
        cin>>n>>k;
        ull arr[n+2];
        ull ls[n+2],rs[n+2],a[n+2],b[n+2];

        memset(arr,0,sizeof(arr));

        arr[0]=1;arr[n+1]=1;ull last=-1;
        for(j=1;j<=k;j++)
        {
            memset(a,-1,sizeof(a));
            memset(b,-1,sizeof(b));
            memset(ls,0,sizeof(rs));
            memset(rs,0,sizeof(rs));
            ull ma=0;ull ma2=0;
            for(y=1;y<=n;y++)
            {
                if(arr[y]==0)
                {
                    for(x=y-1;x>=1;x--)
                    {
                        if(arr[x]==0)
                            ls[y]++;
                        else
                            break;
                    }
                    for(x=y+1;x<=n;x++)
                    {
                        if(arr[x]==0)
                            rs[y]++;
                        else
                            break;
                    }
                    a[y]=min(ls[y],rs[y]);
                    if(ma<=a[y])
                        ma=a[y];
                }
            }
            for(y=1;y<=n;y++)
            {
                if(a[y]==ma)
                {
                    b[y]=max(ls[y],rs[y]);
                    if(ma2<=b[y])
                        ma2=b[y];
                }
            }
            for(y=1;y<=n;y++)
            {
                if(b[y]==ma2)
                {
                    arr[y]=1;
                    last=y;
                    break;
                }
            }
        }
         printf("Case #%d: %llu %llu\n",i,b[last],a[last]);
    }
    return 0;
}
