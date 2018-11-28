#include <bits/stdc++.h>
using namespace std;
#define gc getchar_unlocked
#define fo(i,n) for(i=0;i<n;i++)
#define Fo(i,k,n) for(i=k;k<n?i<n:i>n;k<n?i+=1:i-=1)
#define ll long long
#define si(x)	scanf("%d",&x)
#define sl(x)	scanf("%lld",&x)
#define ss(s)	scanf("%s",s)
#define pi(x)	printf("%d\n",x)
#define pl(x)	printf("%lld\n",x)
#define ps(s)	printf("%s\n",s)
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define all(x) x.begin(), x.end()
#define clr(x) memset(x, 0, sizeof(x))
#define sortall(x) sort(all(x))
#define tr(it, a) for(auto it = a.begin(); it != a.end(); it++)
#define PI 3.1415926535897932384626
typedef pair<int, int>	pii;
typedef pair<ll, ll>	pl;
typedef vector<int>		vi;
typedef vector<ll>		vl;
typedef vector<pii>		vpii;
typedef vector<pl>		vpl;
typedef vector<vi>		vvi;
typedef vector<vl>		vvl;
int mpow(int base, int exp);
void ipgraph(int m);
void dfs(int u, int par);
const int mod = 1000000007;
const int N = 3e5, M = N;
//=======================

vi g[N];
int a[N], n, s[N], k[N];
double d;
bool f(double x){
    int i;
    double t = (d*1.0)/x;
    double ans = 0;
    fo(i, n) ans = max(ans, (d-k[i]+0.0)/s[i]);
    return ans <= t;
}
double bin(double lo, double hi, int iter = 200){
    if(iter==0) return lo;
    iter--;
    double mid = (lo+hi)/2;
    if(f(mid)) return bin(mid, hi, iter);
    return bin(lo, mid, iter);
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int i,j,t,xx;
	freopen("in.txt", "r", stdin);	freopen("out.txt", "w", stdout);
	cin >> t;
	fo(xx, t){
		cin >> d >> n;
		fo(i, n) cin >> k[i] >> s[i];
		double lo = 0.0, hi = pow(10, 19);
		double ans = bin(lo, hi);
		cout << fixed << setprecision(8) <<  "Case #" << xx+1 << ": " << ans << endl;
	}

	return 0;
}
