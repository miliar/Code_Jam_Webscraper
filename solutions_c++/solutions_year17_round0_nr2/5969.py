#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin >> t;
	for (int tc = 1; tc <= t; tc++) {
		string n;
		cin >> n;
		int len = n.size();
		vector<int> num(len);
		for (int i = 0; i < len; i++)
			num[i] = n[i] - '0';
		if (len == 1) {
			cout << "Case #" << tc << ": " << n << '\n';
			continue;
		}
		while (true) {
			int first = -1;
			for (int i = 1; i < len; i++) {
				if (num[i - 1] > num[i]) {
					first = i - 1;
					break;
				}
			}
			if (first == -1) {
				cout << "Case #" << tc << ": ";
				int ii = 0;
				while (num[ii] == 0) ii++;
				for (int i = ii; i < len; i++)
					cout << num[i];
				cout << '\n';
				break;
			}
			if (num[first] == 1) {
				cout << "Case #" << tc << ": ";
				for (int i = 0; i < len - 1; i++)
					cout << '9';
				cout << '\n';
				break;
			} else {
				num[first]--;
				for (int i = first + 1; i < len; i++)
					num[i] = 9;
			}
		}
	}
	return 0;
}