#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int T, K;
	string str;
	cin >> T;
	getline(cin, str);
	for (int t = 1; t <= T; ++t) {
		cin >> str;
		cin >> K;
		const int S = (str.size());
		vector<int> sum(S, 0);
		sum[0] = str[0] == '-';
		int res = sum[0];
		bool ok = true;
		for (int c = 1; c < S; ++c) {
			int prev_sum = c >= K ? sum[c - K] : 0;
			sum[c] = sum[c - 1];
			bool cur_flip = (sum[c] - prev_sum) & 1 == 1;
			bool need_flip = str[c] == '-';
			int flip = cur_flip != need_flip;
			if (c <= S - K)
				sum[c] += flip;
			else if (flip == 1) {
				ok = false;
			}
			res += flip;
		}
		getline(cin, str);
		cout << "Case #" << t << ": ";
		if (!ok) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << res << endl;
		}
	}
	return 0;
}