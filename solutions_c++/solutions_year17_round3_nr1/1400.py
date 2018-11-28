// <abhishek944>  <(0-9):(A-Z):(a-z)>  <(48-57):(65-90):(97-122)>
#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;
typedef long double ld;

#define endl "\n"
#define sz size()
#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define fill(a,val) memset(a,val,sizeof(a))
#define openup freopen("inputA.txt","r",stdin)
#define closeup freopen("output.txt","w",stdout);
#define FOR(i,l,r) for(int i = l;i <= r; i++)
#define RFOR(i,r,l) for(int i = r;i >= l; i--)
#define Nitro ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define forall(it, x) for(__typeof((x).begin()) it=(x).begin();it!=(x).end();it++)
#define sleep() std::this_thread::sleep_for (std::chrono::seconds(1));

const ld PI = 3.1415926535897932384626;
const ll MOD = 1000000000 + 7;
const int INF = 0x3f3f3f3f;
const ll INFF = 0x3f3f3f3f3f3f3f3f;
const ld eps = 0.00000001;

#define TRACE(x) cerr<<"[[ "<<#x<<" = "<<x<<" ]]"<<endl;
#ifdef TRACE
#define trace(...) __f(#__VA_ARGS__,__VA_ARGS__)
template <typename Arg1> void __f(const char* name, Arg1 && arg1) {
cerr << name << " : " << arg1 << endl; }
template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args) { const char* comma = strchr(names + 1, ',');
cerr.write(names, comma - names) << " : " << arg1 << " | "; __f(comma + 1, args...); }
#else
#define trace(...)
#endif
#define Assert(x,y) {if(x!=y){cerr<<__LINE__ <<"->  Assertion Failed "<<": ("<<#x<<"!="<<y<<") ";TRACE(x);exit(1);}}
double tick(){static clock_t oldt,newt=clock();double diff=1.0*(newt-oldt)/CLOCKS_PER_SEC;oldt=newt;return diff;}

ll Mmod(ll a,ll m){ll c=a%m;while(c<0)c+=m;return c;}
ll Mmul(ll a,ll b,ll m){ll c=a*b*1LL;c%=m;while(c<0){c+=m;}return c;}
ll Madd(ll a,ll b,ll m){ll c=a+b;c%=m;while(c<0){c+=m;}return c;}
ll Msub(ll a,ll b,ll m){return Madd(a,m-b,m);}
ll Npow(ll A,ll p){ll ret=1;while(p){if(p&1){ret=(ret*A);}A=(A*A);p>>=1;}return ret;}
ll Mpow(ll a,ll n,ll b){ll res=1;while(n){if(n&1){res=Mmul(res,a,b);}a=Mmul(a,a,b);n>>=1;}return res;}
ll Ndiv(ld A,ld B,bool ud){if(B){ld ret=(ld)(A)/(ld)(B);if(ud)return ceil(ret);return floor(ret);}return INF;}
ll Mdiv(ll a,ll b,ll m){ll ans=Mmul(a,Mpow(b,m-2,m),m);return ans;}

/*
	Handle 		-	abhishek944
	Problem 	-	
	Complexity 	-	
	Description	-	
	Judge		-	
*/

#define O 1
#define M (1000 * O) + 10
#define N M + 123

#define pdd pair < double , double >

bool cmp(const pdd &X , const pdd &Y) {
	if(X.ff==Y.ff) return X.ss > Y.ss;
	return X.ff > Y.ff;
}

double dp[2000][2000];

double getarea(pdd &X) {
	double tmp = PI * X.ff * X.ff;
	tmp += 2 * PI * X.ss * X.ff;
	return tmp;
}

double subarea(pdd &X) {
	double tmp = X.ff * X.ff * PI;
	return tmp;
}

int main()
{
	Nitro; openup; closeup;

	int t;
	cin >> t;
	FOR(ii , 1 , t) {

		fill(dp , 0);
		int n , k;
		cin >> n >> k;

		vector < pair < double , double > > vi;

		double x , y;
		FOR(i , 0 , n - 1) {
			cin >> x >> y;
			vi.pb({x , y});
		}

		sort(vi.begin() , vi.end() , cmp);

		/*vector < pdd > tmp;
		for(int i=0;i<n;) {
			int j = i+1;
			while(j < n && vi[i].ff==vi[j].ff) j++;
			tmp.push_back(vi[i]);
			i = j; 
		}
		vi = tmp;*/

		for(int j=1;j<=n;j++) {
			if(j==1) dp[1][j] = getarea(vi[0]);
			else dp[1][j] = max(dp[1][j - 1] , getarea(vi[j- 1]));
		}

		for(int i=2;i<=k;i++) {
			for(int j=i;j<=n;j++) {
				if(j==i) dp[i][j] = dp[i-1][j-1] + getarea(vi[j - 1]) - subarea(vi[j - 1]);  
				else {
					dp[i][j] = max(dp[i][j - 1] , dp[i - 1][j - 1] + getarea(vi[j - 1]) - subarea(vi[j - 1]));
				}
			}
		}

		cout << "Case #" << ii << ": " << fixed << setprecision(8) << dp[k][n] << endl;
	}

	return 0;
}