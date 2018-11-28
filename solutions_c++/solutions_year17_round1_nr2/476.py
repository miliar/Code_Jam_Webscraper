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

int func() {
	int n, p;
	cin >> n >> p;
	vi vet(n);
	for (int i = 0; i < n; ++i) {
		cin >> vet[i];
	}
	vvi mat(n, vi(p));
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < p; ++j) {
			cin >> mat[i][j];
		}
		sort(all(mat[i]));
	}
	vi pos(n);
	vii aux(n);
	bool add = false;
	int out = 0;
	while (true) {
		for (int i = 0; i < n; ++i) {
			if(add) ++pos[i];
			do {
				if (pos[i] >= p) {
					return out;
				}
				double v = mat[i][pos[i]]/1.1/vet[i];
				aux[i].st = (v == int(v) ? int(v) : int(v) + 1);
				aux[i].nd = mat[i][pos[i]]/0.9/vet[i];
			} while (aux[i].st > aux[i].nd && ++pos[i]);
		}
		add = false;
		int mx = aux[0].st;
		int mn = aux[0].nd;
		for (int i = 0; i < n; ++i) {
			mx = max(mx, aux[i].st);
			mn = min(mn, aux[i].nd);
		}
		if (mn < mx) {
			for (int i = 0; i < n; ++i) {
				if (aux[i].nd < mx) {
					do {
						++pos[i];
						if (pos[i] >= p) {
							return out;
						}
						double v = mat[i][pos[i]]/1.1/vet[i];
						aux[i].st = (v == int(v) ? int(v) : int(v) + 1);
						v = mat[i][pos[i]]/0.9/vet[i];
						aux[i].nd = (v == int(v) ? int(v) : int(v) + 1);
					} while (aux[i].st > aux[i].nd);
				}
			}
		} else {
			++out;
			add = true;
		}
	}
}

int main(void){
	//ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t(0); t - T; ++t) {
		cout << "Case #" << t + 1 << ": " << func() << endl;
	}

	return 0;
}
