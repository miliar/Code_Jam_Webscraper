#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

void proc(int caseidx) {
	long long n;
	scanf("%lld", &n);
	++n;
	string s = to_string(n);

	long long ans = 1;
	string tmp;
	for (int i = 0; i < s.length(); ++i) {
		if (tmp.empty() || tmp.back() < s[i]) {
			string tmp2 = tmp;
			tmp2.push_back(s[i] - 1);
			for (int j = i + 1; j < s.length(); ++j) tmp2.push_back('9');
			ans = max(ans, stoll(tmp2));
		}
		if (tmp.empty() || tmp.back() <= s[i]) {
			tmp.push_back(s[i]);
		}
		else {
			break;
		}
	}
	printf("Case #%d: %lld\n", caseidx, ans);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		proc(i);
	}
	return 0;
}