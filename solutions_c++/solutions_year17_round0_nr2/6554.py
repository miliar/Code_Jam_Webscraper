#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

#define IOS ios_base::sync_with_stdio(0);cin.tie(0);
#define MP make_pair
#define PB push_back
#define FF first
#define SS second

bool chk(LL n) {
	LL pre = 9;
	while (n > 0) {
		if (n % 10 > pre) return 0;
		pre = n % 10;
		n /= 10;
	}
	return 1;
}

int main() {
	IOS;
	LL n, kase = 0;
	cin >> n;
	while (n--) {
		LL tmp;
		cin >> tmp;
		for (LL i = tmp; i >= 0; i--) {
			if (chk(i)) {
				cout << "Case #" << ++kase << ": " << i << "\n";
				break;
			}
		}
	}
}
