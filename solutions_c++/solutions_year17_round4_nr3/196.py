#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

vector <int> get_state(const vector <int> &state, string s) {
	int n = state.size();
	vector <int> nstate = state;
	bool has_vertical = false;
	for (int i = 0; i < n; ++i) {
		char c = s[i];
		if (c == '|') {
			has_vertical = true;
			for (int j = i - 1; j >= 0; --j) {
				if (s[j] == '|' || s[j] == '-')
					return {};
				if (s[j] != '.')
					break;
				s[j] = '*';
			}
			for (int j = i + 1; j < n; ++j) {
				if (s[j] == '|' || s[j] == '-')
					return {};
				if (s[j] != '.')
					break;
				s[j] = '*';
			}
		}
	}
	for (int i = 0; i < n; ++i) {
		if (s[i] == '.') {
			if (state[i] == 3)
				return {};
			if (state[i] == 0)
				nstate[i] = 1;
		}
		if (s[i] == '-') {
			if (state[i] == 3)
				return {};
			nstate[i] = 2;
			continue;
		}
		if (s[i] == '|') {
			if (state[i] == 0)
				nstate[i] = 3;
			if (state[i] == 1)
				return {};
		}
		if (s[i] == '#') {
			if (state[i] == 1)
				return {};
			nstate[i] = 0;
		}
	}
	return nstate;
}

void solve(int t) {
	int r, c;
	cin >> r >> c;
	vector <string> arr(r);
	for (int i = 0; i < r; ++i)
		cin >> arr[i];
	// 0 - no need to cover, 1 - need to cover, 2 - already beamed, 3 - mustn't beam
	vector <int> init(r, 0);
	map <vector <int>, vector <string> > result;
	result[init] = {};
	for (int i = 0; i < c; ++i) {
		map <vector <int>, vector <string> > nresult;
		int cnt = 0;
		for (int j = 0; j < r; ++j)
			if (arr[j][i] == '|' || arr[j][i] == '-')
				++cnt;
		for (const auto &p : result) {
			auto state = p.first;
			// check
			bool ok = true;
			string cur = "";
			for (int j = 0; j < r; ++j) {
				if ((arr[j][i] == '|' || arr[j][i] == '-') && state[j] == 2)
					ok = false;
				if (arr[j][i] == '#' && state[j] == 1)
					ok = false;
				cur.push_back(arr[j][i]);
			}
			if (!ok)
				continue;

			auto narr = p.second;
			if (cnt == 0) {
				narr.push_back(cur);
				auto nstate = get_state(state, cur);
				if (!nstate.empty())
					nresult[nstate] = narr;
			}
			else {
				for (int mask = 0; mask < (1 << cnt); ++mask) {
					int count = 0;
					for (int j = 0; j < r; ++j)
						if (arr[j][i] == '|' || arr[j][i] == '-') {
							if (mask & (1 << count))
								cur[j] = '-';
							else
								cur[j] = '|';
							++count;
						}
					narr.push_back(cur);
					auto nstate = get_state(state, cur);
					if (!nstate.empty())
						nresult[nstate] = narr;
					narr.pop_back();
				}
			}
			/*else if (cnt == 1) {
				for (int j = 0; j < r; ++j)
					if (arr[j][i] == '|' || arr[j][i] == '-')
						cur[j] = '-';
				narr.push_back(cur);
				auto nstate = get_state(state, cur);
				if (!nstate.empty())
					nresult[nstate] = narr;
				
				narr.pop_back();
				for (int j = 0; j < r; ++j)
					if (arr[j][i] == '|' || arr[j][i] == '-')
						cur[j] = '|';
				narr.push_back(cur);
				nstate = get_state(state, cur);
				if (!nstate.empty())
					nresult[nstate] = narr;
			}
			else {
				for (int j = 0; j < r; ++j)
					if (arr[j][i] == '|' || arr[j][i] == '-')
						cur[j] = '-';
				narr.push_back(cur);
				auto nstate = get_state(state, cur);
				if (!nstate.empty())
					nresult[nstate] = narr;
			}
			*/
		}
		result = nresult;
	}
	cout << "Case #" << t << ": ";
	vector <string> res;
	for (const auto &p : result) {
		bool ok = true;
		for (int x : p.first)
			if (x == 1)
				ok = false;
		if (ok) {
			res = p.second;
			break;
		}
	}
	if (res.empty()) {
		cout << "IMPOSSIBLE" << endl;
	}
	else {
		cout << "POSSIBLE" << endl;
		vector <string> ans(r);
		for (int i = 0; i < res.size(); ++i)
			for (int j = 0; j < res[i].length(); ++j)
				ans[j].push_back(res[i][j]);
		for (int i = 0; i < r; ++i)
			cout << ans[i] << endl;
	}
}

int main() {
	freopen("C-small-attempt2.in", "r", stdin);
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; ++t)
		solve(t);
	return 0;
}