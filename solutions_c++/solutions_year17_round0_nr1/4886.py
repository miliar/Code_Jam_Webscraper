#include<bits/stdc++.h>
#define in freopen("input.txt","r",stdin)
#define out freopen("output.txt","w",stdout)

#define inp freopen(".in","r",stdin)
#define outp freopen(".out","w",stdout)

using namespace std;

#define pb push_back
#define pf push_front
#define p_f pop_front
#define p_b pop_back
#define LL long long int
#define LD long double
#define MP make_pair
#define sqr(x) (x*x)
#define nwl pr("\n")
#define fi first
#define dist(x,y,xx,yy) sqrt( (x-xx)*(x-xx)+(y-yy)*(y-yy) )
#define lenint int intsi(int x){ int cnt=0; while(x>0){cnt++;x/=10;} return (cnt); }
#define se second
#define all(v) v.begin(),v.end()
#define sc scanf
#define DEBUG(a) cout<<#a<<" -> "<<a<<endl;
#define pr printf
#define si size()
#define str strlen
#define time clock()/(double)CLOCKS_PER_SEC
#define gcd LL GCD(LL a,LL b){ if(b==0)return a;else return GCD(b,a%b); }
const int INF=(-1u)/2;
const long long int INF2=(-1ull)/2;
int a,b,c[100010],d[100010],i,j,k,n,m,timer=0,x,y;
int cnt=0,fl=0,a2,a3=-1000000,ans=0,l,r, t;
string s;
void invert(char& a)
{
	if (a == '+')
		a = '-';
	else 
		a = '+';
}
main()
{
    in;out;
//    ios_base::sync_with_stdio(0);
    cin>>t;
    cnt = 1;
    while(t-- > 0)
    {
    	cin >> s >> k;
    	n = s.length();
    	ans = 0;
    	cout << "Case #" << cnt << ": ";
    	++cnt;
    	for(i = 0; i + k <= n; ++i)
    	{
    		if (s[i] == '-')
    		{
    			++ans;
    			for (j = i; j < i+k; ++j)
    				invert(s[j]);
    		}
    	}
    	fl = 0;
    	for (int i = 0; i < n; ++i)
    	{
    		if (s[i] == '-')
    		{
    			fl = 1;
    			cout << "IMPOSSIBLE\n";
    			break;
    		}
    	}
    	if (!fl)
    		cout << ans << endl;
    }
    return 0;
}
