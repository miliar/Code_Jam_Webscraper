#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
#include <tuple>
#include <queue>
#include <utility>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <limits>
#include <new>
#include <functional>
#include <unordered_map>
#include <unordered_set>
#include <random>
#include <chrono>
#include <thread>

const double pi = 3.1415926535897932384626433832795;

using namespace std;

typedef long long ll;

void get_all_options(vector<vector<int>>& opts, int n) {
	switch (n) {
	case 1:
		opts[0] = { 0 };
		break;
	case 2:
		for (int i1 = 0; i1 < n; i1++) {
			for (int i2 = 0; i2 < n; i2++) {
				opts[i1 * n + i2] = { i1, i2 };
			}
		}
		break;
	case 3:
		for (int i1 = 0; i1 < n; i1++) {
			for (int i2 = 0; i2 < n; i2++) {
				for (int i3 = 0; i3 < n; i3++) {
					opts[i1 * n * n + i2 * n + i3] = { i1, i2, i3 };
				}
			}
		}
		break;
	case 4:
		for (int i1 = 0; i1 < n; i1++) {
			for (int i2 = 0; i2 < n; i2++) {
				for (int i3 = 0; i3 < n; i3++) {
					for (int i4 = 0; i4 < n; i4++) {
						opts[i1 * n * n * n + i2 * n * n + i3 * n + i4] = { i1, i2, i3, i4 };
					}
				}
			}
		}
		break;
	case 5:
		for (int i1 = 0; i1 < n; i1++) {
			for (int i2 = 0; i2 < n; i2++) {
				for (int i3 = 0; i3 < n; i3++) {
					for (int i4 = 0; i4 < n; i4++) {
						for (int i5 = 0; i5 < n; i5++) {
							opts[i1 * n * n * n * n + i2 * n * n * n + i3 * n * n + i4 * n + i5] = { i1, i2, i3, i4, i5 };
						}
					}
				}
			}
		}
		break;
	case 6:
		for (int i1 = 0; i1 < n; i1++) {
			for (int i2 = 0; i2 < n; i2++) {
				for (int i3 = 0; i3 < n; i3++) {
					for (int i4 = 0; i4 < n; i4++) {
						for (int i5 = 0; i5 < n; i5++) {
							for (int i6 = 0; i6 < n; i6++) {
								opts[i1 * n * n * n * n  * n + i2 * n * n * n * n + i3 * n * n * n + i4 * n * n + i5 * n + i6] = { i1, i2, i3, i4, i5, i6 };
							}
						}
					}
				}
			}
		}
		break;
	}
}

bool neigh(int left, int center, int right) {
	if (abs(left - center) % 5 <= 1) return false;
	if (abs(right - center) % 5 <= 1) return false;
	return true;
}

bool is_perm(vector<int>& in) {
	vector<int> count(in.size(), 0);
	for (auto x : in) {
		if (++count[x] > 1) return false;
	}
	return true;
}

string test(int* u, int n) {
	string types = "ROYGBV";
	vector<int> unis;
	for (int i = 0; i < 6; i++) {
		for (int j = 0; j < u[i]; j++) {
			unis.push_back(i);
		}
	}
	int fact = 1;
	for (int i = 1; i <= unis.size(); i++) {
		fact *= unis.size();
	}
	vector<vector<int>> options(fact);
	get_all_options(options, n);
	vector<vector<int>> perms;
	for (int i = 0; i < options.size(); i++) {
		if (is_perm(options[i])) {
			perms.push_back(options[i]);
			/*for (int j = 0; j < n; j++) {
				cout << options[i][j] << (j != n - 1 ? ' ' : '\n');
			}*/
		}
	}
	for (int i = 0; i < perms.size(); i++) {
		vector<int> pos(n);
		for (int j = 0; j < n; j++) {
			pos[j] = unis[perms[i][j]];
		}
		bool ok = true;
		for (int j = 0; j < n; j++) {
			if (!neigh(pos[(j - 1 >= 0 ? j - 1 : n - 1)], pos[j], pos[(j + 1) % n])) {
				ok = false;
				break;
			}
		}
		if (ok) {
			string result;
			for (int j = 0; j < n; j++) {
				result += types[pos[j]];
			}
			return result;
		}
	}
	return "IMPOSSIBLE";
}

string test_end(int end, int begin, int* u, int n) {
	string types = "ROYGBV";
	vector<int> unis;
	for (int i = 0; i < 6; i++) {
		for (int j = 0; j < u[i]; j++) {
			unis.push_back(i);
		}
	}
	//cout << unis.size() << endl;
	int fact = 1;
	for (int i = 1; i <= unis.size(); i++) {
		fact *= unis.size();
	}
	vector<vector<int>> options(fact);
	get_all_options(options, n);
	vector<vector<int>> perms;
	for (int i = 0; i < options.size(); i++) {
		if (is_perm(options[i])) {
			perms.push_back(options[i]);
			/*for (int j = 0; j < n; j++) {
			cout << options[i][j] << (j != n - 1 ? ' ' : '\n');
			}*/
		}
	}
	for (int i = 0; i < perms.size(); i++) {
		vector<int> pos(n);
		for (int j = 0; j < n; j++) {
			pos[j] = unis[perms[i][j]];
		}
		bool ok = true;
		for (int j = 0; j < n; j++) {
			if (!neigh((j - 1 >= 0 ? pos[j - 1] : begin), pos[j], (j + 1 >= n ? end : pos[j + 1]))) {
				ok = false;
				break;
			}
		}
		if (ok) {
			string result;
			for (int j = 0; j < n; j++) {
				result += types[pos[j]];
			}
			return result;
		}
	}
	return "IMPOSSIBLE";
}

int main(void) {
	cin.tie(nullptr);
	cin.sync_with_stdio(false);

	int t;
	cin >> t;
	string types = "ROYGBV";
	for (int i = 1; i <= t; i++) {
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		int u[6] = { r, o, y, g, b, v };
		if (n <= 6) {
			cout << "Case #" << i << ": " << test(u, n) << endl;
			continue;
		}
		vector<int> chain;
		string output = "";
		vector<pair<int, int>> h;
		bool failed = false;
		for (int j = 0; j < n - 6; j++) {
			int mid = -1;
			h.clear();
			for (int k = 0; k < 6; k++) {
				h.push_back(make_pair(u[k], k));
			}
			sort(h.begin(), h.end(), [](auto& l, auto& r) {return l.first > r.first;});
			/*for (int k = 0; k < 6; k++) {
				cout << h[k].first << (k != 5 ? ' ' : '\n');
			}*/
			for (int k = 0; k < 6; k++) {
				if (j == 0) {
					mid = h[k].second;
					break;
				}
				if (abs(chain[j - 1] - h[k].second) % 5 > 1 && h[k].first > 0) {
					mid = h[k].second;
					break;
				}
			}
			if (mid == -1) {
				failed = true;
				break;
			}
			output += types[mid];
			u[mid]--;
			//cout << mid << endl;
			chain.push_back(mid);
		}
		if (failed) {
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
			continue;
		}
		string rs = test_end(chain[0], chain[chain.size() - 1], u, 6);
		if (rs == "IMPOSSIBLE") output = "IMPOSSIBLE";
		else output += rs;
		cout << "Case #" << i << ": " << output << endl;
	}

	return 0;
}