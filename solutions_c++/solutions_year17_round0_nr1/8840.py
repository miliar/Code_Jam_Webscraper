#include <iostream>
#include <stack>
#include <string>

using namespace std;

void flip(char* s, int k);

int main() {
	cin.sync_with_stdio(false);
	int t;
	cin >> t;
	for(int num = 1 ; num <= t ; ++num) {
		string s;
		int k, cnt = 0;
		cin >> s >> k;

		for (int i = 0; i < s.size(); ++i) {
			if (s[i] == '-') {
				if (i + k <= s.size()) {
					flip(&s[i], k);
					cnt++;
				}
				else {
					cnt = -1;
					break;
				}
			}
		}
		if(cnt != -1)
			cout << "Case #" << num << ": " << cnt << "\n";
		else
			cout << "Case #" << num << ": IMPOSSIBLE\n";
	}

	return 0;
}

void flip(char* s, int k) {
	for (int i = 0; i < k; ++i) {
		if (s[i] == '+')	s[i] = '-';
		else s[i] = '+';
	}
}
