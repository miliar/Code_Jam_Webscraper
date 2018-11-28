#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <tuple>
#include <utility>
using namespace std;

pair<int, int> solve(int N, int K) {
	vector<int> v(N + 2);
	v[0] = v.back() = 1;
	tuple<int, int, int> last;
	for (int i = 0; i < K; ++i) {
		tuple<int, int, int> best(-1, -1, -1);
		for (int j = 0; j < N + 2; ++j) {
			if (v[j]) continue;
			int LS = 0, RS = 0;
			for (int k = j - 1; k >= 0; --k) {
				if (v[k]) break;
				++LS;
			}
			for (int k = j + 1; k < N + 2; ++k) {
				if (v[k]) break;
				++RS;
			}
			best = max(best, make_tuple(min(LS, RS), max(LS, RS), -j));
		}
		v[-get<2>(best)] = 1;
		last = best;
	}
	return make_pair(get<1>(last), get<0>(last));
}

int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		int N, K;
		cin >> N >> K;
		auto p = solve(N, K);
		cout << "Case #" << test << ": " << p.first << ' ' << p.second << endl;
	}
}
