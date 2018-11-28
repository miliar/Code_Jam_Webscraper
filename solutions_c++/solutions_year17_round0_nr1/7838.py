#include <bits/stdc++.h>

using namespace std;
	
typedef long long unsigned llu;
typedef long long lld;
typedef long ld;

#define REP(i,n)        for(int i=0;i<(n);++i)
#define FOR(i,a,b)      for(int i=(a);i<=(b);++i)
#define FORD(i,a,b)     for(int i=(a);i>=(b);--i)

#define rr 		freopen("A.in", "r", stdin)
#define wr 		freopen("A.txt", "w", stdout)

#define MOD 	1000000007
#define INF 	1LL<<57LL
#define MAX 	1000000
#define pi 		M_PI
#define ESP 	(1e-9)

#define ff 			first
#define ss 			second
#define clr 		clear()
#define square(x) ((x)*(x))
#define pb 			push_back
#define mp 			make_pair
#define gcd(a,b)  	__gcd(a,b)
#define sz(a) 		((int)(a.size()))
#define len(a) 		((int)a.length())
#define all(vi) 	vi.begin(), vi.end()
#define mem(i,n) 	memset(i,n,sizeof(i))
#define IOS 		ios_base::sync_with_stdio(false); cin.tie(NULL);
#define IN          int t; cin >> t; while(t--)
#define CJIN		int t; cin >> t;for(int tc = 1 ; tc<=t ; ++tc)
#define CJOP(ans)	cout << "Case #" << tc << ": " << ans << '\n';    


string s;
int l, k;

int lasti()
{
	FORD(i, l-1, 0)if(s[i]=='-')return i;
	return 0;
}

bool flip(int p)
{
	if(p-k+1 < 0)return false;
	for(int i = p; i >= p-k+1; --i)
	{
		if(s[i]=='-')s[i]='+';
		else if(s[i]=='+')s[i]='-';
	}
	return true;
}

int strchk()
{
	REP(i,l)if(s[i]=='-')return 0;
	return 1;
}

int main()
{
	rr;
	wr;
    int ans;
    CJIN
    {
		cin >> s >> k;
		l = s.length();
		ans = 0;
		bool k = true;
		while(!strchk())
		{
			k = flip(lasti());
			if(!k)break;
			ans++;
		}
		if(k)
		{CJOP(ans);}
		else
		{CJOP("IMPOSSIBLE");}
	}
    return 0;    
}
