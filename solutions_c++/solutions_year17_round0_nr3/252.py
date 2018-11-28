#include <bits/stdc++.h>

using namespace std;
//memset
#define MEMSET_INF 127 // about 2B
#define set0(a) memset(a,0,sizeof(a));
#define setminus1(a) memset(a,-1,sizeof(a));
#define setinf(a) memset(a,MEMSET_INF,sizeof(a));

//stl
#define mp make_pair
#define pb push_back
//#define pc(x) putchar_unlocked(x)
//#define gc() getchar_unlocked()

//Loops
#define REP(i,n) for(int i = 0;i < (int)(n); i++)
#define REP1(i,a,b) for(int i = (int)(a);i <= (int)(b); i++)
#define REPMAP(i,mm) for(auto i = mm.begin();i !=mm.end(); i++)

//Sort
#define sortvec(vec) sort(vec.begin(), vec.end())

//Misc
#define LSOne(i) (i & (-i))	// the first Least Significant One-bit in i

//modulo
#define mod %
#define NUM 1000000007


#define LONG_LONG_MAX	9223372036854775807LL
#define LONG_LONG_MIN	(-LONG_LONG_MAX-1)

#define LMAX LONG_LONG_MAX
#define LMIN LONG_LONG_MIN
#define IMAX INT_MAX
#define IMIN INT_MIN
#define PI M_PI
#define EPS 1e-9
#define INF 1e9
#define M_PI		3.14159265358979323846
#define cin(x) scanf("%d",&x)
#define cout(x) printf("$d",x)
#define endl '\n'
#define s(n) scanf("%d",&n)
#define sll(n) scanf("%I64d",&n)
#define p(n) printf("%d",n)
#define pll(n) printf("%I64d",n)
#define all(v) (v).begin(),(v).end()

//typedef
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;
typedef map<int, int> mii;
typedef tuple<int,int,int> iii;

#define MAX_N 100005


void solve(){
	map<ll, ll , greater<ll> > cnt;
	ll  n, k;
	cin>>n>>k;
	k--;
	cnt[n] = 1;
	while(k){
		pair<ll ,ll> p = *cnt.begin();
		if(p.second > k){
			break;
		}else{
			k -= p.second;
			cnt.erase(cnt.begin());
			cnt[p.first/2] += p.second;
			cnt[(p.first-1)/2] += p.second;
		}
	}
	pair<ll ,ll> p = *cnt.begin();
	cout<<p.first/2<<" "<<(p.first-1)/2;
}

int main(){

	cin.tie(0);
	cout.tie(0);
	cin.sync_with_stdio(0);
	cout.sync_with_stdio(0);
//
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);

	int TC = 1;
	cin>>TC;
	for(int ZZ=1;ZZ<=TC;ZZ++){
		cout<<"Case #"<<ZZ<<": ";
		clock_t start = clock();
//		double ans;
//		cout.precision(10);
//		cout<<fixed<<ans<<endl;
		solve();
		clock_t end = clock();
		cout<<'\n';
		cerr <<"Time: " <<(double)(end-start)/CLOCKS_PER_SEC <<" seconds" <<endl;
	}
	return 0;
}
