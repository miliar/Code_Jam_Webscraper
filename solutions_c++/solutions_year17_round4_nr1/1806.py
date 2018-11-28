#include <bits/stdc++.h>
using namespace std;

int tc;
int N, P, memo[4][101][51][26][14], num[4];

int Solve(int r, vector<pair<int, int> > &v) {
	int id[4], s = 0;
	for (int i=0; i<4; ++i) {
		id[i] = v[i].first;
		s += v[i].first;
	}

	if (s == 0) return 0;

	int &ret = memo[r][id[0]][id[1]][id[2]][id[3]];
	if (ret != -1) return ret;

	ret = r == 0 ? 1 : 0;

	for (int i=0; i<4; ++i) {
		if (v[i].first > 0) {
			v[i].first--;
			ret = max(ret, (r == 0) + Solve((r+v[i].second)%P, v));
			v[i].first++;
		}
	}

	return ret;
}


int main() {
	scanf("%d", &tc);
	for (int tt=1; tt<=tc; ++tt) {
		scanf("%d%d", &N, &P);
		
		memset(memo, -1, sizeof(memo));
		memset(num, 0, sizeof(num));
		for (int i=0; i<N; ++i) {
			int t;
			scanf("%d", &t);
			num[t%P]++;
		}

		vector<pair<int, int> > v;
		for (int i=0; i<4; ++i) 
			v.push_back(make_pair(num[i], i));
		sort(v.begin(), v.end(), greater<pair<int, int> >());

		printf("Case #%d: ", tt);
		printf("%d\n", Solve(0, v));
	}

	return 0;
}
