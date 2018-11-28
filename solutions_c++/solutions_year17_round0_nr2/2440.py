#include <bits\stdc++.h>

using namespace std;

typedef long long ll;
#define N int(1e3+5)

int main() {
	ifstream cin("B-large.in");
	ofstream cout("output.txt");
	int t, n;
	string s;
	cin >> t;
	for (int test = 1; test <= t; test++) {
		cin >> s;
		n = s.length();
		for (int i = n - 1; i > 0; i--) {
			if (s[i - 1] > s[i]) {
				s[i - 1]--;
				for (int j = i; j < n; j++)
					s[j] = '9';
			}
		}
		int i = 0;
		while (i < n - 1 && s[i] == '0')
			i++;
		cout << "Case #" << test << ": ";
		while (i < n)
			cout << s[i++];
		cout << endl;
	}
}