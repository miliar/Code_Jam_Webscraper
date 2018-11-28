#include<iostream>
#include<string>
#define ll unsigned long long
using namespace std;

int main() {
	int t; cin >> t;
	char n[19]; int len, pos;
	for (int T = 1; T <= t;T++) {
		cin >> n; len = strlen(n);
		pos = 0;int i;
		bool f = true;
		for (i = 1; i < len; i++) {
			if (n[pos] > n[i]) {
				f = false;
				break;
			}
			else if (n[pos] < n[i]) {
				pos = i;
			}
		}
		if (f);
		else {
			n[pos] = n[pos] - 1;
			while (++pos < len)n[pos] = '9';
			if (n[0] == '0')
				for (i = 0; i < len; i++) {
					n[i] = n[i + 1];
				}
		}
		cout << "Case #" << T << ": " << stoull(n) << '\n';
	}
	return 0;
}