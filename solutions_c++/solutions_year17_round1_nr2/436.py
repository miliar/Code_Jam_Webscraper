#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

main() {
	FILE *fin = freopen("B-large.in", "r", stdin);
	FILE *fout = freopen("B-large.out", "w", stdout);
	assert( fin!=NULL );
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";

		LL n, p;
		cin >> n >> p;
		LL r[n];
		for(LL i = 0; i < n; i++) cin >> r[i];
		LL q[n][p];
		for(LL i = 0; i < n; i++){
			for(LL j = 0; j < p; j++){
				cin >> q[i][j];
			}
			sort(q[i],q[i]+p);
		}
		LL ans = 0;
		LL cur[n];
		LL numpack = 1;
		for(LL i = 0; i < n; i++) cur[i] = 0;
		while(1){
			if(numpack > 1000000) break;
			LL done = 0;
			LL works = 1;
			LL changed = 0;
			for(LL i = 0; i < n; i++){
				while(1){
					if(cur[i] >= p || numpack > 1000000){
						done = 1;
						break;
					}
					if(q[i][cur[i]]*10 < numpack*9*r[i]){
						cur[i]++;
					} else if(q[i][cur[i]]*10 > numpack*11*r[i]){
						works = 0;
						changed = 1;
						numpack ++;
					} else {
						break;
					}
				}
				if(done) break;
			}
			if(done) break;
			if(works){
				for(LL i = 0; i < n; i++){
					//cout << q[i][cur[i]] << " " << numpack*r[i] << endl;
					cur[i]++;
				}
				//cout << endl;
				ans++;
			} else if(!changed){
				numpack++;
			}
		}
		cout << ans << endl;
	}
	exit(0);
}