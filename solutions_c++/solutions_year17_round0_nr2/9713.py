#include<bits/stdc++.h>
using namespace std;
vector<unsigned long long> ar;

int f(unsigned long long n) {
	unsigned long long m = n, a = 0, mult = 1;
	while (n != 0) {
		ar.push_back(n % 10);
		n /= 10;
	}
	sort(ar.begin(), ar.end());
	int i;
	for (i = 0; i < ar.size(); i++) {
		a *= 10;
		a += ar[i];
	}
	if (a == m)
		return 1;
	return 0;
}

int main() {
//	freopen("input.txt", "r", stdin);
//	freopen("output.txt", "w", stdout);
	unsigned long long n, t, cases = 1;
	cin >> t;
	while (cases <= t) {
		cout << "Case #" << cases++ << ": ";
		cin >> n;
		while (1) {
			ar.clear();
			if (f(n)) {
				cout << n << endl;
				break;
			}
			n--;
		}
	}
	return 0;
}
