#include <iostream>
#include <fstream>
#include <string>
#include <array>
#include <forward_list>
#include <list>
#include <vector>
#include <bitset>
#include <chrono>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <deque>
#include <stack>
#include <limits>
#include <algorithm>
#include <numeric>
#include <utility>
#include <random>
#include <complex>
#include <tuple>
#include <functional>

using namespace std;


vector<string> cretate(int C, string s) {
	vector<string> res;
	for (int i = 0; i < C; i++) res.push_back(s);
	return res;
}

int get_next(vector<vector<string>> & data, vector<string> & line, int N) {
	
	static map<string, set<string>> rels = {
		{"R", {"G", "B", "Y"}},
		{"B", {"O", "R", "Y"}},
		{"Y", {"V", "R", "B"}},
		{"G", {"R"}},
		{"O", {"B"}},
		{"V", {"Y"}}
	};

	sort(data.begin(), data.end(), [&line](auto & d1, auto & d2) {
		if (d1.size() == d2.size() && d1.size() > 0 && line.size() > 0) {
	 		return rels[d1[0]].find(line[0]) == rels[d1[0]].end();
	 	}
	 	return d2.size() < d1.size();
	});
	if (data[0].empty()) return -1;
	if (line.empty()) {
		return 0;
	}
	string s = line[line.size() - 1];
	string s0 = line[0];
	for (size_t i = 0; i < data.size(); i++) {
		if (line.size() == (N - 1) && !data[i].empty()) {
			if (rels[data[i][0]].find(s0) != rels[data[i][0]].end() &&
			 rels[data[i][0]].find(s) != rels[data[i][0]].end()) return i;
		}
		else {
			if (!data[i].empty())
				if (rels[data[i][0]].find(s) != rels[data[i][0]].end()) return i;
		}
	}
	return -2;
}

void solve(int ti) {
	int N, R, O, Y, G, B, V;
	cin >> N >> R >> O >> Y >> G >> B >> V;
	
	vector<vector<string>> data(3);
	data[0] = cretate(R, "R");
	data[1] = cretate(Y, "Y");
	data[2] = cretate(B, "B");
	//data[3] = cretate(G, "G");
	//data[4] = cretate(O, "O");
	//data[5] = cretate(V, "V");

	vector<string> line;
	while(true) {
		int i = get_next(data, line, N);
		if (i == -1) break;
		if (i == -2) {
			line.clear();
			break;
		}
		line.push_back(data[i][0]);
		data[i].erase(data[i].begin());
	}
	if (line.empty()) cout << "IMPOSSIBLE";
	else for (auto v : line) cout << v;
}

int main() {
	int t; cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve(i);
		cout << endl;
	}
}
