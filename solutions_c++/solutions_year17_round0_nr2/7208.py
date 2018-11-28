#include<bits/stdc++.h>

#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define len(s) s.length()
#define forp(i,a,b) for( i=a;i<=b;i++)
#define rep(i,n)    for( i=0;i<n;i++)
#define ren(i,n)    for( i=n-1;i>=0;i--)
#define forn(i,a,b) for( i=a;i>=b;i--)
#define all(v) v.begin(),v.end()
#define b(v) v.begin()
#define e(v) v.end()
#define mem(n,m) memset(n,m,sizeof(n))
#define lb lower_bound
#define ub upper_bound
#define pii pair<int,int>
#define pll pair<long long,long long>
#define vii vector<int>
#define vll vector<long long>
#define gl(cin,s)  getline(cin,s);
#define bitc(n) __builtin_popcountll(n)
#define present(s,x) (s.find(x) != s.end()) 
#define cpresent(s,x) (find(all(s),x) != s.end()) 
#define tr(container, it) for(__typeof(container.begin()) it = container.begin(); it != container.end(); it++) 

#define boost ios_base::sync_with_stdio(0)
#define MOD 1000000007
#define EPSILON 1e-9
#define PI 3.14159265358979323846
#define SIZE 100001

typedef long long  ll;
typedef unsigned long long ull;
typedef long double  ldo;
typedef double  db ;
using namespace std;
vector<int> v;
int dp[21][10][2];
int f(int pos,int last,bool is)
{
	if(pos==v.size()-1){
		int fans=0;
		for(int i=last;i<=(is?v[pos]:9);i++){
			fans++;
		}
		return fans;
	}
	if(dp[pos][last][is]!=-1)
	return dp[pos][last][is];
	int fans=0;
	for(int i=last;i<=(is?v[pos]:9);i++){
		fans += f(pos+1,i,(is?(i==v[pos]?true:false):is));
	}
	dp[pos][last][is]=fans;
	return fans;
}
int func(long long x)
{
	v.clear();
	while(x){
		v.pb(x%10);
		x/=10;
	}
	reverse(all(v));
	mem(dp,-1);
	return f(0,0,true);
}
int main()
{  	
	/* #ifndef ONLINE_JUDGE
	freopen(fi, "r", stdin);
	#endif */
	freopen("route.in","r",stdin);
	freopen("route2.out","w",stdout);
	//cin.ignore();
	//cin.clear();
	boost;
	//cin.tie(0);
	int T;
	long long n;
	cin>>T;
	for(int tt=1;tt<=T;tt++){
		cin>>n;
		long long lo = 1,hi = n;
		int val = func(n);
		while(lo<hi){
			long long mid = (lo+hi)>>1;
			int temp = func(mid);
			if(temp < val){
				lo = mid+1;
			}
			else{
				hi = mid;
			}
		}
		cout<<"Case #"<<tt<<": ";
		cout<<lo<<endl;
	}
	return 0;
}
