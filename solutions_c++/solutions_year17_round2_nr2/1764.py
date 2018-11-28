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
int n,r,o,y,g,b,v;
string ss[5][5];
pair<int,int> a[4],c[4];

void col(int k){
	if(c[k].f){
		cout<<ss[k][0];
		c[k].f--;
	}
	else{
		cout<<ss[k][1];
		c[k].s--;
	}

}
int kk ;
void print() {
	if(a[2].f==1 && a[1].f==0 && a[0].f==0){
		col(a[2].s);
		return;
	}
	while(a[1].f!=a[0].f){
		col(a[2].s);
		col(a[1].s);
		a[2].f--;
		a[1].f--;
	}
	while(a[2].f != a[0].f){
		col(a[2].s);
		col(a[1].s);
		col(a[2].s);
		col(a[0].s);
		a[2].f-=2;
		a[1].f--;
		a[0].f--;
	}
	while(a[0].f){
		col(a[2].s);
		col(a[1].s);
		col(a[0].s);
		a[0].f--;
	}
}
void solve() {
	cin>>n>>r>>o>>y>>g>>b>>v;
	int fl=0,co=0,set=-1;
	kk=0;
	string buff;
	if(o>2*b || g>2*r || v>2*y){
		cout<<"IMPOSSIBLE"<<endl;
		return;
	}
	if(b<2*o){
		if(b==2*o-1 && n!=5){
			buff = "OB";
			b -= 3;
			o -= 2;
		}
		else if(n==4){
			cout<<"BOBO"<<endl;;
			return;
			b=o=0;
		}
		else fl = 1;
		set = 0;
		co++;
	}
	if(r<2*g){
		if(r==2*g-1 && n!=5){
			buff = "GR";
		r -= 3;
			g -= 2;
		}
		else if(n==4){
			cout<<"RGRG"<<endl;
			return;
			r=g=0;
		}
		else fl = 1;
		set = 1;
		co++;
	}
	if(y<2*v){
		if(y==2*v-1 && n!=5){
			buff = "VY";
			y -= 3;
			v -= 2;
		}
		else if(n==4){
			cout<<"YVYV"<<endl;
			return;
			y=v=0;
		}
		else fl = 1;
		set = 2;
		co++;
	}
	if(co>1) fl=1;
	if(fl){
		cout<<"IMPOSSIBLE"<<endl;
		return;
	}
	c[0] = mp(b-2*o,o);
	c[1] = mp(r-2*g,g);
	c[2] = mp(y-2*v,v);
	for(int i=0;i<3;i++)
		a[i] = mp(c[i].f + c[i].s,i);
	sort(a,a+3);
	if(a[2].f>a[1].f+a[0].f && a[2].f>1){
		cout<<"IMPOSSIBLE"<<endl;
		return;
	}
	ss[0][1] = "BOB";
	ss[0][0] = "B";
	ss[1][1] = "RGR";
	ss[1][0] = "R";
	ss[2][1] = "YVY";
	ss[2][0] = "Y";
	if(co) cout<<buff;
	print();
	if(set>=0) cout<<ss[set][1];
	cout<<endl;
}
