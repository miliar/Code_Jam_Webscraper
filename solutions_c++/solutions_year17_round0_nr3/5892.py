#include<bits/stdc++.h>
using namespace std;

typedef long long int ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector< pair<int,int> > vpii;
typedef vector< pair<ll,ll> > vpll;
typedef vector< vector<int> > matrix;

#define SET(Ar,val) memset(Ar,val,sizeof(Ar))
#define rep(i,val,n)  for(int i=val;i<n;i++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define LMAX LONG_LONG_MAX
#define LMIN LONG_LONG_MIN
#define IMAX INT_MAX
#define IMIN INT_MIN
#define M 1000000007

/*--------------------------------------------------------------------------------------------------------------------------------*/

template <class T> T modpower(T a,T b,T MOD)
{
    T ans=1;
    while(b!=0)
    {
        if(b%2==1)
        ans=(ans*a)%MOD;
        a=(a*a)%MOD;
        b/=2;
    }
    return ans;
}

vector< pair< int,pair<int,int> > > V;

void init()
{
    int t;
    cin >> t;
    rep(ca,1,t+1)
    {
        int n,k;
        cin >> n >> k ;
        int ar[n+5];
        rep(i,0,n+4)
        ar[i]=0;
        ar[0]=1;
        ar[n+1]=1;
        rep(j,1,k+1)
        {
            rep(i,1,n+1)
            {
                if(ar[i]==0)
                {
                    int u=i-1,v=i+1,l=0,r=0;
                    while(ar[u]!=1)
                    {
                        u--;
                        l++;
                    }
                    while(ar[v]!=1)
                    {
                        v++;
                        r++;
                    }
                    int a1=min(l,r),a2=max(l,r);
                    V.pb({a1,{a2,i}});
                }
            }
            //vector< pair< int,pair<int,int> > > X;
            sort(V.rbegin(),V.rend());
            ar[V[0].se.se]=1;
            if(j==k)
            cout << "Case #" << ca << ": " << max(V[0].fi,V[0].se.fi) << " " << min(V[0].fi,V[0].se.fi) << endl ;
            V.clear();
        }
    }
}

int main()
{
    clock_t time1 = clock();
	#ifndef ONLINE_JUDGE
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("C-small-1-attempt0.out","w",stdout);
	#else
	//ONLINE_JUDGE
	#endif
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
    init();
    clock_t time2 = clock();
    cerr <<"Time: " <<(double)(time2-time1)/CLOCKS_PER_SEC <<" seconds" <<endl;
	return 0;
}
