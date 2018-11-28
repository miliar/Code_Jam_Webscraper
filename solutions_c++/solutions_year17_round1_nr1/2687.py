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

vector<vector<int>>solve(vector<vector<int>>a, int R, int C) {
	auto ans = a;
	auto searched = a;
	rep(i, R)rep(j, C)searched[i][j] = 0;
	rep(i, R)rep(j, C)if (searched[i][j] == 0 && ans[i][j] != 0) {

		int maxnum[5] = { 1,0,0,0,0 };
		for (int upper = 0; 0 <= i - upper && searched[i - upper][j] == 0; upper++) {
			for (int lower = 0; i + lower < R && searched[i + lower][j] == 0; lower++) {
				for (int left = 0; 0 <= j - left && searched[i][j - left] == 0; left++) {
					for (int right = 0; j + right < C && searched[i][j + right] == 0; right++) {
						int scale = (upper + lower + 1)*(right + left + 1);
						if (scale <= maxnum[0])continue;
						bool flag = true;
						for (int y = i - upper; y <= i + lower; y++) {
							for (int x = j - left; x <= j + right; x++) {
								if (ans[y][x] != 0 && abs(y-i)+abs(x-j) != 0) {
									flag = false;
									break;
								}
							}
							if (flag == false)break;
						}
						if (flag == true) {
							maxnum[0] = scale;
							maxnum[1] = upper;
							maxnum[2] = lower;
							maxnum[3] = left;
							maxnum[4] = right;
						}
					}
				}
			}
		}
		for (int y = i - maxnum[1]; y <= i + maxnum[2]; y++) {
			for (int x = j - maxnum[3]; x <= j + maxnum[4]; x++) {
				ans[y][x] = ans[i][j];
				searched[y][x] = 1;
			}
		}
		int ttt = 1;
	}
	return ans;
}

signed main() {
	cin.tie(0);
	ios::sync_with_stdio(false);

	int T;
	cin >> T;

	for(int num = 1; num <= T; num++) {
		int R, C;
		cin >> R >> C;
		vector<string>g(R);
		rep(i, R)cin >> g[i];

		vector<vector<int>>p(R, vector<int>(C, 0));
		rep(i, R)rep(j, C) {
			if (g[i][j] != '?')p[i][j] = g[i][j] + 1 - 'A';
		}
		auto ans = solve(p, R, C);
		
		cout << "case #" << num << ":" << endl;
		rep(i, R) {
			rep(j, C)cout << char('A' + ans[i][j] - 1);
			cout << endl;
		}
	}

	return 0;
}

