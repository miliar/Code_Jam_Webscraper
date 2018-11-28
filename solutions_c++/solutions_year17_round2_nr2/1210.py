#include <bits/stdc++.h>

using namespace std;

class Node {
	public:
		int i;
		int cnt;
		bool operator<(const Node& r) const {
			return cnt > r.cnt;
		}
};

string solve()
{
	static const char code[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};
	int n;
	vector<Node> arr;
	cin >> n;
	for (int i = 0; i < 6; i++) {
		Node n;
		n.i = i;
		cin >> n.cnt;
		arr.push_back(n);
	}
	sort(arr.begin(), arr.end());
	for (int i = 0; i < 6; i++) {
		if (arr[i].cnt * 2 > n) {
			return "IMPOSSIBLE";
		}
	}

	vector<char> ans(n);
	int pos = 0;
	for (int i = 0; i < 6; i++) {
		while (pos < n && arr[i].cnt > 0) {
			arr[i].cnt--;
			ans[pos] = code[arr[i].i];
			pos += 2;
		}
	}
	pos = 1;
	for (int i = 0; i < 6; i++) {
		while (pos < n && arr[i].cnt > 0) {
			arr[i].cnt--;
			ans[pos] = code[arr[i].i];
			pos += 2;
		}
	}
	string ret;
	for (int i = 0; i < n; i++) ret += ans[i];
	for (int i = 1; i < n; i++) {
		if (ans[i] == ans[i - 1]) {
			puts("-0-0---");
			cout << i << endl;
			cout << ans[i] << ' ' << ans [i - 1] << endl;
			throw "fuck";
		}
	}
	return ret;
}

int main()
{
	int t;
	cin >> t;
	for (int cs = 1; cs <= t; cs++) {
		cout << "Case #" << cs << ": " << solve() << endl;
	}
}
