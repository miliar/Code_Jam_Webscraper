#include <bits/stdc++.h>

using namespace std;

const int MAXN = (int)2e5 + 256;

typedef long long ll;

ll d[2][20][12];
int a[20], sz;
ll res, num;

ll f(char sp, int pos, int last) {
	if (pos == sz) {
		res = max(res, num);
		// cerr << num << endl;
		return 1;
	}
	ll &res = d[sp][pos][last];
	// if (~res) return res;
	res = 0;
	for (int i = last; i <= 9; ++i) {
		if (sp) {
			if (i > a[pos])
				break;
			num = num * 10 + i;
			res += f(i == a[pos], pos + 1, i);
			num /= 10;
		} else {
			num = num * 10 + i;
			res += f(0, pos + 1, i);
			num /= 10;
		}
	}
	return res;
}

inline ll gen(int len) {
	ll res = 0;
	while (len--) {
		res = res * 10 + rand() % 9 + 1;
	}
	return res;
}

int main() {
	int t, Case = 0; scanf("%d", &t);
	while (t--) {
		long long n; scanf("%lld", &n);
		// long long n = gen(18);
		memset(d, 255, sizeof d);
		sz = 0;
		num = 0;
		while (n) {
			a[sz++] = n % 10;
			n /= 10;
		}
		reverse(a, a + sz);
		res = 1;
		f(1, 0, 0);

		printf("Case #%d: %lld\n", ++Case, res);
	}
	return 0;
}

