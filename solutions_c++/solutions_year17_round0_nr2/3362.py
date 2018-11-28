#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

bool is_good(string s) {
	for (int i = 0; i < s.size()-1; i++) {
		if (s[i+1] < s[i]) return 0;
	}

	return 1;
}

int main() {
	int t;
	cin >> t;

	int c = 1;
	while (t--) {
		string s;
		cin >> s;
		string a = s;


		while(!is_good(s)) {
			for (int i = 0; i < s.size()-1; i++) {
				if (s[i] > s[i+1]) {
					for (int j = i+1; j < s.size(); j++) {
						s[j] = '9';
					}
					s[i]--;
					break;
				}
			}
		}

		cout << "Case #" << c++ << ": ";
		
		bool flag = 0;
		for (int i = 0; i < s.size(); i++) {
			if (!flag and s[i] == '0') continue;
			flag = 1;
			cout << s[i];
		}

		cout << endl;
	}

}
