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
int cnt=0,fl=0,a2,a3=-1000000,ans=0,l,r, t, len, r2, l2;
set<pair<int, pair<int, int>>>mySet;
set<pair<int, pair<int, int>>>::iterator it;
main()
{
    in;out;
//    ios_base::sync_with_stdio(0);
	cin >> t;
	cnt = 1;
	while (t-- > 0)
	{
    	cout << "Case #" << cnt << ": ";
    	++cnt;
    	cin >> n >> k;
    	mySet.clear();
    	mySet.insert(MP(n * -1, MP(1, n)));
    	while (k-- > 0)
    	{
    		it = mySet.begin();
    		len = it->fi * -1;
    		l = it->se.fi;
    		r = it->se.se;
    		mySet.erase(it);
    		//cout << len << " " << l << " " << r << endl;
    		--len;
    		a = len / 2;
    		b = len - a;
    		r2 = l + a - 1;
    		l2 = r - b + 1;
    		if (a)
    			mySet.insert(MP(a * -1, MP(l, r2)));
    		if (b)
    			mySet.insert(MP(b * -1, MP(l2, r)));
    	}
    	swap(a, b);
    	cout << a << " " << b << endl;
	}
    return 0;
}
