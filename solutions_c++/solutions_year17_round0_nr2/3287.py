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
ll n;
int dig;
int a[20];
int main() {
	fi("B-large.in");
	fo("out.txt");
	int i,t,no=1;
	ll ans,temp;
	S(t);
	while(t--) {
		Sl(n);
		ans=0;
		temp=n;
		i=0;
		do {
			a[i]=n%10;
			n/=10;
			++i;
		} while(n);
		n=temp;
		dig=i;
		reverse(a,a+i);
		if(dig<=1) ans=n;
		else {
			for(i=0;i<dig;++i) {
				if(i&&a[i]<a[i-1]) break;
			}
			if(i==dig) ans=n;
			else {
				int j=i-1;
				while(j-1>=0&&a[j]==a[j-1]) --j;
				a[j]--;
				for(++j;j<dig;++j) a[j]=9;
				ans=0;
		//		debug(dig);
				for(i=0;i<dig;++i) ans=ans*10+a[i];
			}
		}
		printf("Case #%d: %lld\n",no,ans);
		++no;
	}
   return 0;
}
