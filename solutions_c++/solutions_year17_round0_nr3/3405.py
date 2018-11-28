#include <bits/stdc++.h>
using namespace std;

#define pb         push_back

typedef long long ll;
const ll INF = 1000000000000000000ll;
const ll MOD = 1000000007ll;
const double EPS = 1e-8;

int main(void) {
	//ios_base::sync_with_stdio(false);
	//cin.tie(0);
	
	int t;
	cin >> t;

	for(int cs=1; cs<=t; cs++){
		int st[1000005];
		int n, k;
		cin >> n >> k;

		for(int i=0; i<=n+1; i++){
			st[i] = 0;
		}
		st[0] = 1;
		st[n+1] = 1;

		auto comp = [](pair<int, pair<int, int>> l, pair<int, pair<int, int>> r){if(l.first == r.first) return l.second.first > r.second.first; else return l.first < r.first;};
		priority_queue< pair<int, pair<int, int> > , vector< pair<int, pair<int, int> > >, decltype(comp)> que(comp);
		que.push(make_pair(n, make_pair(0, n+1)));
		for(int i=0; i<k; i++){
			auto x = que.top(); que.pop();
			//cout << x.first << endl;

			int l = x.second.first;
			int r = x.second.second;
			int mid = (l + r) / 2;
			st[mid] = 1;

			if(mid - l - 1 > 0){
				que.push(make_pair(mid - l - 1, make_pair(l, mid)));
			}
			if(r - mid - 1 > 0){
				que.push(make_pair(r - mid - 1, make_pair(mid, r)));
			}

			if(i == k-1){
				int j = mid-1;
				while(j >= 0 && st[j] == 0) j--;
				int ls = (mid-1) - j;

				j = mid+1;
				while(j <= n+1 && st[j] == 0) j++;
				int rs = j - (mid + 1);

				printf("Case #%d: %d %d\n", cs, max(ls, rs), min(ls, rs));
			}

		}

		/*
		for(int j=0; j<=n+1; j++){
			printf("%d ", st[j]);
		}
		puts("");
		*/

	}
	
	return 0;
}
