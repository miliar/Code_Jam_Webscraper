#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

char convert(char x) {
	if (x == '-') return '+';
	else return '-';
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t; cin >> t;

	for(int tc = 1 ; tc <= t ; tc++){
		string x, y; int n;
		cin >> x >> n;
		y = x;

		for (int i = 0; i < y.length() / 2; i++) 
			swap(y[i], y[y.length() - 1 - i]);

		bool p1 = true, p2 = true;
		int ans1 = 0, ans2 = 0;

		for (int i = 0; i < x.length(); i++) {
			if (x[i] == '-' && i + n <= x.length()) {
				ans1++;
				for (int j = i; j < i + n; j++) {
					x[j] = convert(x[j]);
				}
			}
		}

		for (int i = 0; i < y.length(); i++) {
			if (y[i] == '-' && i + n <= y.length()) {
				ans2++;
				for (int j = i; j < i + n; j++) {
					y[j] = convert(y[j]);
				}
			}
		}

		for (int i = 0; i < x.length(); i++) 
			if (x[i] == '-') p1 = false;
		for (int i = 0; i < x.length(); i++)
			if (y[i] == '-') p2 = false;

		cout << "Case #" << tc << ": ";
		if ((!p1)&(!p2)) cout << "IMPOSSIBLE\n";
		else if ((!p1)&(p2)) cout << ans2 << endl;
		else if ((p1)&(!p2)) cout << ans1 << endl;
		else cout << min(ans2, ans2) << endl;

	}

}