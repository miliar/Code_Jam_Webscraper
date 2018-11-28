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
		int n, c, m;
		cin >> n >> c >> m;
		int pfreq[1100];
		int bfreq[1100];
		for(int i = 0; i < 1100; i++) pfreq[i] = bfreq[i] = 0;	
		for(int i = 0; i < m; i++){
			int r1, r2;
			cin >> r1 >> r2;
			pfreq[r1]++;
			bfreq[r2]++;
		}
		int ans = 0;
		int csum = 0;
		for(int r = 1; r <= n; r++){
			csum += pfreq[r];
			ans = max(ans, (csum+r-1)/r);
		}
		for(int d = 1; d <= c; d++){
			ans = max(ans, bfreq[d]);
		}
		int ans2 = 0;
		for(int r = n; r >= 1; r--){
			if(pfreq[r] > ans){
				//pfreq[r-1] += pfreq[r]-ans;
				ans2 += pfreq[r]-ans;
			}
		}
		cout << ans << " " << ans2 << endl;
	}
	exit(0);
}