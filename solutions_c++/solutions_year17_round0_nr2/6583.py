#include <bits/stdc++.h>

using ll = long long;
using ull = unsigned long long;
using std::cout;
using std::cin;

void solve(int t) {
	std::string str, ans;
	cin >> str;
	if (std::is_sorted(str.begin(), str.end())) {
		ans = str;
	}
	else {
		std::vector<int> diff(str.size(), 1000);
		int index = 1;
		for (; index < str.size(); index++) {
			if (str[index - 1] <= str[index]) {
				diff[index] = str[index] - str[index - 1];
			}
			else
				break;
		}
		index--;
		ans = str;
		while (index > 0 && diff[index] == 0)
			index--;
		// cout << index << "\n";
		ans[index]--;
		for (int i = index + 1; i < str.size(); i++)
			ans[i] = '9';
	}
	cout << "Case #" << t << ": " << std::stoll(ans) << "\n";
}

int main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		solve(t + 1);
	}
	return 0;
}

/***

4
132
1000
7
111111111111111110

***/