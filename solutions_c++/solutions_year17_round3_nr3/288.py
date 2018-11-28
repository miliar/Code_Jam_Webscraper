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

ld eps=1e-13;

int main()
{ios_base::sync_with_stdio(false);
freopen("input.txt","r",stdin);
freopen("output.txt","w",stdout);
int t,t1=0;
gl(t);
while(t--)
{
	t1++;
	ol("Case #");ol(t1);ol(": ");
	int n,k;
	cin>>n>>k;
	ld a[55],u;
	cin>>u;
	rep(i,0,n-1)cin>>a[i];
	while(1)
	{
		//ol(u);on;
		if(u<eps)break;
		sort(a,a+n);
		if(a[0]>1-eps)break;
		if(fabs(a[0]-a[n-1])<eps)
		{
			rep(i,0,n-1)
			{
				ld x=n;
				a[i]+=u/x;
			}
			break;
		}
		rep(i,1,n-1)
		{
			if(a[0]<a[i])
			{
				ld x=i;
				ld y=min(u,(a[i]-a[0])*i);
				x=y/x;
				rep(j,0,i-1)
				a[j]+=x;
				u-=y;
				break;
			}
		}
		/*rep(i,0,n-1)
		{
			ol(a[i]);os;
		}
		on;*/
	}
	ld ans=1;
	rep(i,0,n-1)ans*=a[i];
	cout<<fixed<<setprecision(10)<<ans<<"\n";
}
return 0;
}


