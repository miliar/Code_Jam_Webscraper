#include<bits/stdc++.h>
using namespace std;

//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);
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
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.in","w",stdout);
    int t,n,i;
    double d,x,y,ti,m;
    sd(t);
    int p=0;
    while(t--)
    {
        p++;
        m=0.0;
        cin>>d;
        sd(n);
        for(i=0;i<n;i++)
        {
            cin>>x;
            cin>>y;
            ti=(d-x)/y;
            m=max(ti,m);
        }
        cout<<"Case #"<<p<<": ";
        printf("%0.8f\n",d/m);

    }
}
