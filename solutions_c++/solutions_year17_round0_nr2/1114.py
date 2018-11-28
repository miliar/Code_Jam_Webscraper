#include<bits/stdc++.h>
#define maxi 300005
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define ll long long
#define si(n) scanf("%d",&n)
#define sll(n) scanf("%lld",&n)
#define TRACE
#ifdef TRACE
#define trace1(x)                cerr << #x << ": " << x << endl;
#define trace2(x, y)             cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define trace3(x, y, z)          cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define trace4(a, b, c, d)       cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define trace5(a, b, c, d, e)    cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define trace6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
#else
#define trace1(x)
#define trace2(x, y)
#define trace3(x, y, z)
#define trace4(a, b, c, d)
#define trace5(a, b, c, d, e)
#define trace6(a, b, c, d, e, f)
#endif
#define gc getchar
ll mpow(ll a, ll n,ll mod){
	ll ret=1;ll b=a;
	while(n) {
		if(n&1)
			ret=(ret*b)%mod;
		b=(b*b)%mod;
		n>>=1;
	}
	return (ll)ret;
}
inline void read(int &x){
	x=0;
	register char c=gc();
	for(;c<'0' || c>'9';c=gc());
	for(;c>='0' && c<='9';c=gc())
		x=(x<<3)+(x<<1)+(c-'0');
}
inline void write(int x){
	register char buffor[35];
	register int i=0;
	do{
		buffor[i++]=(x%10)+'0';
		x/=10;
	} while(x);
	i--;
	while(i>=0) putchar(buffor[i--]);
	putchar('\n');
}
inline int in() { int x; read(x); return x; }
void solve();
int dbg=1;
using namespace std;
int main(){
	int t=1;
	read(t);
	for(int i=0;i<t;i++){
		printf("Case #%d: ",i+1);
		solve();
	}
	return 0;
}
ll find(ll num,ll n){
	ll a=num;
	//trace2(num,n);
	for(int i=9;i>=(num%10);i--)
		if(num*10+i<=n && (num*10+i)!=0)
			a = max(a,find(num*10+i,n));
	return a;
}
void solve() {
	ll n;
	cin>>n;
	cout<<find(0,n)<<endl;
}
