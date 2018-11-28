#include <bits/stdc++.h>

using namespace std;
const int N = 1001;
int brute(int n) {
	int ret = -1;
	for (int i = 1; i <= n; ++i) {
		string tmp = to_string(i);
		bool tide = true;
		for (int j = 1; j < tmp.size(); ++j) {
			if (tmp[j - 1] > tmp[j])
				tide = false;
		}
		if (tide)
			ret = i;
	}
	return ret;
}
long long greedy(long long n) {
	string s = to_string(n);
	for (int i = 1; i < s.size(); ++i) {
		if (s[i - 1] > s[i]) {
			int index = i - 1;
			char digit = s[i - 1];
			while (index >= 0 && s[index] == digit) {
				s[index] = (char) (digit - 1);
				--index;
			}
			index += 2;
			while (index < s.size())
				s[index++] = '9';
			return stoll(s);
		}
	}
	return n;
}
int main() {
#ifndef ONLINE_JUDGE
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
#endif
	int t;
	scanf("%d\n", &t);
	for (int test = 1; test <= t; ++test) {
		long long n;
		scanf("%lld\n", &n);
		printf("Case #%d: %lld\n", test, greedy(n));
	}
	return 0;
}

