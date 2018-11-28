#include <iostream>
#include <queue>
using namespace std;

int main() {
	int N;
	cin >> N;
	for (int I = 1; I <= N; ++I) {
		bool p = 1;
		cout << "Case #" << I << ": ";
		string s;
		cin >> s;
		int asc = 0;
		for (int i = 0; i < s.size(); ++i) {
			if (s[i] < s[asc]) {
				for (int j = 0; j < s.size(); ++j) {
					if (j < asc) cout << s[j];
					if (j == asc and (j or s[j] != '1')) cout << s[j]-'0'-1;
					if (j > asc) cout << 9;
				}
				p = 0;
				break;
			}
			if (s[i] > s[asc]) asc = i;
		}
		if (p) cout << s;
		cout << endl;
	}
	
}
