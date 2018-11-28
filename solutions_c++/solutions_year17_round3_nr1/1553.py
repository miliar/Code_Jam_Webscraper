# include <bits/stdc++.h>
using namespace std;

typedef int64_t i64;

struct P {
	i64 rh;
	i64 ri;
	i64 idx;
};

int main()
{		
	int T; cin >> T;
	for(int tt=1; tt<=T; ++tt) {
		int n, k; cin >> n >> k;
		
		vector<i64> ri(n), hi(n);
		for(int i=0; i<n; ++i) {
			cin >> ri[i] >> hi[i];
		}
		
		vector<P> best(n);
		for(int i=0; i<n; ++i) {
			best[i] = {2 * ri[i] * hi[i], ri[i], i};
		}
		
		sort(best.begin(), best.end(), [](P a, P b) {
			return (a.rh == b.rh? (a.ri > b.ri):(a.rh > b.rh));
		});
		
		i64 bb = 0;
		for(int i=0; i<n; ++i) {
			i64 cd = ri[i] * ri[i] + 2 * ri[i] * hi[i];
			i64 kk = k - 1;
			//i64 pr = ri[i];
			for(int j=0; j<n && kk; ++j) {
				if (best[j].idx != i) {
					cd += best[j].rh;
					//pr = best[j].ri;
					kk -= 1;
				}
			}
			
			if (!kk) bb = max(bb, cd);
			//cout << "DEBUG: " << cd << endl;
		}
		
		const long double PI = 3.1415926535897932384626;
		printf("Case #%d: %Lf\n", tt, PI * bb);
	}

	return 0;
}