#include<bits/stdc++.h>

using namespace std;

typedef pair<double,double>   II;
typedef vector< II >      VII;
typedef vector<int>     VI;
typedef vector< VI > 	VVI;
typedef long long int 	ll;

#define M 100005
#define mod 1000000007
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(a) (int)(a.size())
#define ALL(a) a.begin(),a.end()
#define forn(i, n) for(int i = 0; i < int(n); ++i)
#define forv(i, n) for(int i = 0; i != int(n); ++i)
#define cases int t;  cin>>t;   while(t--)
#define check(a,n) forn(i,int(n)) cout<<int(a[i])<<" "; cout<<endl
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

int main()
{
    fast_io;
    freopen("A-large.in","r",stdin);
    freopen("output.in","w",stdout);
    int t;
    cin>>t;
    forn(ca,t)
    {
        double r,h,sum=0,ans=0,pi=acos(-1);
        VII v,u;
        int n,k;
        cin>>n>>k;
        forn(i,n)
            cin>>r>>h,v.PB(MP(r*h,r)),u.PB(MP(r,h));
        sort(ALL(v));
        sort(ALL(u));
        for(int i=n;i>=k;i--)
        {
            double maxr=u[i-1].F,maxh=u[i-1].S;
            int k1=k-1,flag=0;
            sum=maxr*maxh;
            for(int j=n;j--;)
            {
                if(k1==0)
                    break;
                if(v[j].F==maxr*maxh&&v[j].S==maxr&&!flag)
                {
                    flag=1;
                    continue;
                }
                sum+=v[j].F;
                k1--;
            }
           // cout<<maxr<<" "<<sum<<endl;
            double area=sum*2*pi+pi*maxr*maxr;
            ans=max(ans,area);
        }
        cout<<"Case #"<<ca+1<<": ";
        cout<<setprecision(8)<<fixed<<ans<<"\n";
    }
    return 0;
}
