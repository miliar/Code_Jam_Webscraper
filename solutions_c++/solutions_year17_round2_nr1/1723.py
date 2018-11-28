# include <bits/stdc++.h>
using namespace std;

struct SP {
	int k, s;
};

int main()
{		
	int T; cin >> T;
	for(int tt=1; tt<=T; ++tt) {
		int d, n; cin >> d >> n;

		vector<SP> hi(n);
		for(int i=0; i<n; ++i) {
			cin >> hi[i].k >> hi[i].s;
		}

		sort(hi.begin(), hi.end(), [](SP a, SP b) {
			return (a.k > b.k);
		});

		vector<long double> ti(n);
		for(int i=0; i<n; ++i) {
			long double te = (d - hi[i].k) * 1.0 / hi[i].s;
			ti[i] = max(te, i? ti[i-1]:0);
		}

		printf("Case #%d: %Lf\n", tt, d*1.0/ti.back());
	}

	return 0;
}