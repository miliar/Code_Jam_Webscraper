#include <bits/stdc++.h> 

using namespace std;

typedef long long ll; 
typedef pair<int, int> pii;

#define REP(i,n) for(int(i)=0;(i)<(int)(n);(i)++)

char b[110][110];
char ch[110][110];
int n;
char c;
int x, y;

void read() {
	int m;
	scanf("%d %d", &n, &m);
	
	REP(i,n) REP(j,n) b[i][j] = ' ';
	for (int i = 0; i < m; i++) {
		scanf(" %c %d %d", &c, &x, &y); x--; y--;
		b[x][y]=c;
	}
}

int g[310][310];
int seen[310];
int match[310];

bool bpm(int v) {
	if (seen[v]) return false;
	seen[v] = 1;

	for (int i = 0; i < 2*n - 1; i++) if (g[v][i]) {
		if (match[i] == -1 || bpm(match[i])) {
			match[i] = v;
			return true;
		}
	}

	return false;
}

void solve() {
	// place x
	REP(i,n) REP(j,n) ch[i][j] = b[i][j];

	vector<int> occrow(n,0);
	vector<int> occcol(n,0);
	for (int row = 0; row < n; row++) {
		for (int col = 0; col < n; col++) {
			if (b[row][col] == 'x' || b[row][col] == 'o') {
				occrow[row] = 1;
				occcol[col] = 1;
			}
		}
	}

	for (int row = 0; row < n; row++) {
		for (int col = 0; col < n; col++) if (!occrow[row] && !occcol[col]) {
			occrow[row] = occcol[col] = 1;

			if (b[row][col] == '+') ch[row][col] = 'o';
			else ch[row][col] = 'x';
		}
	}


	// place o
	memset(g,0,sizeof(g));

	vector<int> occdiagplus(2*n, 0);
	vector<int> occdiagminus(2*n, 0);
	for (int row = 0; row < n; row++) {
		for (int col = 0; col < n; col++) {
			if (ch[row][col] == '+' || ch[row][col] == 'o') {
				occdiagplus[row+col] = 1;
				occdiagminus[row-col+(n-1)] = 1;
			}
		}
	}

	for (int row = 0; row < n; row++) {
		for (int col = 0; col < n; col++) {
			if (!occdiagplus[row+col] && !occdiagminus[row-col+(n-1)]) {
				g[row+col][row-col+(n-1)]=1;
			}
		}
	}

	memset(match,-1,sizeof(match));
	for (int i = 0; i < 2*n - 1; i++) {
		memset(seen,0,sizeof(seen));
		bpm(i);
	}

	for (int i = 0; i < 2*n-1; i++) {
		if (match[i] != -1) {
			int dp = match[i];
			int dm = i - (n-1);

			int row = (dp+dm)/2;
			int col = (dp-dm)/2;

			if (ch[row][col] == 'x') ch[row][col] = 'o';
			else ch[row][col] = '+';
		}
	}

	int style = 0;
	vector< pair<char, pair<int, int> > > changes;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (ch[i][j] == 'o') style += 2;
			else if (ch[i][j] != ' ') style++;

			if (ch[i][j] != b[i][j]) changes.push_back({ch[i][j], {i,j}});
		}
	}

	printf("%d %d\n", style, changes.size());
	for (int i = 0; i < changes.size(); i++) {
		printf("%c %d %d\n", changes[i].first, changes[i].second.first + 1, changes[i].second.second + 1);
	}
}


























int myMod = 0;
int howMany = 1;

int main(int argc, char** argv) {
	if (argc > 1) {
		stringstream ss; ss << argv[1]; ss >> myMod;
		ss.str(""); ss.clear();
		ss << argv[2]; ss >> howMany;
	}

	int cases;
	scanf("%d", &cases);
	for (int i = 0; i < cases; i++) {
		read();
		if (i % howMany == myMod) {
			printf("Case #%d: ", i+1);
			solve();
		}
	}
}