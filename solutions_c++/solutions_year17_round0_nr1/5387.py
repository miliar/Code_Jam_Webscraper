#include <iostream>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <functional>
#include <limits>

#include <cstdio>
#include <cmath>

using namespace std;

int main(void) {
	int32_t T;
	cin >> T;

	for (auto tc = 1; tc <= T; tc++) {
		string S;
		int32_t K;

		cin >> S >> K;

		string complete;
		for (auto i = 0; i < S.size(); i++) {
			complete.push_back('+');
		}

		bool is_impossible = true;
		int32_t result = 0;

		priority_queue< pair<int32_t, string>, vector< pair<int32_t, string> >, greater< pair<int32_t, string> > > PQ;
		set<string> dup_chk;

		PQ.push(make_pair(0, S));

		while (!PQ.empty()) {
			string str = PQ.top().second;
			int32_t depth = PQ.top().first;
			PQ.pop();

			if (str == complete) {
				is_impossible = false;
				result = depth;
				break;
			}

			if (dup_chk.find(str) != dup_chk.end()) {
				continue;
			}
			dup_chk.insert(str);

			for (auto i = 0; i <= str.size() - K; i++) {
				string tmp = str;
				bool is_valid = false;

				for (auto j = i; j < i + K; j++) {
					if (tmp[j] == '-') {
						tmp[j] = '+';
						is_valid = true;
					}
					else {
						tmp[j] = '-';
					}
				}

				if (is_valid && dup_chk.find(tmp) == dup_chk.end()) {
					PQ.push(make_pair(depth + 1, tmp));
				}
			}
		}

		if (is_impossible) {
			cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
		}
		else {
			cout << "Case #" << tc << ": " << result << endl;
		}
	}

	return 0;
}
