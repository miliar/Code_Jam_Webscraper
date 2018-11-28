#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int can(int per, int pack, int serve){
	if(pack * 100.0 / (serve * per) < 90)
		return -1;
	if(pack * 100.0 / (serve * per) > 110)
		return 1;
	return 0;
}

int main() {
	freopen("B-small-attempt0 (1).in", "r", stdin);
	freopen("Bsmall.txt", "w", stdout);
	int t, tc = 1; cin >> t;
	while(t--){
		int n, p; cin >> n >> p;
		vector<int>a(n);
		for(int i = 0; i < n; i++)
			cin >> a[i];
		vector<deque<int> > packs(n, deque<int>(p));
		for(int i = 0; i < n; i++){
			for(int j = 0; j < p; j++)
				cin >> packs[i][j];
			sort(packs[i].begin(), packs[i].end());
		}

		ll res = 0;
		for(int i = 1; i <= 2 * 1e6; i++){
			while(1){
				bool ok = 1;
				for(int j = 0; j < n && ok; j++){
					while(packs[j].size() && can(a[j], packs[j].front(), i) == -1)
						packs[j].pop_front();
					if(!packs[j].size() || can(a[j], packs[j].front(), i))
						ok = 0;
				}

				if(!ok)
					break;
				res++;
				for(int j = 0; j < n; j++)
					packs[j].pop_front();
			}
		}

		cout << "Case #" << tc++ << ": " << res << endl;
	}
	return 0;
}
