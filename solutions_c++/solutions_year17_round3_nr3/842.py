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

const int MAXN = 55;
const double EPS = 1e-8;

double p[MAXN], tmp[MAXN];
int n, Need;
double u;

double solve () {
    cin >> n >> Need >> u;
    double total = u, mean;
    for (int i = 0; i < n; i++) {
    	cin >> p[i];
    	total += p[i];
    }
    mean = total / n;	
    int cnt = 0;
    double ans = 1.0;
    for (int i = 0; i < n; i++) {
    	if (mean - p[i] > EPS) {
    		tmp[cnt++] = p[i];
    	} else {
    		ans *= p[i];
    	}
    }
    tmp[cnt++] = mean;
    sort (tmp, tmp + cnt);
	for (int i = 1; i < cnt; i++) {
		total = u;
		for (int j = 0; j < i; j ++) {
			total += tmp[j];	
		}
		mean = min (tmp[i], total / i);
		for (int j = 0; j < i; j ++) {
		   	if (u > EPS && mean - tmp[j] > EPS) {
		    	u -= mean - tmp[j];
				tmp[j] = mean;                       
			}
		}
	} 
	for (int i = 0; i < cnt - 1; i++) {
//		cerr << tmp[i] << " ";
		ans *= tmp[i];
	}
//	cerr << "\n" << "u == " << fixed << " " << u << "\n";
	return ans;
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
		cout << "Case #" << i << ": " << fixed << setprecision (8) << solve() << "\n";
	}
              
	return 0;
}