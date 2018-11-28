#include<bits/stdc++.h>
using namespace std;
int a[10100],b[10100],getans,T,num;
long long n;
void dfs(int x,int f)
{
   // cout<<x<<" "<<f<<endl;
    if (x==0)
    {
        getans=1;
        return ;
    }
    // cout<<x<<" "<<a[x]<<" "<<b[x+1]<<" "<<f<<endl;
    if (f==0)
    {
        for (int i=a[x]; i>=b[x+1]; i--)
        {
            if(!getans)
            {
                b[x]=i;
                //for (int ii=1;ii<=num;ii++) cout<<b[ii];cout<<"  "<<x<<endl;
                dfs(x-1,b[x]!=a[x]);
            }
        }
    }
    else
    {
        for (int i=9; i>=b[x+1]; i--)
        {
            if (!getans)
            {
                b[x]=i;
                dfs(x-1,1);
            }
        }
    }
    return ;
}
int main()
{
    freopen("B.out","w",stdout);
    scanf("%d",&T);
    for (int cas=1; cas<=T; cas++)
    {
        scanf("%lld",&n);
        getans=0;
        num=0;
        while (n)
        {
            a[++num]=n%10;
            n/=10;
        }
        memset(b,0,sizeof(b));
        dfs(num,0);
        printf("Case #%d: ",cas);
        //cout<<num<<endl;
          while (num && b[num]==0) num--;
        for (int i=num; i>0; i--) printf("%d",b[i]);
        printf("\n");
    }
    return 0;
}
