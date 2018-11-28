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


void solve(int tt, int x) {
	cout << "Case #" << tt << ": " << x / 2 << " " << (x - 1) / 2 << endl;
}

signed main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int maxnum = 1;
	rep(i, 18)maxnum *= 10;

	int T;
	cin >> T;
	for(int tt = 1; tt <= T; tt++) {
		int N, K;
		cin >> N >> K;

		int lower = N, NumL = 1, NumU = 0;

		while (true) {
			if (K <= NumU) {
				int ans = lower + 1;
				cout << "Case #" << tt << ": " << ans / 2 << " " << (ans - 1) / 2 << endl;
				break;
			}
			else K -= NumU;
			if (K <= NumL) {
				int ans = lower;
				cout << "Case #" << tt << ": " << ans / 2 << " " << (ans - 1) / 2 << endl;
				break;
			}
			else K -= NumL;

			int newL = (lower - 1) / 2, newNL = 0, newNU = 0;
			if (lower == 2) {
				newL = 1;
				newNL = NumL + NumU * 2;
			}
			else {
				if (lower % 2) {
					newNL = NumL * 2 + NumU;
					newNU = NumU;
				}
				else {
					newNL = NumL;
					newNU = NumL + NumU * 2;
				}
			}
			lower = newL;
			NumL = newNL;
			NumU = newNU;
		}


	}

	return 0;
}