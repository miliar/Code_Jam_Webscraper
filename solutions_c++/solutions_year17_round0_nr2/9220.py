/*************************************************************************
    > File Name: BB.cpp
    > Author: HandsomeHow
    > Mail: handsomehowyxh@gmail.com 
    > Created Time: 2017/4/8 18:24:34
 ************************************************************************/

#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b) for(int i=(a);i<=(b);i++)
#define per(i,a,b) for(int i=(a);i>=(b);i--)
#define pb push_back
#define mp make_pair
#define cl(a) memset((a),0,sizeof(a))
#ifdef HandsomeHow
#define dbg(x) cerr << #x << " = " << x << endl
#else
#define dbg(x)
#endif
typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> pii;
const int inf=0x3f3f3f3f;
const double eps=1e-8;
const int mod=1000000007;
const double pi=acos(-1.0);
inline void gn(long long&x){
    int sg=1;char c;while(((c=getchar())<'0'||c>'9')&&c!='-');c=='-'?(sg=-1,x=0):(x=c-'0');
    while((c=getchar())>='0'&&c<='9')x=x*10+c-'0';x*=sg;}
inline void gn(int&x){long long t;gn(t);x=t;}
inline void gn(unsigned long long&x){long long t;gn(t);x=t;}
ll gcd(ll a,ll b){return a? gcd(b%a,a):b;}
ll powmod(ll a,ll x,ll mod){ll t=1ll;while(x){if(x&1)t=t*a%mod;a=a*a%mod;x>>=1;}return t;}
// (¤Å¡ã¦Ø¡ã)¤Åe¡ï------------------------------------------------
set<ll>st;
void go(ll x){
	if(x > 1e18)
		return;
	//dbg(x);
	st.insert(x);
	int lt = x % 10;
	rep(i,lt,9)go(x*10+i);
}
int main(){
#ifdef HandsomeHow
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
#endif
	rep(i,1,9)
		go(i);
	int t;gn(t);
	rep(_,1,t){
		ll v;gn(v);
		auto it = st.upper_bound(v);
		--it;
		printf("Case #%d: %lld\n",_,*it);
	}
	return 0;
}

