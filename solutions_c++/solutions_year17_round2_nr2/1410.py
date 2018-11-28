#include<bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define ll long long
#define mp make_pair
#define MAX 100005
#define inf 1e18
#define mod 1000000007
#define pb push_back
#define INF 1000005
#define pii pair<ll,ll>

//ll a[MAX];

/*ll gcd(ll a, ll b)
{
    if (a == 0)
        return b;
    return gcd(b%a, a);
}*/

//pii a[MAX];

char sol(int n)
{
    if(n==0)
        return 'R';
    if(n==1)
        return 'B';
    if(n==2)
        return 'Y';
}
int main()
{
    freopen ("B-small.in","r",stdin);
    freopen ("beta.txt","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n,t,r,o,y,g,b,v;
    cin>>t;


    for(int k=1;k<=t;k++)
    {
        cout<<"Case #"<<k<<": ";
        cin>>n>>r>>o>>y>>g>>b>>v;

        pair<int,int> a[3];
        int i;
        a[0].f=r;
        a[1].f=b;
        a[2].f=y;

        a[0].s=0;
        a[1].s=1;
        a[2].s=2;

        sort(a,a+3);

        if(a[2].f>a[0].f+a[1].f)
        {
            cout<<"IMPOSSIBLE\n";
            continue;
        }

        char ans[n+1];

        for(i=0;i<n;i+=2)
        {
          if(a[2].f>0)
          {
            ans[i]=sol(a[2].s);
            a[2].f--;
          }
          else
            if(a[1].f>0)
            {
                ans[i]=sol(a[1].s);
                a[1].f--;
            }
            else
            {
                ans[i]=sol(a[0].s);
                a[0].f--;
            }
        }
        for(i=1;i<n;i+=2)
        {
          if(a[2].f>0)
          {
            ans[i]=sol(a[2].s);
            a[2].f--;
          }
          else
            if(a[1].f>0)
            {
                ans[i]=sol(a[1].s);
                a[1].f--;
            }
            else
            {
                ans[i]=sol(a[0].s);
                a[0].f--;
            }
        }
        for(i=0;i<n;i++)
            cout<<ans[i];
        cout<<endl;
    }

    return 0;
}
