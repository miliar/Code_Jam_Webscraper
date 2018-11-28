#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <ctime>
#include <cstring>
#include <cassert>
#include <bitset>
#include <sstream>
#include <queue>

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define sz(a) ((int) (a).size())
#define eprintf(...) fprintf(stderr, __VA_ARGS__)

using namespace std;

typedef long long int64;
typedef long double ldb;

const long double eps = 1e-9;
const int inf = (1 << 30) - 1;
const long long inf64 = ((long long)1 << 62) - 1;
const long double pi = acos(-1);

template <class T> T sqr (T x) {return x * x;}
template <class T> T abs (T x) {return x < 0 ? -x : x;}

long long TimeLeft(long long hd, long long cur_hd, long long ak, long long moves) {
	long long init_moves = moves;
	if ((moves - 1) * ak < cur_hd) {
		return moves;
	}

	moves -= (cur_hd - 1) / ak;
	if ((hd - 1) / ak <= 1) {
		return inf64;
	}

	long long delta = (hd - 1) / ak - 1;
	return 1 + (moves - 2) / delta + init_moves; 
}

int main () {
    ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tc;
	cin >> tc;
	for (int ti = 0; ti < tc; ++ti) {
		clock_t tStart = clock();

	    long long hd, ad, hk, ak, b, d;
	    cin >> hd >> ad >> hk >> ak >> b >> d;

	    if (ad >= hk) {
	    	cout << "Case #" << ti + 1 << ": " << 1 << endl;
	    	continue;
	    }

	    if (ak - d >= hd) {
	    	cout << "Case #" << ti + 1 << ": " << "IMPOSSIBLE" << endl;
	    	continue;
	    }

	    if (ak < hd && max(2 * ad, ad + b) >= hk) {
        	cout << "Case #" << ti + 1 << ": " << 2 << endl;
	    	continue;
	    }

	    if (2 * ak - 3 * d >= hd) {
	    	cout << "Case #" << ti + 1 << ": " << "IMPOSSIBLE" << endl;
	    	continue;
	    }

	    long long moves = (hk + ad - 1) / ad;
	    if (b > 0) {
	    	long long y_best = (sqrt(b * hk) - ad) / b;
	    	for (long long y = max(0LL, y_best - 100); y < max(0LL, y_best + 100); ++y) {
	    		moves = min(moves, (hk + y * b + ad - 1) / (y * b + ad) + y);
	    	}
	    }

	    long long res = TimeLeft(hd, hd, ak, moves);
	    
	    if (d > 0) {
	    	long long cur_hd = hd;
	    	long long time_first = 0;
	    	while (true) {
	    		if (cur_hd <= ak - d) {
	    			++time_first;
	    			cur_hd = hd - ak;
	    		}

	    		++time_first;
	    		ak = max(0LL, ak - d);
	    		cur_hd -= ak;
	    		long long new_res = time_first + TimeLeft(hd, cur_hd, ak, moves);

	    		res = min(res, new_res);
	 	    	
	 	    	if (ak == 0) {
	    			break;
	    		}
	    	}
	    }

		cerr << ti << " " << (double)(clock() - tStart)/CLOCKS_PER_SEC << "s." << endl;
        cout << "Case #" << ti + 1 << ": " << res << endl;
	}

	
	return 0;
}
