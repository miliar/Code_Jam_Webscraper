#include <bits/stdc++.h>
using namespace std;
typedef vector<string> vs;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef pair<pii,int> piii;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<pll> vll;
typedef vector<pii> vii;
typedef vector<piii> viii;
void FastIO(){ ios_base::sync_with_stdio(false); cin.tie(false); cout.tie(false);}
template <class T > T amax(T _a, T _b ){	return _a > _b ? _a : _b;}
template <class T > T amin(T _a, T _b ){	return _a < _b ? _a : _b;}
template <class T > T gcd(T _a, T _b ){	T t; while(_b){	t = _b;	_b = _a%_b;_a = t; } return _a;}
#define M 1000000007
template <class T > T apow(T b,T p){ T r=1; while(p>0){if((p%2)==1)r=(r*b)%M; b=(b*b)%M;p/=2;}return r;}
#define pb push_back
#define mp make_pair
#define sz(v) (int)v.size()
#define all(c) c.begin(), c.end()
#define ff first
#define se second
#define rep(i,n) for(int i = 0; i < n; i++)
#define rea(i,l,r) for(int i = l; i <= r; i++)
#define red(i,r,l) for(int i = r; i >= l; i--)
#define isSet(pos,mask) ((mask>>(pos))&1)
#define cSetbits(data) __builtin_popcount(data)
#define cSetbitsll(data) __builtin_popcountll(data)
int IMAX = 1e9+5;
ll LMAX = (ll)1e18+5;
ld EPS = 1e-9;
ld PI = acos(-1);
bool valid(int i,int r,int j,int c){ return 0<=i&&i<r&&0<=j&&j<c;}
const int di[8] = {0,1,0,-1,1,-1,-1,1};
const int dj[8] = {1,0,-1,0,1,-1,1,-1};
#define LOCALI 1
#define LOCALO 1
#define DEBUG 0
const int N = 1e3+10;
const int LOGN = 20;
int n,k;
pll rh[N];
bool cmp(pll a,pll b){
    if(a.ff == b.ff) return a.se < b.se;
    else return a.ff > b.ff;
}
bool cmpside(pll a,pll b){
    return a.ff*a.se > b.ff*b.se;
}
void ReadValue(){
    cin>>n>>k;
    rep(i,n)cin>>rh[i].ff>>rh[i].se;
}
void Result(int tc){
    int ii = 0;
    ld cur = 0,ans = 0;
    for(int in = 0; in < n-k+1; in++){
        sort(rh,rh+n,cmp);
        sort(rh+in+1,rh+n,cmpside);
        cur = 2*rh[in].ff*rh[in].se + rh[in].ff*rh[in].ff;
        rep(i,k-1)
            cur += (2*rh[i+in+1].ff*rh[i+in+1].se);
        if(cur > ans) ans = cur;
    }
    ans = ans*PI;
    cout<<setprecision(12)<<fixed;
    cout<<"Case #"<<tc<<": "<<ans<<"\n";
}
int main() {
	int tc =1;
	FastIO();
	if(LOCALI)freopen("A-large.in", "r", stdin);
    if(LOCALO)freopen("output1.txt", "w", stdout);
	cin>>tc;
	rep(i,tc){
	    ReadValue();
	    Result(i+1);
	}
	return 0;
}
