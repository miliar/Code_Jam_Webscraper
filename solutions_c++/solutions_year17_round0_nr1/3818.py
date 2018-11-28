#include<bits/stdc++.h>
using namespace std;
int t, ans, k, len, cnt;
string str;
int relax(int pos) {
	int curr = pos;
	while (str[curr--] == '+') {
	}
	return (curr + 1);
}
int flip(int pos) {
	int i;
	if (pos < k - 1)
		return -1;
	for ( i = pos; i > pos - k ; i--) {
		str[i] = (str[i] == '-') ? '+' : '-';
	}
	return (i + 1);
}

int main() {
	ios_base::sync_with_stdio(false), cin.tie(0), cout.tie(0);
// #ifndef ONLINE_JUDGE
// 	freopen("input.txt", "r", stdin);
// 	freopen("output.txt", "w", stdout);
// #endif
	cin >> t;

	for (int i = 1 ; i <= t ; i++)
	{
		cnt = 0;
		ans = 0;
		cin >> str;
		cin >> k;
		len = str.length();
		int at;
		at = len - 1;
		while (str[at--] == '+') {
		}
		at += 1;
		while (at != 0) {
			if (at == 0)
				break;
			at = flip(at);
			if (at == -1)
				break;
			at = relax(len - 1);
			ans += 1;
		}
		at = 0;
		int temp = 0;
		for (int i = 0 ; i < k ; i++) {
			if (str[i] == '-') {
				temp += 1;
			}
		}
		if (temp == k) {
			for (int i = 0 ; i < k ; i++) {
				str[i] = '+';
			}
			ans += 1;
		}
		for (int i = 0 ; i < len; i++) {
			if (str[i] == '+') {
				cnt += 1;
			}
		}
		if (cnt != len ) {
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << "\n";
		}
		else
			cout << "Case #" << i << ": " << ans << "\n";
	}
	return 0;
}