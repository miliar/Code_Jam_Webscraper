#include <bits/stdc++.h>
using namespace std;

#define INF INT_MAX
#define LINF LLONG_MAX
#define MOD 1000000007
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define SZ(x) ((int)((x).size()))
#define clr(a,x) memset(a,x,sizeof(a))
#define IOS ios_base::sync_with_stdio(0)
#define F(ii,L,R) for (int ii = L; ii < R; ii++)
#define FE(ii,L,R) for (int ii = L; ii <= R; ii++)
#define FF(ii,L,R) for (int ii = L; ii > R; ii--)
#define FFE(ii,L,R) for (int ii = L; ii >= R; ii--)
#define FOREACH(i,t) for (__typeof__(t.begin()) i=t.begin(); i!=t.end(); i++)
#define ALL(c) (c).begin(),(c).end()
#define wez(n) int (n); scanf("%d",&(n))
#define wez2(n,m) int (n),(m); scanf("%d %d",&(n),&(m))
#define wez3(n,m,k) int (n),(m),(k); scanf("%d %d %d",&(n),&(m),&(k))
#define getI(a) scanf("%d", &a)
#define getII(a,b) scanf("%d%d", &a, &b)
#define getIII(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define getS(x) cin >> x;
#define printA(a,L,R) FE(i,L,R) cout << a[i] << (i==R?'\n':' ')
#define printV(a) printA(a,0,a.size()-1)
#define FIN(x) freopen(x,"r",stdin)
#define FOUT(x) freopen(x,"w",stdout)
#define print(t) cout << t << ' ';
#define PI           3.14159265358979323846264338327950288419716939937510

typedef long long ll;
typedef unsigned long long ull;
typedef float fl;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef pair<long, long> pll;
typedef map<char, int> mci;
typedef map<int, int> mii;

void DEB() {cout << endl;}
template <typename T, typename...Ts>
void DEB(T first, Ts... rest) {
    print(first);
    DEB(rest...); 	
}

int K;
double dp[1001][1001];

double solve(vector<pair<double,double> > a, int n, int k){
	if(n == 0 || k == 0)	return 0;
	if(!dp[n][k]){
		double area = 2.0 * PI * a[n-1].fi * a[n-1].se;
		if(k == K) area += PI * a[n-1].fi * a[n-1].fi;
		dp[n][k] = max(area + solve(a, n-1, k-1), solve(a, n-1, k));
	}
	return dp[n][k];
}

bool cmp(pair<double, double> a, pair<double, double> b){
	return a.fi > b.fi;
}

void work(){
	FIN("A-large.in");
	FOUT("A-large.out");	
	wez(t);
	FE(tt, 1, t){
		wez2(n, k);
		K = k;
		vector<pair<double, double> > a;
		F(i, 0, n){
			double x=0, y=0;
			cin >> x >> y;
			a.pb(mp(x, y));
		}
		sort(ALL(a));
		printf("Case #%d: ", tt);
		clr(dp, 0.0);
		printf("%.6f\n", solve(a, n, k));
	}
}

int main(){
	work();
	return 0;
}