#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

set<LL> f;
map<LL,LL> cnt;


main() {
	FILE *fin = freopen("C-large.in", "r", stdin);
	FILE *fout = freopen("C-large.out", "w", stdout);
	assert( fin!=NULL );
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		LL n, k;
		cin >> n >> k;
		f.clear();
		cnt.clear();
		cnt[n]++;
		f.insert(-n);
		LL done = 0;
		while(1){
			LL len = -*f.begin();
			f.erase(f.begin());
			LL l = (len - 1)/2;
			LL r = len - 1 - l;
			f.insert(-l);
			f.insert(-r);
			done += cnt[len];
			cnt[l] += cnt[len];
			cnt[r] += cnt[len];
			if(done >= k){
				cout << max(l,r) << " " << min(l,r) << endl;
				break;
			}
		}
	}
	exit(0);
}