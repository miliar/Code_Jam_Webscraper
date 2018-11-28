#include <bits/stdc++.h>

using namespace std;
	
	
typedef long long unsigned llu;
typedef long long int ll;
typedef long ld;
typedef unsigned int ui;

#define SI(n) scanf("%d",&n)
#define SF(n) scanf("%ld",&n)
#define SLL(n) scanf("%lld",&n)
#define PI(n) printf("%d",n)
#define PF(n) printf("%ld",n)
#define PLL(n) printf("%lld",n)

#define rr      freopen("B.in", "r", stdin)
#define wr      freopen("BO.txt", "w", stdout)

#define all(a)  a.begin(), a.end()
#define setbitcount(n) __builtin_popcount(n)
#define trailzerobitc(n) __builtin_ctz(n)

#define pi 		M_PI
#define ESP 	(1e-9)
#define DREP(a)         sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(a,ind)      (lower_bound(all(a),ind)-a.begin())

#define REP(i,n)        for(int i=0;i<(n);++i)
#define FOR(i,a,b)      for(int i=(a);i<=(b);++i)
#define FORD(i,a,b)     for(int i=(a);i>=(b);--i)

#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#define trace1(x) cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl;
#define trace2(x,y) cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl;
#define justp(x,y) cout << "x : " << x << " " << "y : " << y << endl; 

#define MOD 		1000000007
#define MAX 	    100000
#define ff 			first
#define ss 			second 
#define clr 		clear()
#define square(x) ((x)*(x))
#define pb 			push_back
#define mp 			make_pair
#define gcd(a,b)  	__gcd(a,b)
#define sz(a) 		((int)(a.size()))
#define len(a) 		((int)a.length())
#define mem(i,n) 	memset(i,n,sizeof(i))
#define IOS 		ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
#define IN          int t; cin >> t; while(t--)
#define CJIN		int t; cin >> t;for(int tc = 1 ; tc<=t ; ++tc)
#define CJOP(ans)	cout << "Case #" << tc << ": " << ans << '\n';    

int main()
{
    rr;
    wr;
    IOS;
    CJIN
    {
    	string s;
    	cin >> s;
    	int idx,l;
    	l = s.length();
    	bool st = true;
    	REP(i, l-1)
    	{
    		if(s[i] > s[i + 1])
    		{
    			idx = i;
    			st = false;
    			break;
    		}
    	}
    
    	if(!st)
    	{
    		s[idx]--;
    		FOR(i, idx + 1, l - 1)
    		s[i] = '9';
    		FORD(i, idx - 1, 0)
    		{
    			if(s[i] > s[i + 1])
    			{
    				s[i]--;
    				s[i + 1] = '9';
    			}
    		}
    		string ans = "";
    		REP(i,l)
    		if(s[i] != '0') ans += s[i];
    		CJOP(ans);
    	}
    	else
    	CJOP(s);
    }
    return 0;    
}
