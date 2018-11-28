#include <bits/stdc++.h>
#define FILEN ""

#ifdef LOCAL
	#define debug (x)			cerr << #x << " == " << x << "\n";
	#define debugP (x, y) 		cerr << #x << " == " << x << " " << #y << " == " << y << "\n";
	#define debugT (x, y, z)    cerr << #x << " == " << x << " " << #y << " == " << y << " " << #z << " == " << z << "\n";
#else
	#define debug (x)
	#define debugP (x, y)
	#define debugT (x, y, z)
#endif

using namespace std;

#define mp make_pair
#define pb push_back
typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> pii;
typedef pair <double, double> pdd;

const int MAXN = 3;

pii C[MAXN], J[MAXN];
int n, m;

int solve () {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> C[i].first >> C[i].second;
	//	C[i].second += C[i].first;
	}
	for (int i = 0; i < m; i++) {
		cin >> J[i].first >> J[i].second;
	//	J[i].second += J[i].first;
	}
	sort (C, C + n);
	sort (J, J + m);

	if (n == 1 || m == 1) {
		return 2;
	}
	if (n == 2) {
		int val = min (C[1].second - C[0].first, C[0].second + 24 * 60 - C[1].first);
	//	cerr << C[1].second - C[0].first << "\n";
		if (val > 720)
			return 4;
		return 2;		
	} else {
		int val = min (J[1].second - J[0].first, J[0].second + 24 * 60 - J[1].first);
		cerr << val << "\n";
		if (val > 720)
			return 4;
		return 2;		
	}
}

int main () {
	ios_base:: sync_with_stdio (false);
	cin.tie (NULL);
#ifdef LOCAL
	freopen ("test.in", "r", stdin);
	freopen ("test.out", "w", stdout);
#else
	freopen (FILEN".in", "r", stdin);
	freopen (FILEN".out", "w", stdout);	
#endif

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cerr << "i" << i << " : \n";
		cout << "Case #" << i << ": " << solve () << "\n";
	}
              
	return 0;
}