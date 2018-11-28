#include <bits/stdc++.h>

using namespace std;

int main () {
	int test, cnt = 0;
	cin >> test;
	while (test--) {
		cnt++;
		printf("Case #%d: ", cnt);
		
		string x;
		cin >> x;
		int len = x.length();
		for (int i = len - 2; i >= 0; i--) {
			if (x[i] <= x[i + 1])
				continue;
			x[i] = x[i] - 1;
			for (int j = i + 1; j < len; j++)
				x[j] = '9';
		}
		int pos = 0;
		for (int i = 0; i < len; i++)
			if (x[i] != '0') {
				pos = i;
				break;
			}
		for (int i = pos; i < len; i++)
			cout << x[i];
		cout << endl;
	}	
	return 0;
}