#include <bits/stdc++.h>
using namespace std;

int T, N, P, Gi, c[4], ans;

int main() {
	cin >> T;
	for (int t=1; t<=T; t++) {
		cin >> N >> P;
		c[0]=c[1]=c[2]=c[3]=0;
		for (int i = 0; i < N; i++) {
			cin >> Gi;
			c[Gi%P]++;
		}
		ans = c[0];

		if (P == 2)
			ans += (c[1]+1)/2;
		else if (P == 3) {
			if (c[2] >= c[1]) {
				ans += c[1];
				c[2] -= c[1];
				c[1] = 0;
				ans += (c[2]+2) / 3;
			}
			else /*if (c[1] > c[2])*/ {
				ans += c[2];
				c[1] -= c[2];
				c[2] = 0;
				ans += (c[1]+2) / 3;
			}
		}

		cout << "Case #" << t << ": " << ans << endl;
	}
}
