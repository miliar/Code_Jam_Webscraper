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

char graph[30][30];
int N, M;

vector<int> ve[30];
vector<int> aa;

int main(void) {
	int TEST;
	scanf("%d", &TEST);
	for (int CASE = 1; CASE <= TEST; CASE++) {
		scanf("%d %d\n", &N, &M);
		aa.clear();
		for (int i = 1; i <= N; i++) {
			ve[i].clear();
			for (int j = 1; j <= M; j++) {
				graph[i][j] = getchar();
				if (graph[i][j] != '?') {
					ve[i].push_back(j);
				}
			}
			getchar();
		}

		for (int i = 1; i <= N; i++) {
			int ind = 0;
			if (ve[i].size() != 0) {
				aa.push_back(i);
				for (int j = 1; j <= M; j++) {
					if (ind != ve[i].size() && ve[i][ind] < j) {
						ind++;
					}
					if (ind == ve[i].size()) {
						graph[i][j] = graph[i][ve[i][ind - 1]];
					}
					else {
						graph[i][j] = graph[i][ve[i][ind]];
					}
				}
			}
		}

		int ind = 0;
		for (int i = 1; i <= N; i++) {
			while (ind != aa.size() && aa[ind] < i) {
				ind++;
			}
			if (ve[i].size() == 0) {
				if (ind == aa.size()) {
					for (int j = 1; j <= M; j++) {
						graph[i][j] = graph[aa[ind - 1]][j];
					}
				}
				else {
					for (int j = 1; j <= M; j++) {
						graph[i][j] = graph[aa[ind]][j];
					}
				}
			}
		}

		printf("Case #%d: \n", CASE);
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= M; j++) {
				printf("%c", graph[i][j]);
			}
			printf("\n");
		}
	}

	return 0;
}