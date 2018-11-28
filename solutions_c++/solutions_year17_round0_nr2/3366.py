#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

int main() {
	int t;
	cin >> t;
	vector<long long int> d;
	long long int a = 0;
	for (int i = 0; i < 19; i++) {
		a *= 10;
		a++;
		d.push_back(a);
		//cout << a << endl;
	}
	for (int i = 0; i < t; i++) {
		long long int n;
		cin >> n;
		long long int ans = 0;
		long long int c = 0;
		for (int j = 18; j >= 0; j--) {
			long long int cc = n / d[j];
			if (c + cc < 10) {
				ans += d[j] * cc;
				c += cc;
				n %= d[j];
			}
			else {
				ans += d[j] * (9 - c);
				break;
			}
		}
		printf("Case #%d: ", i + 1);
		cout << ans << endl;
	}
	return 0;
}