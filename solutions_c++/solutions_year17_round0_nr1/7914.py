#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <numeric>
#include <map>

#pragma warning(disable:4996)
using namespace std;

int T, K;
string S;

int main(void)
{
	freopen("./GoogleCodeJam/Input/A-large.in", "r", stdin);
	freopen("./GoogleCodeJam/Output/A-large_ans.txt", "w", stdout);
	cin >> T;

	for (int t = 0; t < T; ++t){
		cin >> S >> K;
		string ans = "";
		for (int i = 0; i < S.size(); ++i)
			ans += '+';

		int ret = 0;
		for (int i = 0; i < S.size() - K + 1; ++i) {
			if (S[i] == '-') {
				for (int j = i; j < i  + K; ++j) {
					if (S[j] == '-') S[j] = '+';
					else S[j] = '-';
				}
				ret++;
			}
		}

		if (S == ans)
			cout << "Case #" << t + 1 << ": " << ret << endl;
		else
			cout << "Case #" << t + 1 << ": " << "IMPOSSIBLE" << endl;
	}
}