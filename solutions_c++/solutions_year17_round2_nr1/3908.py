# include <bits/stdc++.h>
# define s(x) scanf("%d",&x)
# define l(x) scanf("%lld",&x)
using namespace std;
#define pb push_back
#define mp make_pair
#define ll long long
#define ms(a,b) memset((a),(b),sizeof(a))
#define inf 1000000007
#define f(i,n) for(i=0;i<n;i++)
#define fa(i,a,b) for(i=a;i<b;++i)
#define p(x) printf("%d ",x)
#define pl(x) printf("%lld ", x)
#define pf(x) printf("%lf ", x)
#define pn() printf("\n")
#define pt() printf("test \n")
#define ps(m) printf("%s\n",m)
# define vi vector<ll>
# define vpi vector<pair<ll,ll> >
# define yes 100005
ll n,m,k;
bool comp(pair<double,double> p,pair<double,double>q)
{
    return p.first<q.first;
}
int main()
{
    ll q,r,i,j,y,ans,v;
     freopen("a.txt","w",stdout);
    cin>>v;
    double t,u,d,p,x,num1,num2;
    fa(y,1,v+1)
    {
        cin>>d>>n;
        vector<pair<double,double> > a;
        f(i,n)
        {
            cin>>num1>>num2;
            a.pb(mp(num1,num2));
        }
        sort(a.begin(),a.end(),comp);
        p=(d-a[n-1].first)/a[n-1].second;
        for(i=n-2;i>=0;i--)
        {
            x=(d-a[i].first)/a[i].second;
            if(x>p)
                p=x;
        }
        printf("Case #%lld: ",y);
        printf("%llf",(d/p));
        pn();
    }
    return 0;
}

