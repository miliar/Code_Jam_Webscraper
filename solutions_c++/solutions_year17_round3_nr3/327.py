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

double dp[52][52];
pair< int , string > ar[52];
double br[52];
string curstring;
ll getit(string s){
	ll ans = s[0] - '0';
	for(int i = 1; i < s.length(); i++){
		if(s[i] == '.')
			continue;
		ans = 10 * ans + s[i] - '0';
	}
	return ans;
}
int n , k;
double dpp(int ind, int tocorrent){
	if(ind == n){
		if(tocorrent == 0)
			return 1.0;
		return 0.0;
	}
	if(dp[ind][tocorrent] > -0.5)
		return dp[ind][tocorrent];
	double ans = (1-br[ind])*dpp(ind+1 , tocorrent);
	if(tocorrent){
		ans += br[ind] * dpp(ind+1, tocorrent-1);
	}
	return dp[ind][tocorrent] = ans;


}
void solve(){
	setminus1(dp);
	cin>>n>>k;
	double ans = 0;
	cin>>curstring;
	ll cur = getit(curstring);
	REP( i ,n){
		cin>>ar[i].second;
		ar[i].first = getit(ar[i].second);
	}
	sort(ar,ar+n,[](pair< int , string > p1 , pair< int , string > p2){
		return p1.first > p2.first;
	});
	REP( i ,n){
		double x = ar[i].first;
		x /= 10000.0;
		br[i] = x;
	}

	ll fornow = ar[k-1].first;
	ll cnt = 1;
	int changed = 0;
	for(int j = k-2; j >= 0 ; j--){
		ll target = ar[j].first;
		if((target - fornow)*cnt <= cur){
			cur -= (target - fornow)*cnt;
			cnt++;
			fornow = target;
		}else{
			double final = fornow;
			final /= 10000.0;
			final += (((double)cur)/((double)cnt*10000.0));
			for(int jj = j+1 ; jj < k; jj++){
				br[jj] = final;
			}
			changed = 1;
			break;
		}
	}
	if((10000 - fornow)*cnt <= cur){
		// k 1
		cout<<"1.000000";
		return;
	}
	if(changed == 0){
		double final = fornow;
		final /= 10000.0;
		final += (((double)cur)/((double)cnt*10000.0));
		for(int jj = 0 ; jj < k; jj++){
			br[jj] = final;
		}
	}
	for(int j = k; j <= n; j++){
		ans += dpp(0 , j);
	}
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
