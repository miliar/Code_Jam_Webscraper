#include<cstdio>
#include<algorithm>
using namespace std;

char board[33][33];
char tmp[33][33];
bool visited[26];

void process(int R, int C){
	for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) if (board[i][j] != '?' && !visited[board[i][j]-'A']){
		char c = board[i][j];
		visited[c - 'A'] = true;
		int jl = j, jr = j;
		while (jl > 0 && board[i][jl - 1] == '?') jl--;
		while (jr < C - 1 && board[i][jr + 1] == '?') jr++;
		int il = i, ir = i;
		while (il > 0){
			bool ok = true;
			for (int jj = jl; jj <= jr; jj++) if (board[il - 1][jj] != '?'){
				ok = false;
			}
			if (ok) il--;
			else break;
		}
		while (ir < R - 1){
			bool ok = true;
			for (int jj = jl; jj <= jr; jj++) if (board[ir + 1][jj] != '?'){
				ok = false;
			}
			if (ok) ir++;
			else break;
		}
		for (int ii = il; ii <= ir; ii++)for (int jj = jl; jj <= jr; jj++) board[ii][jj] = c;
	}
	for (int i = 0; i < 26; i++) visited[i] = false;
}

void chk(int R, int C){
	for (int it = 0; it < 26; it++){
		char c = 'A' + it;
		int xl = R, xr = -1, yl = C, yr = -1;
		for (int i = 0; i < R; i++) for (int j = 0; j < C; j++) if (board[i][j] == c){
			xl = min(xl, i);
			xr = max(xr, i);
			yl = min(yl, j);
			yr = max(yr, j);
		}
		if (xr >= 0){
			bool ok = true;
			for (int i = xl; i <= xr; i++)for (int j = yl; j <= yr; j++) if (board[i][j] != c){
				printf("Case #%d failed.\n");
				return;
			}
		}
	}
	for (int i = 0; i < R; i++)for (int j = 0; j < C; j++) if (board[i][j] == '?'){
		printf("Case #%d failed.\n");
		return;
	}
}

int main(){
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);

	int T; scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++){
		printf("Case #%d:\n", tc);
		int R, C; scanf("%d%d", &R, &C);
		for (int i = 0; i < R; i++) scanf("%s", board[i]);

		process(R, C);
		for (int i = 0; i < R; i++) printf("%s\n", board[i]);
	}
}