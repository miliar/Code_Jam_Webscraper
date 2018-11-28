#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <iomanip>
#include <limits>

using namespace std;

unordered_map<int, unordered_map<int, unordered_map<int, double>>> cache;

double eval(vector<pair<int, int>>& h, vector<int>& d, int pos, int curh, int rem) {
	if (pos == d.size()) {
		return 0;
	}

	if (cache.find(pos) != cache.end()) {
		auto tt = cache[pos];
		if (tt.find(curh) != tt.end()) {
			auto ttt = tt[curh];
			if (ttt.find(rem) != ttt.end()) {
				return ttt[rem];
			}
		}
	}

	double res = numeric_limits<double>::max();
	if (rem >= d[pos]) 
		res = eval(h, d, pos + 1, curh, rem - d[pos])+ ((double)d[pos]) / h[curh].second;
	
	if (h[pos].first >= d[pos])
		res = min(res, eval(h, d, pos + 1, pos, h[pos].first - d[pos]) + ((double)d[pos]) / h[pos].second);

	cache[pos][curh][rem] = res;

	return res;
}

int main() {
#ifdef _DEBUG
	std::ifstream in("C:\\Users\\silvio.lazzeretti\\Downloads\\C-example.txt");
	std::streambuf *cinbuf = std::cin.rdbuf(); //save old buf
	std::cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
#endif
	int T;
	cin >> T;
	int t = 0;
	while (++t <= T) {
		cache.clear();

		int N, Q;
		cin >> N >> Q;

		vector<pair<int, int>> h(N);
		for (int i = 0; i < N; ++i) {
			int E, S;
			cin >> E >> S;
			h[i] = make_pair(E, S);
		}

		vector<int> d(N-1);
		int ofs = 1;
		for (int i = 0; i < N; ++i) {
			vector<int> tmp(N);
			for (int j = 0; j < N; ++j)
				cin >> tmp[j];

			if(i<N-1)
				d[i] = tmp[ofs++];
		}

		int start, end;
		cin >> start >> end;

		double res=eval(h, d, start, 0, h[0].first-d[0])+ ((double)d[0]) / h[0].second;

		cout << "Case #" << t << ": ";
		cout << fixed << setprecision(6) << res;
		cout << endl;
	}
	return 0;
}