#include <bits/stdc++.h>
using namespace std;
#define ll long long

int dx[] = {-1,1,0,0};
int dy[] = {0,0,1,-1};

int N,M;
bool valid(int r,int c) {
	return (r >= 0 && r < N && c >= 0 && c < M);
}

int main() {
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	int T;cin >> T;
	for(int t=1;t<=T;++t) {
		char a[26][26];
		map<char,int> mxR,mnR,mxC,mnC;
		cin >> N >> M;
		char c;
		deque<pair<int,int> > dq;
		for(int i=0;i<N;++i)
			for(int j=0;j<M;++j) {
				cin >> c;
				a[i][j] = c;
				if (c != '?') {
					if (mxR.find(c) == mxR.end())
						mxR[c] = i;
					mxR[c] = max(mxR[c], i);

					if (mxC.find(c) == mxC.end())
						mxC[c] = j;
					mxC[c] = max(mxC[c], j);

					if (mnR.find(c) == mnR.end())
						mnR[c] = i;
					mnR[c] = min(mnR[c], i);

					if (mnC.find(c) == mnC.end())
						mnC[c] = j;
					mnC[c] = min(mnC[c], j);
				}
				else dq.push_back({i,j});
			}

		while(!dq.empty()) {
			int i = dq.front().first,j = dq.front().second;
			dq.pop_front();
			bool don = 0;
			if (a[i][j] == '?') {
				for (int k = 0; k < 4; ++k) {
					int x = i + dx[k], y = j + dy[k];
					if (valid(x, y) && a[x][y] != '?') {
						if (x == i) {
							bool ok = 1;
							for(int e = mnR[a[x][y]];e <= mxR[a[x][y]]; ++e)
								if(a[e][j] != '?' && a[e][j] != a[x][y]) {
									ok = 0;
									break;
								}
							if (ok) {
								mxC[a[x][y]] = max(mxC[a[x][y]], j);
								mnC[a[x][y]] = min(mnC[a[x][y]], j);
								a[i][j] = a[x][y];
								don = 1;
								break;
							}
						} else {
							bool ok = 1;
							for (int e = mnC[a[x][y]]; e <= mxC[a[x][y]]; ++e)
								if (a[i][e] != '?' && a[i][e] != a[x][y]) {
									ok = 0;
									break;
								}
							if (ok) {
								mxR[a[x][y]] = max(mxR[a[x][y]], i);
								mnR[a[x][y]] = min(mnR[a[x][y]], i);
								a[i][j] = a[x][y];
								don = 1;
								break;
							}
						}
					}
				}
			}
			if(!don) dq.push_back({i,j});
		}



		cout << "Case #"<<t<<":\n";
		for(int i=0;i<N;++i) {
			for(int j=0;j<M;++j) cout << a[i][j];
			cout << "\n";
		}

	}
}
