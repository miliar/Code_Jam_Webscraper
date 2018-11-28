#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

vector<int> v;

int main() {
	int t, ca = 1;
	scanf("%d", &t);
	while (t--) {
		printf("Case #%d: ", ca++);
		long long n;
		scanf("%lld", &n);
		v.clear();
		while (n) {
			v.push_back(n % 10);
			n /= 10;
		}
		for (int i = 0; i < v.size() / 2; i++) {
			swap(v[i], v[v.size() - i - 1]);
		}
		int pos = 0, ok = 1;
		for (ok = 1; ok < v.size(); ok++) {
			if (v[ok] > v[ok - 1]) {
				pos = ok;
			} else if (v[ok] < v[ok - 1]) {
				break;
			}
		}
		if (ok != v.size()) {
			v[pos]--;
			for (int i = pos + 1; i < v.size(); i++) {
				v[i] = 9;
			}
		}
		for (int i = 0; i < v.size(); i++) {
			n = n * 10 + v[i];
		}
		printf("%lld\n", n);
	}
}
