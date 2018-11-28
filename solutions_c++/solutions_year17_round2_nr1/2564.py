#include <bits/stdc++.h>
using namespace std;
#define eb emplace_back
#define emp emplace
#define fi first
#define se second
#define INF 0x3f3f3f3f
typedef long long ll;
typedef pair<int,int> ii;

int main(void) {
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;

	int cnt = 1;
	while (t--) {
		double d;
		int n;
		cin >> d >> n;

		double t = -1;
		for (int i = 0; i < n; i++) {
			double s, v;
			cin >> s >> v;

			t = max(t, (d-s)/v);
		}

		cout.precision(8);
		cout << "Case #" << cnt++ << ": " <<fixed<< d/t << endl;

	}

	return 0;
}
