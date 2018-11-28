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
int dp[105][105][105];
int p;
int n;
int totalsum = 0;
int dpp(int mod1, int mod2,int mod3){
	if(dp[mod1][mod2][mod3] != -1)
		return dp[mod1][mod2][mod3];
	int ans = 0;
	int openleft = totalsum - mod1 - 2*mod2 - 3*mod3;
	openleft %= p;
	openleft+=p;
	openleft %= p;
	int cur = 0;
//	cout<<mod1<<" "<<mod2<<" "<<mod3<<" gives left over "<<openleft<<endl;
	if(openleft == 0)
		cur++;
	if(mod1)
		ans = max(ans , cur + dpp(mod1-1, mod2,mod3));
	if(mod2)
		ans = max(ans , cur + dpp(mod1, mod2-1,mod3));
	if(mod3)
		ans = max(ans , cur + dpp(mod1, mod2,mod3-1));
//	cout<<mod1<<" "<<mod2<<" "<<mod3<<" "<<ans<<endl;
	return dp[mod1][mod2][mod3] = ans;
}

void solve(){
	setminus1(dp);
	dp[0][0][0] = 0;
	cin>>n>>p;
	int m[4];
	REP( i , 4)
		m[i] = 0;
	totalsum = 0;
	REP( i ,n){
		int x;
		cin>>x;
		x %= p;
		m[x] ++;
		totalsum += x;
	}
	totalsum %= p;
	cout<<dpp(m[1] , m[2] , m[3]) + m[0];

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
