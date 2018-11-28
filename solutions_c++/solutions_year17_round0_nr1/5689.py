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

void init()
{
    int t;
    cin >>  t ;
    rep(ca,1,t+1)
    {
        string s;
        int k;
        cin >> s >> k;
        int l=s.size();
        if(k>l)
        {
            int fg=0;
            rep(i,0,l)
            {
                if(s[i]=='-')
                {
                    fg=1;
                    break;
                }
            }
            if(fg)
            cout << "Case #" << ca << ": " << "IMPOSSIBLE\n";
            else
            cout << "Case #" << ca << ": " << "0\n";
        }
        else
        {
            int cnt=0,fg=0;
            rep(i,0,l-k+1)
            {
                if(s[i]=='-')
                {
                    cnt++;
                    rep(j,i,i+k)
                    {
                        if(s[j]=='-')
                        s[j]='+';
                        else
                        s[j]='-';
                    }
                }
            }
            rep(i,l-k+1,l)
            {
                if(s[i]=='-')
                {
                    fg=1;
                    break;
                }
            }
            if(fg)
            cout << "Case #" << ca << ": " << "IMPOSSIBLE\n";
            else
            cout << "Case #" << ca << ": " << cnt << "\n";
        }
    }
}

int main()
{
    clock_t time1 = clock();
	#ifndef ONLINE_JUDGE
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
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
