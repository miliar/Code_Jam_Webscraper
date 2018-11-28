#include <bits/stdc++.h>
using namespace std;

int main() {

	freopen("readin.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	while (t--) {

		double d;
		int n;
		cin >> d >> n;
		double mt = 0, di, sp;
		for (int i = 0; i < n; i++) {
			cin >> di >> sp;
			mt = max(mt, (d - di) / sp);
		}
		static int tc = 1;
		printf("Case #%d: ", tc++);
		cout << fixed << setprecision(6) << d / mt << endl;
	}

	return 0;
}
