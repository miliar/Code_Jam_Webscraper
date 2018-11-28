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

const int MAXN = 1005;
const long double EPS = 1e-10;
const long double PI = acosl (-1.0);

int was[MAXN], n, k;
long double ans;
pii cc[MAXN]; // {R, H}
pii tmp[MAXN];


bool comp (pii a, pii b) {
	long double val1 = (long double) a.first * a.second;
	long double val2 = (long double) b.first * b.second;
	if (abs (val1 - val2) < EPS) {
		if (a.first == b.first)
			return a.first < b.first;
		return a.second < b.second;
	}
	return (val2 - val1) < EPS;
}

double solve () {
	cin >> n >> k;
	//cerr << n << " " << k << "\n";
    for (int i = 0; i < n; i++) {
    	cin >> cc[i].first >> cc[i].second;
    }
    sort (cc, cc + n);
    reverse (cc, cc + n);
    /*for (int i = 0; i < n; i++) {
    	cerr << cc[i].first << " " << cc[i].second << "\n";
    }*/   
    ans = 0.0;
    for (int i = 0; i < n - k + 1; i++) {
    //	cerr << i << "\n";
    	int sz = n - i - 1;
    	long double cur = PI * cc[i].first * cc[i].first + 2.0f * PI * cc[i].first * cc[i].second;
    	for (int j = i + 1; j < n; j++) {
    		tmp [j - (i + 1)] = mp (cc[j].second, cc[j].first);			
    	}
    //	cerr << sz;
    	sort (tmp, tmp + sz, comp);
    	//cerr << "taken:\n";
    	for (int j = 0; j < k - 1; j++) {
    	//	cerr << j << "\n";
    		cur += 2.0 * PI * tmp[j].second * tmp[j].first;
    //  		cerr << tmp[j].first << " " << tmp[j].second << "\n";   		
    	}                  
    	if (cur - ans > EPS) {
    		ans = cur;
    //		cerr << ans << " " << i << "\n";
    	}
    }
    //cerr << ans << "\n";
    
    return ans;
}

int main () {
	ios_base:: sync_with_stdio (false);
	cin.tie (NULL);
#ifdef LOCAL
	freopen ("test.in", "r", stdin);
	freopen ("test.out", "w", stdout);
#endif

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": " << fixed << setprecision (8) << solve() << "\n"; 
	}
              
	return 0;
}