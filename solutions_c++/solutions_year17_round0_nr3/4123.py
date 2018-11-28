#include <iostream>
#include <fstream>
#include <vector>
#include <utility>
#include <map>

using namespace std;

class Solution {
public:
	pair<long long, long long> solve(long long N, long long K) {

		map<long long, long long> mp;

		mp[N] = 1;

		while (true) {

			auto ite = --mp.end();
			auto l = ite->first;
			auto c = ite->second;

			if (K > c) {
				K -= c;
				mp.erase(ite);
				add(mp, (l - 1) / 2, c);
				add(mp, l / 2, c);
			} else {
				return make_pair(l / 2, (l - 1) / 2);
			}
		}
	}
private:
	void add(map<long long, long long> &mp, long long key, long long val) {
		if (mp.find(key) == mp.end()) {
			mp[key] = val;
		} else {
			mp[key] += val;
		}
	}
};

int main() {

	Solution solution;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T;
	long long N, K;

	fin >> T;

	for (int i = 0; i < T; ++i) {
		fin >> N >> K;

		auto res = solution.solve(N, K);

		fout << "Case #" << i + 1 << ": " << res.first << " " << res.second << endl;
	}

	return 0;
}
