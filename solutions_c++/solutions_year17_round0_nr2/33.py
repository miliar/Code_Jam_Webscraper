#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <stack>
#include <queue>

using namespace std;

long long work(long long n) {
	int cnt = 0;
	int a[20];
	while (n) {
		a[cnt] = n % 10;
		n /= 10;
		cnt ++;
	}
	bool smalled = false;
	int flag = -1;
	for (int i = cnt-1; i > 0; i --) {
		if (a[i] > a[i-1]) {
			flag = i;
			break;
		}
	}
	if (flag != -1) {
		a[flag] --;
		for (int i = 0; i < flag; i ++) a[i] = 9;
	}
	long long ans = 0;
	for (int i = cnt-1; i >= 0; i --) {
		ans = ans * 10 + a[i];
	}
	return ans;
}

int main() {
	int t;
	cin >> t;
	for (int tt = 1; tt <= t; tt ++) {
		long long n;
		cin >> n;
		cout << "Case #" << tt << ": ";
		long long ans = work(n);
		while (ans != work(ans)) ans = work(ans);
		cout << ans << endl;
	}

	return 0;
}

