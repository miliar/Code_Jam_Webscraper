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

char base_graph[110][110];
char graph[110][110];
int make_graph[110][110];
int make_graph2[110][110];
int check_graph[210][210];
int check_graph2[410][410];
int N, M;
int cou, ans;
bool check[410];

void check_init() {
	for (int i = 0; i < 410; i++) {
		check[i] = false;
	}
}
void init() {
	cou = 0;
	ans = 0;
	check_init();
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			graph[i][j] = '.';
			base_graph[i][j] = '.';
			make_graph[i][j] = 0;
			make_graph2[i][j] = 0;
		}
	}


	for (int i = 0; i <= 205; i++) {
		for (int j = 0; j <= 205; j++) {
			check_graph[i][j] = 0;
		}
	}
	for (int i = 1; i <= N; i++) {
		check_graph[0][i] = 1;
	}
	for (int i = 1; i <= N; i++) {
		for (int j = 101; j <= N + 100; j++) {
			check_graph[i][j] = 1;
		}
	}
	for (int j = 101; j <= N + 100; j++) {
		check_graph[j][205] = 1;
	}


	for (int i = 0; i <= 405; i++) {
		for (int j = 0; j <= 405; j++) {
			check_graph2[i][j] = 0;
		}
	}
	for (int i = 1; i <= N * 2 - 1; i++) {
		check_graph2[0][i] = 1;
	}
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			check_graph2[i + j  - 1][j - i + N + 200] = 1;
		}
	}
	for (int i = 201; i <= N * 2 - 1 + 200; i++) {
		check_graph2[i][405] = 1;
	}
}
void put_plus(int x, int y) {
	check_graph2[0][x + y - 1] = 0;
	check_graph2[y - x + N + 200][405] = 0;
	make_graph2[x][y] = 1;
}
void put_x(int x, int y) {
	check_graph[0][x] = 0;
	check_graph[y + 100][205] = 0;
	make_graph[x][y] = 1;
}
void count_change() {
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (base_graph[i][j] != graph[i][j]) {
				cou++;
			}
			switch (graph[i][j]) {
			case '+':
				ans++;
				break;
			case 'x':
				ans++;
				break;
			case 'o':
				ans += 2;
				break;
			}
		}
	}
}
void print(int CASE) {
	printf("Case #%d: %d %d\n", CASE, ans, cou);
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (base_graph[i][j] != graph[i][j]) {
				printf("%c %d %d\n", graph[i][j], i, j);
			}
		}
	}
}
bool dfs(int ind) {
	if (ind == 205) {
		return true;
	}
	if (check[ind]) {
		return false;
	}
	check[ind] = true;
	for (int i = 1; i <= 205; i++) {
		if (check_graph[ind][i] == 1) {
			if (dfs(i)) {
				check_graph[ind][i] = 0;
				check_graph[i][ind] = 1;
				if (1 <= ind && ind <= N && 101 <= i && i <= N + 100) {
					make_graph[ind][i - 100] = 1;
				}
				if (1 <= i && i <= N && 101 <= ind && ind <= N + 100) {
					make_graph[i][ind - 100] = 0;
				}
				return true;
			}
		}
	}

	return false;
}
bool dfs2(int ind) {
	if (ind == 405) {
		return true;
	}
	if (check[ind]) {
		return false;
	}
	check[ind] = true;
	for (int i = 1; i <= 405; i++) {
		if (check_graph2[ind][i] == 1) {
			if (dfs2(i)) {
				check_graph2[ind][i] = 0;
				check_graph2[i][ind] = 1;
				if (1 <= ind && ind <= N * 2 - 1 && 201 <= i && i <= N * 2 - 1 + 200) {
					int y = (ind + i - 200 + 1 - N) / 2;
					int x = ind - y + 1;
					make_graph2[x][y] = 1;
				}
				if (1 <= i && i <= N * 2 - 1 && 201 <= ind && ind <= N * 2 - 1 + 200) {
					int y = (ind + i - 200 + 1 - N) / 2;
					int x = i - y + 1;
					make_graph2[x][y] = 0;
				}
				return true;
			}
		}
	}

	return false;
}
void make_ans() {
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++) {
			if (make_graph[i][j] == 1 && make_graph2[i][j] == 1) {
				graph[i][j] = 'o';
			}
			else if (make_graph[i][j] == 1) {
				graph[i][j] = 'x';
			}
			else if (make_graph2[i][j] == 1) {
				graph[i][j] = '+';
			}
			else {
				graph[i][j] = '.';
			}
		}
	}
}

int main(void) {
	int TEST;
	scanf("%d", &TEST);
	for (int CASE = 1; CASE <= TEST; CASE++) {
		scanf("%d %d\n", &N, &M);
		init();
		for (int i = 1; i <= M; i++) {
			char temp;
			int t1, t2;
			scanf("%c %d %d\n", &temp, &t1, &t2);
			base_graph[t1][t2] = temp;
			graph[t1][t2] = temp;
			if (temp == 'x') {
				put_x(t1, t2);
			}
			else if (temp == '+') {
				put_plus(t1, t2);
			}
			else if (temp == 'o') {
				put_plus(t1, t2);
				put_x(t1, t2);
			}
		}

		while (dfs(0)) {
			check_init();
		}
		check_init();
		while (dfs2(0)) {
			check_init();
		}

		make_ans();
		count_change();
		print(CASE);
	}

	return 0;
}