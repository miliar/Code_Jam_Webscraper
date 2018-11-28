#include <bits/stdc++.h>

using namespace std;

typedef long long lint;

int main(){
	// freopen("test.txt","r",stdin);
	// freopen("answer.txt","w",stdout);
	cin.sync_with_stdio(0); cin.tie(0);
	int T; cin >> T;
	for (int tc = 1; tc <= T; ++tc){
		lint n, k; cin >> n >> k;

		map<lint, lint> cnt;
		set<lint> S;
		cnt[n] = 1;
		S.insert(n);
		lint fnd;
		while (true){
			lint cur = *(--S.end()); S.erase(--S.end());
			// cout << cur << endl;
			if (cnt[cur] >= k){
				fnd = cur;
				break;
			}
			k -= cnt[cur];
			if (cur%2 == 0){
				cnt[cur/2] += cnt[cur];
				cnt[cur/2 - 1] += cnt[cur];
				S.insert(cur/2);
				S.insert(cur/2 - 1);
			}
			else{
				cnt[cur/2] += 2*cnt[cur];
				S.insert(cur/2);
			}
		}
		lint ml = 0, mr = 0;
		if (fnd%2 == 0){
			ml = fnd/2 - 1;
			mr = fnd/2;
		}
		else{
			ml = mr = fnd/2;
		}
		printf("Case #%d: ", tc);
		printf("%lld %lld", mr, ml);
		printf("\n");
	}
	return 0;
}