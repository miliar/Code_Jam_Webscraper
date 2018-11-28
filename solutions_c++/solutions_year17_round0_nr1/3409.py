#include <iostream>
#include <string>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
	int nn;
	cin >> nn;
	for (int i = 0; i < nn; i++) {
		string s;
		int n;
		cin >> s >> n;
		int sz = s.size();
		vector<int> cc(sz, 0);
		for (int j = 0; j < sz; j++) {
			if (s[j] == '+') {
				cc[j] = 1;
			}
		}
		vector<int> d(sz + 1, 0);
		int a = 0;
		int c = 0;
		for (int j = 0; j < sz; j++) {
			a += d[j];
			cc[j] += a;
			cc[j] %= 2;
			if (cc[j] == 0 && j+n <= sz) {
				a++;
				cc[j] = 1;
				d[j + n] = -1;
				c++;
			}
			//cout << a << ' ' << d[j] << endl;
		}
		bool h = true;
		for (int j = 0; j < sz; j++) {
			if (cc[j] == 0) {
				h = false;
				break;
			}
		}
		printf("Case #%d: ", i + 1);
		if (h) {
			printf("%d\n", c);
		}
		else {
			printf("IMPOSSIBLE\n");
		}
	}
	return 0;
}