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
#define MOD 999999999999999989
#define oo 1e12
#define N 100005
#define cot 21
#define itm1 fst
#define EPS 1e-3
#define itm2 snd.fst
#define itm3 snd.snd
#define FILES 1
#define min INT_MIN
#define d 28
typedef long long ll;
typedef pair<ll,ll> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<ll> vll;
typedef pair<ll,ii> tri;
typedef vector<tri> vt;
typedef pair<double, int> pi;
	string s;
inline void change(ll pos,ll k){
	REP(i,pos,pos+k){
		if(s[i] == '+') s[i] = '-';
		else s[i] ='+';
	}
}
int main() { ll n; cin>>n;
REP(is,0,n){
 cin>>s;
	ll k; ll gg=0,ez=1; cin >> k;
	REP(i,0,s.size()){
		if(s[i] == '-' && i+k <= s.size()){
			change(i,k); gg++;
		}
	}
	REP(i,0,s.size()){
		if(s[i] == '-'){
			ez--; break;
		}
	}
	cout << "Case #" << is+1 << ": ";
	if(ez) cout << gg << endl;
	else cout << "IMPOSSIBLE" << endl;
}
	// your code goes here
	return 0;
}
