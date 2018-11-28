#include <bits/stdc++.h>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)
#define Cor(i,l,r) for (int i = l; i >= r; --i)

const int pi[] = {1,0,-1,0};
const int pj[] = {0,1,0,-1};

char A[55][55];
int n, m;
bool isShooter(int x, int y) {
	return A[x][y] == '|' || A[x][y] == '-';
}

bool isWall(int x, int y) {
	return A[x][y] == '#';
}

bool isOut(int x, int y) {
	return x < 1 || x > n || y < 1 || y > m;
}

bool isBlank(int x, int y) {
	return A[x][y] == '.';
}

bool isPie(int x, int y) {
	return A[x][y] == '/';
}

bool isNa(int x, int y) {
	return A[x][y] == '\\';
}

bool forbid[2555][2];
vector< pair<int,int> > vec[55][55];
int go(int x, int y, int d, int who, int flag) {
	if (isWall(x, y) || isOut(x, y)) {
		return 0;
	}
	if (isShooter(x, y)) {
		forbid[who][flag] = true;
		return 0;
	}
	if (isBlank(x, y)) {
		vec[x][y].emplace_back(who, flag);
		go(x + pi[d], y + pj[d], d, who, flag);
	}
	if (isPie(x, y)) {
		(d += 3) &= 3;
		go(x + pi[d], y + pj[d], d, who, flag);
	}
	if (isNa(x, y)) {
		(d += 1) &= 3;
		go(x + pi[d], y + pj[d], d, who, flag);
	}
	return 0;
}

bool Map[5555][5555], nMap[5555][5555];
bool add(int x, int y) {
	Map[x][y] = true;
}

int c, label[5555], bel[5555], q[5555], in[5555], ans[5555];
int main() {
	int T; cin >> T;
	For(TK,1,T) {
		cin >> n >> m;
		For(i,1,n) For(j,1,m) vec[i][j].clear();
		For(i,1,n) scanf("%s", A[i] + 1);
		c = 0;
		memset(forbid, 0, sizeof forbid);
		For(i,1,n) For(j,1,m) if (A[i][j] == '|' || A[i][j] == '-') {
			int x = i, y = j;
			++c; 
			go(x + pi[0], y + pj[0], 0, c, A[i][j] == '-');
			go(x + pi[1], y + pj[1], 1, c, A[i][j] == '|');
			go(x + pi[2], y + pj[2], 2, c, A[i][j] == '-');
			go(x + pi[3], y + pj[3], 3, c, A[i][j] == '|');
		}
		memset(Map, 0, sizeof Map);
		For(i,1,n) For(j,1,m) if (isBlank(i, j)) {
			if (vec[i][j].empty()) {
				add(1, c + 1);
				add(c + 1, 1);
			} else if (vec[i][j].size() == 1) {
				add(vec[i][j][0].first + c * (!vec[i][j][0].second), vec[i][j][0].first + c * (vec[i][j][0].second));
			} else {
				assert(vec[i][j].size() == 2);
				add(vec[i][j][0].first + c * (!vec[i][j][0].second), vec[i][j][1].first + c * (vec[i][j][1].second));
				add(vec[i][j][1].first + c * (!vec[i][j][1].second), vec[i][j][0].first + c * (vec[i][j][0].second));
			}
		}
		For(i,1,c) {
			if (forbid[i][0]) add(i, i + c);
			if (forbid[i][1]) add(i + c, i);
		}
		For(k,1,c + c) For(i,1,c + c) For(j,1,c + c) Map[i][j] |= Map[i][k] && Map[k][j];
		bool no = false ;
		For(i,1,c) if (Map[i][i + c] && Map[i + c][i]) no = true;
		memset(label, 0, sizeof label);
		int t = 0;
		For(i,1,c + c) if (!label[i]) {
			label[i] = ++t;
			For(j,i + 1,c + c) if (Map[i][j] && Map[j][i]) label[j] = label[i];
		}
		memset(nMap, 0, sizeof nMap);
		For(i,1,c + c) For(j,1,c + c) if (Map[i][j] && label[i] != label[j]) {
			nMap[label[i]][label[j]] = true;
		}
		memcpy(Map, nMap, sizeof nMap);
		memset(in, 0, sizeof in);
		For(i,1,t) For(j,1,t) if (Map[i][j]) ++in[j];
		int hd = 0, tl = 0;
		For(i,1,t) if (!in[i]) q[++tl] = i;
		while (hd != tl) {
			int v = q[++hd];
			For(j,1,t) if (Map[v][j]) {
				if (--in[j] == 0) {
					q[++tl] = j;
				}
			}
		}
		For(i,1,tl) bel[q[i]] = i;
		For(i,1,c) ans[i] = (bel[label[i]] < bel[label[i + c]]);
		c = 0;
		printf("Case #%d: ", TK);
		if (!no) {
			puts("POSSIBLE");
			For(i,1,n) For(j,1,m) if (isShooter(i, j)) {
				++c;
				if (ans[c]) {
					if (A[i][j] == '-') A[i][j] = '|';
					else A[i][j] = '-';
				}
			}
			For(i,1,n) puts(A[i] + 1);
		} else puts("IMPOSSIBLE");
	}
	return 0;
}