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

int main(void){
	//ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t(0); t - T; ++t) {
		int r, c;
		cin >> r >> c;
		vector<string> vet(r);
		for (int i = 0; i < r; ++i) {
			cin >> vet[i];
		}
		for (int i = 0; i < r; ++i) {
			for (int j = 1; j < c; ++j) {
				if (vet[i][j] == '?') {
					vet[i][j] = vet[i][j-1];
				}
			}
			for (int j = c-2; j >= 0; --j) {
				if (vet[i][j] == '?') {
					vet[i][j] = vet[i][j+1];
				}
			}
		}
		for (int i = 1; i < r; ++i) {
			if (vet[i][0] == '?') {
				for (int j = 0; j < c; ++j) {
					vet[i][j] = vet[i-1][j];
				}
			}
		}
		for (int i = r-2; i >= 0; --i) {
			if (vet[i][0] == '?') {
				for (int j = 0; j < c; ++j) {
					vet[i][j] = vet[i+1][j];
				}
			}
		}
		cout << "Case #" << t + 1 << ":" << endl;
		for (int i = 0; i < r; ++i) {
			cout << vet[i] << endl;
		}
	}

	return 0;
}
