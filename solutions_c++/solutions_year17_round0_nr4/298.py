#include<bits/stdc++.h>

using namespace std;

#define x first
#define y second
#define pb push_back
#define eb emplace_back

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int maxn = 210, maxd = 2 * maxn - 1, maxm = maxn * maxn;

#define DBG(x) cerr << __LINE__ << ": " << #x << " = " << (x) << endl

string G[maxn], NG[maxn];
bool seep[4][maxn][maxn];
bool freexrow[maxn], freexcol[maxn];

// 'o' = 'x' + '+'
bitset<maxd> matchvis;
vvi matchadj;
vi matchpar;

bool match(int cur)
{
	for (int nxt : matchadj[cur]) {
		if (matchvis.test(nxt)) continue;
		matchvis.set(nxt);
		if (matchpar[nxt] == -1 || match(matchpar[nxt])) {
			matchpar[nxt] = cur;
			return true;
		}
	}
	return false;
}

int maxmatch(int nodesLeft, int nodesRight)
{
	matchpar.assign(nodesRight, -1);
	int ret = 0;
	while (nodesLeft--) {
		matchvis.reset();
		ret += match(nodesLeft);
	}
	return ret;
}

void setMove(int &cnt, int row, int col, char ch) {
	// cerr << "CHANGE " << row << ", " << col << " TO " << x << endl;
	if (NG[row][col] == 'o') return;
	if (ch == 'x') {
		if (NG[row][col] != 'x') cnt++;
		if (NG[row][col] == '+') 	NG[row][col] = 'o';
		else						NG[row][col] = 'x';
	} else {
		if (NG[row][col] != '+') cnt++;
		if (NG[row][col] == 'x') NG[row][col] = 'o';
		else					NG[row][col] = '+';
	}
}

bool run(int testcase)
{
	for (int i = 0; i < maxn; i++) G[i] = string(maxn, '.');

	int N, M;
	cin >> N >> M;
	for (int i = 0; i < M; i++) {
		char type;
		int x, y;
		cin >> type >> x >> y;
		G[--x][--y] = type;
	}
	for (int i = 0; i < N; i++) NG[i] = G[i];

	int ans = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (G[i][j] == 'o') ans += 2;
			else if (G[i][j] != '.') ans++;
		}
	}

	// HORIZONTAL AND VERTICAL
	fill_n(freexrow, maxn, true);
	fill_n(freexcol, maxn, true);

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (G[i][j] == 'x' || G[i][j] == 'o') {
				freexrow[i] = freexcol[j] = false;
			}
		}
	}

	int emptyxrow = 0, emptyxcol = 0;
	for (int i = 0; i < N; i++) {
		emptyxrow += !freexrow[i];
		emptyxcol += !freexcol[i];
	}

	if (emptyxrow < emptyxcol) {
		for (int r = 0, c = 0; r < N; r++) {
			if (!freexrow[r]) continue;
			while (!freexcol[c]) c++;
			setMove(ans, r, c++, 'x');
		}
	} else {
		for (int r = 0, c = 0; c < N; c++) {
			if (!freexcol[c]) continue;
			while (!freexrow[r]) r++;
			setMove(ans, r++, c, 'x');
		}
	}

	// DIAGONALS
	int numd = 2 * N - 1;
	matchadj.assign(numd, vi());

	int dr[4] = { 1, 1, -1, -1 }, dc[4] = { 1, -1, -1, 1 };
	int sr[4] = { 0, 0, N - 1, N - 1 }, sc[4] = { 0, N - 1, N - 1, 0 };
	int tr[4] = { N, N, -1, -1 }, tc[4] = { N, -1, -1, N };

	for (int dir = 0; dir < 4; dir++) {
		for (int r = sr[dir]; r != tr[dir]; r += dr[dir]) {
			for (int c = sc[dir]; c != tc[dir]; c += dc[dir]) {
				seep[dir][r][c] = (G[r][c] == '+' || G[r][c] == 'o');
				if (r != sr[dir] && c != sc[dir]) {
					seep[dir][r][c] |= seep[dir][r - dr[dir]][c - dc[dir]];
				}
			}
		}
	}
/*
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			seepdown[i][j] = (G[i][j] == '+' || G[i][j] == 'o');
			if (i > 0 && j > 0)
				seepdown[i][j] |= seepdown[i - 1][j - 1];
			if (i > 0 && j + 1 < N)
				seepdown[i][j] |= seepdown[i - 1][j + 1];
		}
	}
	for (int i = N; i--; ) {
		for (int j = 0; j < N; j++) {
			seepup[i][j] = (G[i][j] == '+' || G[i][j] == 'o');
			if (i + 1 < N && j > 0)
				seepup[i][j] |= seepup[i + 1][j - 1];
			if (i + 1 < N && j + 1 < N)
				seepup[i][j] |= seepup[i + 1][j + 1];
		}
	}
*/
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			bool seePlus = seep[0][i][j] || seep[1][i][j] || seep[2][i][j] || seep[3][i][j];
			// cerr << "(" << i << ", " << j << ")";
			// for (int k = 0; k < 4; k++) cerr << " " << seep[k][i][j];
			// cerr << endl;
			// cerr << i << " " << j << ": " << seepup[i][j] << " " << seepdown[i][j] << endl;
			if (!seePlus) {
				int d1 = i + j;
				int d2 = i + (N - 1 - j);
				matchadj[d1].pb(d2);
				// cerr << "x at (" << i << ", " << j << ") ~ /" << d1 << "/" << d2 << "/" << endl;
			}
		}
	}

	int nmatch = maxmatch(numd, numd);
	int realnmatch = 0;
	for (int d2 = 0; d2 < numd; d2++) {
		if (matchpar[d2] < 0) continue;

		realnmatch++;
		int d1 = matchpar[d2];
		int i = (d1 + d2 - N + 1) / 2;
		int j = (d1 - d2 + N - 1) / 2;
		// cerr << "CONNECT AT " << i << ", " << j << endl;
		setMove(ans, i, j, '+');
	}
	assert(realnmatch == nmatch);

	cout << "Case #" << testcase << ": ";
	int cnt = 0;
	stringstream ss;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			if (G[i][j] != NG[i][j]) {
				ss << NG[i][j] << " " << (i + 1) << " " << (j + 1) << endl;
				cnt++;
			}
		}
	}
	cout << ans << " " << cnt << endl;
	cout << ss.str();
	cout.flush();

	for (int j = 0; j < N; j++) {
		int cntnp = 0;
		for (int i = 0; i < N; i++) {
			if (NG[i][j] != '.' && NG[i][j] != '+') cntnp++;
		}
		assert(cntnp <= 1);
	}
	for (int i = 0; i < N; i++) {
		int cntnp = 0;
		for (int j = 0; j < N; j++) {
			if (NG[i][j] != '.' && NG[i][j] != '+') cntnp++;
		}
		assert(cntnp <= 1);
	}
	for (int d = 0; d < numd; d++) {
		int cntnx = 0;
		for (int i = 0; i < N; i++) {
			// d1 = i + j
			int j = d - i;
			if (0 <= j && j < N) {
				if (NG[i][j] != '.' && NG[i][j] != 'x') cntnx++;
			}
		}
		assert(cntnx <= 1);
	}
	for (int d = 0; d < numd; d++) {
		int cntnx = 0;
		for (int i = 0; i < N; i++) {
			// d1 = i + N - 1 - j
			int j = i + N - 1 - d;
			if (0 <= j && j < N) {
				if (NG[i][j] != '.' && NG[i][j] != 'x') cntnx++;
			}
		}
		assert(cntnx <= 1);
	}

	return true;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int ntc;
	cin >> ntc;
	for (int i = 1; i <= ntc; i++) {
		if (!run(i)) cerr << "Something went wrong" << endl;
	}
	return 0;
}

