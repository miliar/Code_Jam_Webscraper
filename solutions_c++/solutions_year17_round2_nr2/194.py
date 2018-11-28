#include <bits/stdc++.h>

using namespace std;

string str = "RYBGVO";

string Solve() {
	vector<int> have(3), inv(3);

	cin >> have[0] >> inv[2] >> have[1] 
		>> inv[0] >> have[2] >> inv[1];


	vector<vector<string>> shits(3);



	for(int i = 0; i < 3; ++i)
		for(int j = 0; j < have[i]; ++j)
			shits[i].push_back(string() + str[i]);

	for(int i = 0; i < 3; ++i) {
		for(int j = 0; j < inv[i]; ++j) {
			if(shits[i].size() < 2) {
				if(shits[i].size() == 1)
					return shits[i].back() + str[i + 3];
				return "IMPOSSIBLE";
			}


			string now;
			now += shits[i].back(); shits[i].pop_back();
			now += string() + str[i + 3];
			now += shits[i].back(); shits[i].pop_back();
			shits[i].push_back(now);
		}
	}


	vector<int> I(3);
	for(int i = 0; i < 3; ++i) {
		I[i] = i;
	}

	for(int i = 0; i < 3; ++i) {
		cerr << shits[i].size() << " ";
	}
	cerr << endl;

	while(true) {
		sort(I.begin(), I.end(), [&](int a, int b) {
			return shits[a].size() > shits[b].size();
		});

		if(shits[I.back()].size() == 0) { 
			I.pop_back();
			continue;
		}

		cerr << ".";

		if(shits[I.front()].size() == shits[I.back()].size()) {
			// OK
			cerr << "!";

			if(I.size() == 1) { 
				if(shits[I[0]].size() != 1 || shits[I[0]][0].size() != 1)
					return "IMPOSSIBLE";
				return shits[I[0]][0];
			}

			int at = 0;
			string ret = "";
			while(true) {
				if(shits[I[at]].empty()) 
					break;
				
				ret += shits[I[at]].back();
				shits[I[at]].pop_back();
				at = (at + 1) % I.size();
			}

			return ret;
		} else {
			assert(shits[I.front()].size() >= 2);
			assert(shits[I.back()].size() >= 1);

			string now;
			now += shits[I[0]].back(); shits[I[0]].pop_back();
			now += shits[I[1]].back(); shits[I[1]].pop_back();
			now += shits[I[0]].back(); shits[I[0]].pop_back();
			shits[I[0]].push_back(now);
		}
	}
}

int main() {
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; ++tt) {
		int n;
		cin >> n;
		string ret = Solve();
		if(ret != "IMPOSSIBLE" && ret.size() != n) ret = "IMPOSSIBLE";

		cout << "Case #" << tt << ": " << ret << endl;
		cerr << "Done case #" << tt << endl;
	}
	return 0;
}