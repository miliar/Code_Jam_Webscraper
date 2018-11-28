#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <cstdio>
using namespace std;

bool isTidy(long long n) {
	string s = to_string(n);
	long long len = s.length();

	if (len == 1) {
		return true;
	}
	for (int i = 0; i < len - 1; i++) {
		if (s[i] > s[i+1]) {
			return false;
		}
	}
	return true;
}


int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out","w", stdout);
	long long times,n,ans,num = 0;
	long long iter = 1;
	cin >> times;
	for (int ti = 1; ti <= times; ti++) {
		cin >> n;
		ans = n;
		if (isTidy(n)) {
			ans = n;
		}
		else {
			num = 1;
			iter = 1;
			while (!isTidy(ans)) {
				num = num * 10;
				ans = ans - (ans % num) - 1;
				iter++;
			}
		}
		cout << "Case #" << ti << ": " << ans << endl;
	}

	return 0;
}