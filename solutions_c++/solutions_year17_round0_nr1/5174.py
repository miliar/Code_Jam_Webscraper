#include <iostream>
#include <string>
using namespace std;

int solve(string s, int k) {
	int c[2000] = {}; int a = 0; int l = s.length();

	for (int i = 0; i < l; i++) {
		if (s[i] == '-')c[i] = 1;
	}

	for (int i = 0; i <= l - k; i++) {
		if (c[i] % 2 != 0) {
			for (int j = 0; j < k; j++) {
				c[i + j] ++;
			}
			a++;
		}
	}
	for (int i = l - k; i < l; i++) {
		if (c[i] % 2 != 0) return -1;
	}

	return a;


}

void output(int num, int arg) {
	if(arg >= 0)
		cout << "Case #" << num << ": " << arg << endl;
	else
		cout << "Case #" << num << ": " << "IMPOSSIBLE" << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		int k; string s;
		cin >> s >> k;
		output(i, solve(s, k));
	}
}