#include<iostream>
#include<algorithm>
#include<vector>
#include<queue>
#include<map>
#include<utility>
#include<set>
#include<stack>
#include<list>
#include<deque>
#include<bitset>
#include<iomanip>
#include<cstring>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<climits>
#include<cmath>
#include<cctype>


#define pb push_back
#define mp make_pair
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define ren(i,a,b) for(int i=a;i>=b;i--)
#define ff first
#define ss second
#define pll pair<long long int,long long int>
#define pii pair<int,int>
#define vll vector<long long int>
#define vii vector<int>
#define gi(n) scanf("%d",&n)
#define gll(n) scanf("%lld",&n)
#define gstr(n) scanf("%s",n)
#define gl(n) cin >> n
#define oi(n) printf("%d",n)
#define oll(n) printf("%lld",n)
#define ostr(n) printf("%s",n)
#define ol(n) cout << n
#define os cout<<" "
#define on cout<<"\n"
#define o2(a,b) cout<<a<<" "<<b
#define all(n) n.begin(),n.end()
#define present(s,x) (s.find(x) != s.end())
#define cpresent(s,x) (find(all(s),x) != s.end())
#define tr(container, it) for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++)
using namespace std;

typedef unsigned long long int ull;
typedef long long int ll;
typedef long double ld;
typedef vector<vector<ll> > mat;



int main()
{ios_base::sync_with_stdio(false);
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int t,t1=0;
gl(t);
while(t--)
{
	t1++;
	long double pi=acos(-1);
	ol("Case #");ol(t1);ol(": ");
	int n,k;
	cin>>n>>k;
	pair<ld,ld> p[1005];
	rep(i,0,n-1)
	{
		int a,b;
		cin>>a>>b;
		p[i].ff=a;p[i].ss=b;
	}
	ld ans=0;
	sort(p,p+n);
	ren(i,n-1,0)
	{
		ld s=pi*p[i].ff*p[i].ff+2*pi*p[i].ss*p[i].ff;
		vector<ld> v;
		ren(j,i-1,0)
		{
			v.pb(2*pi*p[j].ff*p[j].ss);
		}
		sort(all(v));
		//o2(v.size(),k-1);on;
		if(v.size()>=k-1)
		{
			reverse(all(v));
			rep(j,0,k-2)s+=v[j];
			ans=max(ans,s);
		}
		
	}
	cout<<fixed<<setprecision(10)<<ans<<"\n";
	
}
return 0;
}


