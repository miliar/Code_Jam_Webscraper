#include <iostream>
#include <fstream>

using namespace std;
int main() {
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	freopen("in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, counter = 1;
	cin >> t;
	while (t--) {
		string s;
		int k;
		cin >> s >> k;
		int ans = 0;
		bool flag = 0;
		for (int i = 0; i < (int) s.size(); i++) {
			if (s[i] == '-') {
				if (i + k <= (int) s.size()) {
					for (int j = i; j < i + k; j++) {
						if (s[j] == '-')
							s[j] = '+';
						else
							s[j] = '-';
					}
				} else {
					flag = 1;
					break;
				}
				ans++;
			}
		}
		cout << "Case #" << counter << ": ";
		if (flag)
			cout << "IMPOSSIBLE";
		else
			cout << ans;
		cout << "\n";
		counter++;
	}
}
