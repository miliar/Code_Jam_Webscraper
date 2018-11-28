#include <bits/stdc++.h>

using namespace std;

string s;
void changeFromIndex(int index, char v) {
	for (int i = index; i < s.size(); ++i) {
		if (i == index) s[i] = v;
		else s[i] = '9';
	}
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("respblg", "w", stdout);
	int t;
	cin >> t;
	for (int k = 0; k < t; ++k) {
		string temp;
		cin >> temp;
		s = "";
		int index = 0;
		while(temp[index] == '0') index++;
		for (int i = index; i < temp.size(); ++i) {
			s += temp[i];
		}

		//solve
		bool flag = false;
		for (int i = s.size() - 2; i >= 0; --i) {
			if (s[i] > s[i + 1]) {
				while(s[i] == '0') --i;
				changeFromIndex(i, s[i] - 1);
			}
		}

		printf("Case #%d: ", k + 1);
		index = 0;
		while(s[index] == '0') index++;
		for (int i = index; i < s.size(); ++i) {
			printf("%c", s[i]);
		}
		printf("\n");
	}
	return 0;
}
