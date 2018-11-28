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

ll dp[1005][1005];
ll r[1005] , h[1005];
pair< ll , ll > ar[1005];
int n , k ;
ll dpp(int ind, int left){
	if(ind == n){
		return -1e18;
	}
	if(dp[ind][left] != -1)
		return dp[ind][left];
	ll ans = dpp(ind+1 , left);
	ll ans2 = 2 * r[ind] * h[ind];
	if(left == 1){

	}else{
		ans2 += dpp(ind+1 , left-1);
	}
	return dp[ind][left] = max(ans2 , ans);
}
void solve(){

	cin>>n>>k;
	REP(i , n){
		cin>>ar[i].first>>ar[i].second;
	}
	sort(ar,ar+n,[](pair< ll , ll > p1, pair< ll , ll > p2){
		if(p1.first != p2.first)
			return p1.first > p2.first;
		return p1.second < p2.second;
	});
	REP(i , n){
		r[i] = ar[i].first;
		h[i] = ar[i].second;
	}
	setminus1(dp);
	ll mm = 0;
	if(k != 1){
		REP( i , n){
			mm = max(mm , dpp(i+1 , k-1) + r[i] * r[i] + 2 * r[i] * h[i]);
		}
	}else{
		REP( i , n){
			mm = max(mm , r[i] * r[i] + 2 * r[i] * h[i]);
		}
	}
	double ans = M_PI;
	ans *= mm;
	cout.precision(10);
	cout<<fixed<<ans;
}

int main(){

	cin.tie(0);
	cout.tie(0);
	cin.sync_with_stdio(0);
	cout.sync_with_stdio(0);

	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);

	int TC = 1;
	cin>>TC;
	for(int ZZ=1;ZZ<=TC;ZZ++){
		cout<<"Case #"<<ZZ<<": ";
		clock_t start = clock();
		solve();
		clock_t end = clock();
		cout<<'\n';
		cerr <<"Time: " <<(double)(end-start)/CLOCKS_PER_SEC <<" seconds" <<endl;
	}
	return 0;
}
