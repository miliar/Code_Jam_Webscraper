#include <bits/stdc++.h>
using namespace std;

//type helpers
#define ll long long
#define vi vector <int>
#define vl vector <ll> 
#define pii pair<int, int>
#define pll pair<ll, ll>
#define vpii vector <pii >
#define vpll vector <pll >
//debugging
#define debug(x) cout<<"debugging "<<x<<endl

//loops
#define FOR(i,a,b) for(ll i=a;i<b;i++)
#define FORD(i,a,b) for(ll i=a-1;i>=b;i--)
#define iter(it, s) for(auto it=s.begin(); it!=s.end(); it++)

//io helpers
#define sd(n) scanf("%d", &n)
#define sl(n) scanf("%lld", &n)
#define slf(n) scanf("%lf", &n) 
#define pd(n) printf("%d", n)
#define pl(n) printf("%lld", n)
#define plf(n) printf("%0.9lf", n)
#define ps printf(" ")
#define pn printf("\n")


//ds helpers
#define f first
#define s second
#define pb push_back
#define pob pop_back
#define mp make_pair
#define sz(n) (ll)n.size()


//fast input and output when using cin,cout
#define fast ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0)
//some constants
const int INF = 1<<29;
#define MOD 1000000007
#define PI 3.14159265358979323846
#define EPS 0.0000000001
#define max_size 100005

//some helper functions
inline bool EQ(long double a, long double b) { return fabs(a-b) < 1e-9;}
inline ll lcm(ll a,ll b){ return (a*b)/(__gcd(a,b));}
#define mod(a) ((a)%MOD)
inline ll ciel(long double a) { ll ret = a; if(a-ret>EPS) ret++; return ret; }
inline ll powf(ll n, ll p) {if(p==0)return 1; if(n<=1)return n;ll res = 1;while(p){if(p&1) res = mod(res*n);n = mod(n*n);p /= 2;} return res;}
inline bool ispoweroftwo(ll x){return (x && !(x&(x-1)));}
const int N= 1000000;
long double K[N],S[N],d;
ll n;
bool valid(long double speed ){
	long double t = d*(long double)1.0000000/speed;
	for(int i=0;i<n;i++){
		if((long double)K[i] + S[i]*t < (long double)d) return false;
	}
	return true;
}


int main(int argc, char const *argv[])
{
	/* code */
	cout<<std::fixed << setprecision(10);
	int cases;
	cin>>cases;
	for(int ii=1;ii<=cases;ii++){
		cin>>d;sl(n);
		for (int i=0;i<n;i++) cin >> K[i] >> S[i];
		long double start=0.0000000000 ,end = (long double)d*(long double)1.0000000000;
		while(start<=end-EPS){
			long double mid  = (start+end)/(long double)2.0000000;
			if(valid(mid)) start = mid;
			else end=  mid;
		}
		cout << "Case #" << ii << ": " <<  start << endl;
	}
	return 0;
}