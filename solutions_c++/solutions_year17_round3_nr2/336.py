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

ll busy[2000];
#define C 0
#define J 1
int ac , aj;
#define ONCE 720
#define TWICE (2 * ONCE)
ll dp[1500][750][2];
ll dpp(int curmin , int timebyc, int turn){
	if(curmin == TWICE)
		return 0;
	if(dp[curmin][timebyc][turn] != -1)
		return dp[curmin][timebyc][turn];
	int tc = timebyc;
	int tj = curmin - timebyc;
	if(turn)
		tj++;
	else
		tc++;
	if(tj > ONCE || tc > ONCE)
		return dp[curmin][timebyc][turn] = 1e18;
	if(turn){
		if(busy[curmin] == J)
			return dp[curmin][timebyc][turn] = 1e18;
	}else{
		if(busy[curmin] == C)
			return dp[curmin][timebyc][turn] = 1e18;
	}
	ll ans = 0;
	ans = dpp(curmin + 1 , tc , turn);
	ans = min(ans , dpp(curmin + 1 , tc , 1 - turn) + 1);
//	cout<<curmin<<" "<<timebyc<<" "<<turn<<" "<<ans<<endl;
	return dp[curmin][timebyc][turn] = ans;

}
void solve(){
	setinf(busy);
	cin>>ac>>aj;
	REP( i ,ac){
		int c , d;
		cin>>c>>d;
		for(int j = c; j < d; j++){
			busy[j] = C;
		}
	}
	REP( i ,aj){
		int c , d;
		cin>>c>>d;
		for(int j = c; j < d; j++){
			busy[j] = J;
		}
	}
	setminus1(dp);
	if(busy[0] == busy[TWICE-1] && busy[0] < 100){
		cout<<min(dpp( 0 , 0 , 0) , dpp( 0 , 0 , 1));
	}else if(busy[TWICE-1] < 100 && busy[0] < 100){
		cout<<min(dpp( 0 , 0 , 0) , dpp( 0 , 0 , 1)) + 1;
	}else{
		ll ans = 1e18;
		if(busy[0] < 100){
			busy[TWICE-1] = busy[0];
			ans = min(dpp( 0 , 0 , 0) , dpp( 0 , 0 , 1));
			setminus1(dp);
			busy[TWICE-1] = 1 - busy[0];
			ans = min(ans , min(dpp( 0 , 0 , 0) , dpp( 0 , 0 , 1)) + 1);
		}else if(busy[TWICE-1] < 100){
			busy[0] = busy[TWICE-1];
			ans = min(dpp( 0 , 0 , 0) , dpp( 0 , 0 , 1));
			setminus1(dp);
			busy[0] = 1 - busy[TWICE-1];
			ans = min(ans , min(dpp( 0 , 0 , 0) , dpp( 0 , 0 , 1)) + 1);
		}else{
			busy[0] = 0;
			busy[TWICE-1] = 0;
			ans = min(ans , min(dpp( 0 , 0 , 0) , dpp( 0 , 0 , 1)));
			setminus1(dp);
			busy[0] = 1;
			busy[TWICE-1] = 1;
			ans = min(ans , min(dpp( 0 , 0 , 0) , dpp( 0 , 0 , 1)));
			setminus1(dp);
			busy[0] = 0;
			busy[TWICE-1] = 1;
			ans = min(ans , min(dpp( 0 , 0 , 0) , dpp( 0 , 0 , 1)) + 1);
			setminus1(dp);
			busy[0] = 1;
			busy[TWICE-1] = 0;
			ans = min(ans , min(dpp( 0 , 0 , 0) , dpp( 0 , 0 , 1)) + 1);
		}
		cout<<ans;

	}
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
