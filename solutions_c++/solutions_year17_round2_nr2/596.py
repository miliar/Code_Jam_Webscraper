#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <unordered_map>
#include <unordered_set>

#define pb push_back
#define mp make_pair

using big = long long;

using namespace std;

int N, R, O, Y, G, B, V;

bool ck() {
//	if (R * 2 == N) {
//		return B && Y;
//	}
//	if (B * 2 == N) {
//		return R && Y;
//	}
//	if (Y * 2 == N) {
//		return B && R;
//	}
	return R <= N / 2 && B <= N / 2 && Y <= N / 2;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cas;
	scanf("%d", &cas);

	for (int cass = 1; cass <= cas; ++cass) {
		printf("Case #%d: ", cass);
		cerr << "case " << cass << endl;
		cin >> N >> R >> O >> Y >> G >> B >> V;
		if (!ck()) {
			puts("IMPOSSIBLE");
			continue;
		}
		string ans;
		vector<pair<int, char>> a;
		a.push_back({R, 'R'});
		a.push_back({B, 'B'});
		a.push_back({Y, 'Y'});
		sort(a.begin(), a.end(), greater<pair<int, char>>());
		while (ans.size() < N) {
			int ii = -1, jj = -1;
			for (int i = 0; i < 3 && ii == -1; ++i) {
				for (int j = i + 1; j < 3 && jj == -1; ++j) {
					if (a[i].first && a[j].first) {
						ii = i;
						jj = j;
					}
				}
			}
			if (ii != -1 && jj != -1) {
				--a[ii].first;
				--a[jj].first;
				ans += a[ii].second;
				ans += a[jj].second;
				sort(a.begin(), a.end(), greater<pair<int, char>>());
				continue;
			}
			for (auto &p : a) {
				if (p.first) {
					--p.first;
					ans += p.second;
				}
			}
			sort(a.begin(), a.end(), greater<pair<int, char>>());
		}
		if (ans.front() == ans.back()) {
			swap(ans[ans.size() - 1], ans[ans.size() - 2]);
		}
		cout << ans << endl;
	}
	fclose(stdin);
	fclose(stdout);
}

