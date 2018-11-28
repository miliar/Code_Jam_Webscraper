#include <bits/stdc++.h>

#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i = int(ini); i < int(lim); i++)
#define ford(i, ini, lim) for(int i = int(ini); i >= int(lim); i--)

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

int main() {
	ios_base::sync_with_stdio(false);

	int casos;
	cin >> casos;
	fori(caso, 1, casos + 1) {
		int n, k;
		cin >> n >> k;
		vector<bool> has(n + 2, false);
		has[0] = has[n + 1] = true;
		fori(i, 1, k + 1) {
			int maxx = -(1 << 30), minn = -(1 << 30);
			int best = -1;
			fori(h, 1, n + 1) {
				if(!has[h]) {
					int min_best = 1 << 30, max_best = -(1 << 30);
					ford(j, h - 1, 0) {
						if(has[j]) {
							min_best = min(min_best, h - j - 1);
							max_best = max(max_best, h - j - 1);
							break;
						}
					}
					/*
					*/
					fori(j, h + 1, n + 2) {
						if(has[j]) {
							min_best = min(min_best, j - h - 1);
							max_best = max(max_best, j - h - 1);
							break;
						}
					}
					if(min_best > minn) {
						minn = min_best;
						maxx = max_best;
						best = h;
					}
					else if(min_best == minn && max_best > maxx) {
						minn = min_best;
						maxx = max_best;
						best = h;
					}
				}
			}
			has[best] = true;
			if(i == k) {
				cout << "Case #" << caso << ": " << maxx << " " << minn << '\n';
			}
		}
	}

	return 0;
}

