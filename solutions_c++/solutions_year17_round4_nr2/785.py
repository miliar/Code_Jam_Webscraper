#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007
#define INF 0x3f3f3f3f //numeric_limits<int>::max()
#define INFLL 0x3f3f3f3f3f3f3f3fLL //numeric_limits<ll>::max()
#define mp make_pair
#define mt make_tuple
#define getT(T, p) get<p>(T)
#define pb push_back
#define st first
#define nd second
#define contOnes __builtin_popcountl
#define powDI __builtin_powi
#define sz(v) int(v.size())
#define ver(x) if(debug) {cout << #x << " is " << x << endl; if(--debugCount < 0) exit(1);};
#define endLine if(debug) {cout << endl;}
//cuidado parametro duplicados
#define all(X) (X).begin(), (X).end()
#define logLow(X) (X <= 0 ? 0 : 31 - __builtin_clz(X))
#define logUpper(X) (X <= 1 ? 0 : 32 - __builtin_clz(X-1))
#define pow2(X) ((X)*(X))
#define unico(X) X.erase(unique((X).begin(), (X).end()), (X).end())
#define __ << " " <<

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;
typedef pair<ll,ll> llll;
typedef pair<int,ii> iii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<llll> vllll;
typedef vector<vii> vvii;
typedef vector<iii> viii;
typedef vector<ll> vll; 

const double EPS = 1e-8;
//const double PI = atan(1.0)*4;
const double PI = 2*acos(0.0);
inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}
int debugCount = 20;
bool debug = true;

//#define turns(x) ((x) + hk/(ad + (x)*b))
#define turnsInt(x) (x + (hk + ad + x*b - 1)/(ad + x*b))
#define turnsLL(x) (ll(x) + (hk + ad + ll(x)*b - 1)/(ad + ll(x)*b))


void func() {
	int n, c, m;
	cin >> n >> c >> m;
	vector<int> vet[c];
	for (int i = 0, p, b; i < m; ++i) {
		cin >> p >> b;
		vet[b-1].pb(p);
	}
	if(sz(vet[0]) > 0) sort(all(vet[0]));
	if(sz(vet[1]) > 0) sort(all(vet[1]));
	vector<int> aux0(n+1);
	vector<int> aux1(n+1);
	for (int i = 0; i < sz(vet[0]); ++i) {
		aux0[vet[0][i]]++;
	}
	for (int i = 0; i < sz(vet[1]); ++i) {
		aux1[vet[1][i]]++;
	}
	int y = max(max(sz(vet[0]), sz(vet[1])), aux0[1]+aux1[1]);
	int z = 0;
	for (int i = 1; i <= n; ++i) {
		if(aux0[i] > y - aux1[i]) z += aux0[i] - (y - aux1[i]);
		if(aux1[i] > y - aux0[i]) z += aux1[i] - (y - aux0[i]);
	}
	cout << y << " " << z/2 << endl;
}

int main(void){
	//ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t(0); t - T; ++t) {
		cout << "Case #" << t + 1 << ": ";
		func();
	}

	return 0;
}
