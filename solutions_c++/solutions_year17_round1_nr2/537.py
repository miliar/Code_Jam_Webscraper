#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<list>
#include<vector>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#include<functional>
#include<cmath>
#include<string>

#define sd(a) scanf("%d", &a);
#define sld(a) scanf("%lld", &a);

using namespace std;

typedef long long int lli;
typedef pair<int, int> ii;

int xx[4] = { 0, 0, -1, 1 };
int yy[4] = { -1, 1, 0, 0 };
int N, P;
vector<int> je;
vector<int> dat[51];
vector<ii> ans[51];
int inde[51];
int ans_cou;

int main(void) {
	int TEST;
	scanf("%d", &TEST);
	for (int CASE = 1; CASE <= TEST; CASE++) {
		je.clear();
		ans_cou = 0;
		scanf("%d %d", &N, &P);
		for (int i = 1; i <= N; i++) {
			int temp;
			scanf("%d", &temp);
			je.push_back(temp);
		}
		for (int i = 1; i <= N; i++) {
			dat[i].clear();
			ans[i].clear();
			for (int j = 1; j <= P; j++) {
				int temp;
				scanf("%d", &temp);
				dat[i].push_back(temp);
			}
		}

		for (int i = 1; i <= N; i++) {
			for (int j = 0; j < P; j++) {
				double temp = (double)dat[i][j] / (double)je[i - 1];
				double st = temp * 10 / 11;
				double fi = temp * 10 / 9;

				int rr = st;
				if (rr < st) {
					rr++;
				}
				int gg = fi;
				if (gg > fi) {
					gg--;
				}

				if (rr > gg) {
					ans[i].push_back(ii(-1, -1));
				}
				else {
					ans[i].push_back(ii(rr, gg));
				}
			}
		}
		
		for (int i = 1; i <= N; i++) {
			sort(ans[i].begin(), ans[i].end());
		}
		int cur = 0;
		for (int i = 1; i <= N; i++) {
			cur = max(cur, ans[i][0].first);
			inde[i] = 0;
		}
		while (1) {
			bool check = true;
			bool conti = false;

			for (int i = 1; i <= N; i++) {
				while (inde[i] < ans[i].size() && ans[i][inde[i]].second < cur) {
					inde[i]++;
				}
				
				if (inde[i] == ans[i].size()) {
					check = false;
					break;
				}
				if (ans[i][inde[i]].first > cur) {
					cur = ans[i][inde[i]].first;
					conti = true;
				}
			}

			if (!check) {
				break;
			}

			if (conti) {
				continue;
			}

			for (int i = 1; i <= N; i++) {
				inde[i]++;
			}
			ans_cou++;
		}

		printf("Case #%d: %d\n", CASE, ans_cou);
	}

	return 0;
}