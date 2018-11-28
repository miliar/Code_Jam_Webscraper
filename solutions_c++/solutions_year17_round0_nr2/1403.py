#include<iostream>
#include<iomanip>
#include<map>
#include<unordered_map>
#include<set>
#include<unordered_set>
#include<vector>
#include<array>
#include<string>
#include<stack>
#include<queue>
#include<algorithm>
#include<cassert>
#include<functional>
#include<random>
#include<complex>
#include<bitset>
#include<chrono>
//#include<boost/multiprecision/cpp_int.hpp>
#define int int64_t
#define uint uint64_t
#define REP(i, a, b) for (int64_t i = (int64_t)(a); i < (int64_t)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define SZ(X) ((int64_t)((X).size()))
#define ITR(x, a) for (auto x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())
#define Min(x) *min_element(ALL(x))
#define Max(x) *max_element(ALL(x))
#define Unique(L) (L.erase(unique(ALL(L)), L.end()))
#define intmax (std::numeric_limits<int64_t>::max() / 4)
#define doublemax (std::numeric_limits<double>::max() / 4)
using namespace std;
//typedef boost::multiprecision::cpp_int bigint;
const double EPS = 1e-9;
const double PI = acos(-1.0);



signed main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int maxnum = 1;
	rep(i, 18)maxnum *= 10;

	int T;
	cin >> T;
	rep(tt, T) {
		int N;
		cin >> N;

		if (N < 10) {
			cout << "Case #" << tt + 1 << ": " << N << endl;
			continue;
		}
		if (N == maxnum) {
			cout << "Case #" << tt + 1 << ": " << maxnum - 1 << endl;
			continue;
		}

		vector<int>d(25, 0);
		for (int i = 0, nn = N; nn; i++, nn /= 10) {
			d[i] = nn % 10;
		}
		for (int i = 21; 0 <= i; i--) {
			int upper = d[i + 1];
			int lower = d[i];
			if (lower < upper) {
				d[i + 1]--;
				for (int j = 0; j <= i; j++)d[j] = 9;
				break;
			}
		}
		for (int i = 0; i < 21; i++) {
			int upper = d[i + 1];
			int lower = d[i];
			if (lower < upper) {
				d[i + 1]--;
				d[i] = 9;
			}
		}
		int ans = 0;
		for(int i = 21; 0 <= i; i--) {
			ans *= 10;
			ans += d[i];
		}
		cout << "Case #" << tt + 1 << ": " << ans << endl;
	}

	return 0;
}