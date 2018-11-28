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
ll n,m;

int main()
{
    ll t,i,j,k,x,ans;
     freopen("c.txt","w",stdout);
    cin>>t;
    string a;
    fa(x,1,t+1)
    {
        cin>>a>>k;
        n=a.size();
        ans=0;
        f(i,n-k+1)
        {
            if(a[i]=='+')
                continue;
            ans++;
            fa(j,i,i+k)
            {
                if(a[j]=='+')
                    a[j]='-';
                else
                    a[j]='+';
            }
        }
        cout<<"Case #"<<x<<": ";
        fa(j,i,n)
        {
            if(a[j]=='-')
            {
                cout<<"IMPOSSIBLE\n";
                break;
            }
        }
        if(j==n)
        {
            cout<<ans<<endl;
        }
        a.clear();
    }
    return 0;
}
