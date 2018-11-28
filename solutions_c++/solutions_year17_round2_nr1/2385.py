///Felipe Kallas Silva
///UNIFEI - Federal University of Itajuba
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

const int INF = 0x3F3F3F3F;
const ll LINF = 0x3F3F3F3F3F3F3F3FLL;
const double EPS = 1e-9;

#define mp make_pair
#define pb push_back
#define quad(x) ((x)*(x))
#define clr(x, y) memset(x, y, sizeof x)

#define all(x) x.begin(),x.end()
#define rall(x) x.rbegin(),x.rend()
#define _sort(x) sort(all(x))

#define mod(x, m) ((x % m) + ((x < 0) ? m : 0))

#define F first
#define S second

#define For(i,n) for(int i = 0 ; i < (n); ++i)

#define D(x) cout << #x " = " << (x) << " "
#define C(x) printf("Chegou aqui: %d\n", x)

#define pn printf("\n")
#define ps printf(" ")

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("alarge", "w", stdout);
	int t;
	cin >> t;
	for (int o = 1; o <= t; ++o) {

		double s;
		int n;
		cin >> s >> n;
		double tmin;
		for (int i = 0; i < n; ++i) {
			double s0, v;
			scanf("%lf %lf", &s0, &v);
			double t = (s - s0) / v;
			if (i == 0) tmin = t;
			else if (t > tmin) tmin = t;
		}


		printf("Case #%d: %lf\n", o, s / tmin);
	}
	return 0;
}
