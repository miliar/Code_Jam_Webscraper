#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define lb lower_bound
#define ub upper_bound
#define pb push_back
#define mp make_pair
#define ll long long
#define fi(filename) freopen(filename, "r", stdin)
#define fo(filename) freopen(filename, "w", stdout)
#define popcount(i) __builtin_popcount(i)      //count one. in long long use __builtin_popcountll(i)
#define gcd __gcd
//debug
#define debug(args...) cout<<__FUNCTION__<<":"<<__LINE__<<" ";do{cout<<#args<<": ";dbg,args;cout<<endl;} while(0)
struct debugger
{template<typename T> debugger& operator ,(const T& v){cout<<v<<" ";return *this;}}dbg;
#define dbgarr(a,start,end) cout<<__FUNCTION__<<":"<<__LINE__<<"\n";for(ll i=start;i<end;i++) cout<<#a<<"["<<i<<"] -> "<<a[i]<<" "<<endl;
#define dbgmat(mat,row,col) cout<<__FUNCTION__<<":"<<__LINE__<<"\n";for(ll i=0;i<row;i++) {for(ll j=0;j<col;j++) cout<<mat[i][j]<<" ";cout<<endl;}
#define F(i,a,n) for(typeof(a) i=(a);i<(n);++i)
#define R(i,a,n) for(typeof(a) i=(a);i>=(n);--i)
#define tr(it,container) for(typeof(container.begin()) it = container.begin(); it != container.end(); ++it)
//scan
#define fastio	  ios_base::sync_with_stdio(0);cin.tie()
#define SS(args...) do{input,args;} while(0)
struct scanner
{template<typename T> scanner& operator ,(T& v){cin>>v;return *this;}}input;
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define P(x) printf("%d\n",x)
#define Pl(x) printf("%lld\n",x)
#define M(x,i) memset(x,i,sizeof(x))      // useful to clear array of integer
#define fr first
#define se second
#define INF 2147483647
#define MOD 1000000007   //	(int)1e9+7
#define all(x)    x.begin(),x.end()
#define get getchar//_unlocked
#define put putchar//_unlocked
inline int scan() {
	register int n=0;
	register char p;
	do {p=get();}while(p<'0');
	while(p>='0') {
		n = (n<<3) + (n<<1) + (p - '0');
		p=get();
	}
	return n;
}
inline void print(int X)
{
	int Len=-1;
	char Data[10];
	do {
		Data[++Len]=X%10+'0';
		X/=10;
	} while(X);
	while(Len>=0) put(Data[Len--]);
}
int main() {
	fi("C-small-2-attempt0.in");
	fo("out.txt");
	int t,no=1,num;
	ll n,k,x,y;
	S(t);
	map< ll,ll,greater<ll> > freq;
	while(t--) {
		Sl(n);Sl(k);
		freq.clear();
		freq[n]=1;
		ll ct=0;
		tr(it,freq) {
			num=it->fr;
			if(num==1||ct+it->se>=k) {
				if(num&1) x=y=(num-1)/2;
				else {
					x=num/2;
					y=x-1;
				}
				break;
			}
			else {
				if(num&1) freq[(num-1)/2]+=2*freq[num];
				else {
					freq[num/2]+=freq[num];
					freq[num/2-1]+=freq[num];
				}
			}
			ct+=it->se;
		}
		printf("Case #%d: %lld %lld\n",no,x,y);
		++no;
	}
   return 0;
}
