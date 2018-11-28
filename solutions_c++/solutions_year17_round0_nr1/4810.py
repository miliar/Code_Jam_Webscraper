#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	int testCnt;
	cin >> testCnt;
	for (int testNum = 1; testNum <= testCnt; testNum++) {
		cout << "Case #" << testNum <<": ";
		string str;
		int k;
		cin >> str;
		cin >> k;
		int ans = 0;
		for (int i = 0; i < str.length() - k + 1; i++) {
			if (str[i] == '-') {
				ans++;
				for (int j = 0; j < k; j++) {
					if (str[i + j] == '-')
						str[i + j] = '+';
					else
						str[i + j] = '-';
				}
			}
		}
		for (int i = 0; i < k - 1; i++) {
			if (str[str.length() - i - 1] == '-') { 
				ans = -1;
				break;
			}
		}
		if (ans == -1) {
			cout << "IMPOSSIBLE" << endl;
		}
		else {
			cout << ans << endl;
		}
	}
	return 0;
}