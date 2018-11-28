#include <bits/stdc++.h>
#include <sstream>
using namespace std;
#define fastio ios_base::sync_with_stdio(0);cin.tie(0);
#define clr(a,v) memset(a, v, sizeof(a))
#define trace(x) cerr << #x << ": " << x << '\n'
#define trace2(x,y) cerr << #x << ": " << x << " | " << #y << ": " << y << '\n';
#define trace3(x,y,z) cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << '\n';
#define all(v) (v).begin(),(v).end()
#define pb push_back
#define sz(v) ((int)v.size())
#define REP(i,x,y) for(long long (i)=(x);(i)<(y);(i)++)
#define RREP(i,x,y) for(long long (i)=(x);(i)>=(y);(i)--)
#define REPIT(it,A) for(typeof(A.begin()) it = (A.begin()); it!=A.end();it++)
//#define mp make_pair
#define mt(x,y,z) mp((x),mp((y),(z)))
#define fst first
#define snd second
#define ones(x) __builtin_popcountll(x)
#define gcd __gcd
#define MOD 1000000007
#define oo 1e12
#define N 100005
#define cot 21
#define itm1 fst
#define EPS 1e-3
#define itm2 snd.fst
#define itm3 snd.snd
#define FILES 1
#define min INT_MIN
typedef long long ll;
//typedef int ll;
typedef pair<ll,ll> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<ll> vll;
typedef pair<ll,ii> tri;
typedef vector<tri> vt;
typedef pair<double, int> pi;
ll ar[N];
ll bp(ll a, ll n){
	if(n==0) return 1;
	if(n%2==1) return a*bp(a,n-1);
	if(n%2==0) {
		ll x=bp(a,n/2);
		return x*x;
	}
}

inline void make(ll ta, ll ar[]){
	ll pos=ta;
	REP(i,0,ta-1){
		if(ar[ta-1-i]>ar[ta-i-2]){
			ar[ta-1-i]--; pos=i+1;
			break;
		}
	}
	for(int i=pos;i<ta;i++){
		ar[ta-1-i]=9;
	}
}
ll ok(ll ta, ll ar[]){
	REP(i,0,ta){
		if(ar[ta-1-i]>ar[ta-i-2]) return 1;
	}
	return 2;
}
int main() {fastio;
	ll t; cin>>t;
	REP(asd,0,t){
		ll x; cin>>x; ll val=x,ta;
		REP(i,0,20){
			ar[i]=val%10;
			val=(val-ar[i])/10;
			if(val==0) { ta=i;break;}
		} ta++;
		//make(ta,ar);
		//REP(i,0,ta) cout<<ar[i]<<endl;
		for(int i=0;i<20;i++){
			make(ta,ar);
		//	REP(i,0,ta) cout<<ar[i]<<endl;
			if(ok(ta,ar)==2) break;
		}
		ll ans=0;
			REP(i,0,ta) ans+=ar[i]*bp(10,i);
			cout<<"Case #"<<asd+1<<":"<<" "<<ans<<endl;
		//cout<<" .-. "<<endl;
	memset(ar,0,sizeof(ar));
		
	}
	// your code goes here
	return 0;
}
