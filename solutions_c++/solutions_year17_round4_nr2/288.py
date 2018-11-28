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

int main () {
    ios_base::sync_with_stdio(0);
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

    int tc;
	cin >> tc;
	for (int ti = 0; ti < tc; ++ti) {
	    int n, m, k;
	    cin >> n >> m >> k;
	    
	    vector<int> num_pos(n, 0);
	    vector<int> num_pers(m, 0);
	    
	    for (int i = 0; i < k; ++i) {
	    	int pos, pers;
	    	cin >> pos >> pers;
	    	--pos, --pers;

	    	++num_pos[pos];
	    	++num_pers[pers];
	    }

	    int res = 0;
	    for (int i = 0; i < m; ++i) {
	    	res = max(res, num_pers[i]);
	    }

	    int sum = 0;
	    for (int i = 0; i < n; ++i) {
	    	sum += num_pos[i];
	    	res = max(res, (sum + i) / (i + 1));
	    }

	    int res_prom = 0;
	    for (int i = 0; i < n; ++i) {
	    	res_prom += max(0, num_pos[i] - res);
	    }
		

		cout << "Case #" << ti + 1 << ": " << res << " " << res_prom << endl;
	}

	
	return 0;
}
