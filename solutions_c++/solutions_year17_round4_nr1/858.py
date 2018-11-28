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


int func() {
	int n, p;
	cin >> n >> p;
	vector<int> vet(p);
	for (int i = 0, v; i < n; ++i) {
		cin >> v;
		vet[v%p]++;
	}
	if (p == 2) {
		return vet[0] + (vet[1]+1)/2;
	} else if (p == 3) {
		return vet[0] + min(vet[1], vet[2]) + (vet[1] + vet[2] - min(vet[1], vet[2])*2 + 2)/3;
	} else {
		int v0 = vet[0];
		int v13 = min(vet[1], vet[3]);
		vet[1] -= v13;
		vet[3] -= v13;
		int v2 = vet[2]/2;
		vet[2] %= 2;
		int v31 = (vet[1] + vet[3])/4;
		vet[1] %= 4;
		vet[3] %= 4;
		int v123 = ((vet[1] + vet[2] + vet[3]) > 0) + ((vet[1] + 2*vet[2] + vet[3]) > 4);
		return v0 + v13 + v2 + v31 + v123;
 	}
}

int main(void){
	//ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t(0); t - T; ++t) {
		int f = func();
		cout << "Case #" << t + 1 << ": " << f << endl;
	}

	return 0;
}
