#include<bits/stdc++.h>
using namespace std;


#define bitcount    __builtin_popcountll
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define mp make_pair
#define F first
#define S second
#define ll long long
#define rep(i,x,y) for(i=x;i<y;i++)
#define pf(x,y) printf("x",y)
#define pb push_back
#define MOD 1000000007
int a[50],b[50];
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.in","w",stdout);
    int t,x,i,j,k,p;
    ll n;
    sd(t);
    x=0;
    while(t--)
    {
        for(i=0;i<50;i++)
        {
            a[i]=0;
            b[i]=0;
        }
        x++;
        slld(n);
        i=0;
        while(n!=0)
        {
            a[i++]=n%10;
            n=n/10;
        }
        for(j=0;j<i;j++)
            b[i-j-1]=a[j];
        for(j=0;j<i-1;j++)
        {
            if(b[j]>b[j+1])
            {
                p=b[j];
                for(k=j;k>=0;k--)
                {
                    if(b[k]==p)
                        continue;
                    else
                        break;
                }
                if(k!=-1)
                {
                    b[k+1]--;
                    for(p=k+2;p<i;p++)
                    {
                        b[p]=9;
                    }
                }
                else
                {
                    b[0]--;
                    for(p=1;p<i;p++)
                        b[p]=9;
                }
                break;
            }
        }
        for(j=0;j<i;j++)
        {
            if(b[j]!=0)
                break;
        }
        cout<<"Case #"<<x<<":"<<" ";
        for(p=j;p<i;p++)
        {
            cout<<b[p];
        }
        cout<<"\n";
    }
    return 0;
}
