#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

#define INF 999999999
#define pb push_back
#define fs first
#define sc second
#define mp make_pair
#define EPS .000000001

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int UI;
typedef vector < int > VI;
typedef vector < unsigned int > VUI;
typedef vector < string > VS;
typedef vector < pair < int, int > > VII;

VI R;
VII Q[100];
VI Q2[100];
VI que;
VI beginShow;

int main(){
    //freopen(".in", "rt", stdin);
    //freopen(".out", "wt", stdout);

	int T, N, P, t, ans;
	cin >> T;

	for (int step = 0; step < T; ++step) {

		cin >> N >> P;

		ans = 0;
		R.assign(N, 0);
		que.assign(0, 0);
		beginShow.assign(N, 0);
		for (int i = 0; i < N; ++i)
			cin >> R[i];

		for (int i = 0; i < N; ++i) {
			Q[i].assign(0, {0, 0});
			Q2[i].assign(0, 0);

			for (int j = 0; j < P; ++j) {
				cin >> t;
				
				double mn = t / (1.1 * double(R[i]));
				mn = int(mn) + (fabs(int(mn) - mn) < EPS ? 0 : 1);

				double mx = t / (0.9 * double(R[i]));
				mx = int(mx);

				if (int(mn) <= int(mx)) {
					Q[i].pb({ int(mn), int(mx) });
					Q2[i].pb(1);
					que.pb(int(mn));
					que.pb(int(mx));
				}

				//cout << "(" << t / (1.1 * R[i]) << " " << mn << ", " << t / (0.9 * R[i]) << " " << mx << ") ";
				//cout << "(" << mn << ", " << mx << ") ";
			}

			sort(Q[i].begin(), Q[i].end());

			// for (int j = 0; j < Q[i].size(); ++j)
			// 	cout << "(" << Q[i][j].fs << ", " << Q[i][j].sc << ") ";

			// cout << endl;
		}
		sort(que.begin(), que.end());

		int l = que.size();
		for (int cur = 0; cur < l; ++cur) {

			int curval = que[cur];
			int countfind = 0;

			for (int i = 0; i < N; ++i)
				for (int j = 0; j < P; ++j)
					if (Q[i][j].fs <= curval && Q[i][j].sc >= curval && Q2[i][j]) {
						//beginShow[i] = j + 1;
						++countfind;
						break;
					}

			if (countfind == N) {
				++ans;
				for (int i = 0; i < N; ++i)
					for (int j = 0; j < P; ++j)
						if (Q[i][j].fs <= curval && Q[i][j].sc >= curval && Q2[i][j]) {
							Q2[i][j] = 0;
							break;
						}
			}

		}

		cout << "Case #" << step + 1 << ": " << ans << endl;
		//cout << endl;


		//cout << endl;

	}

    return 0;
}
