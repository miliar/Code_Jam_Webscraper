#include <iostream>
#include <vector>

using namespace std;

int nvert;

vector<bool> crapi, crapj;
vector<vector<bool> > graph;
vector<int> match;

vector<bool> vis;

bool augment(int i) {
	//cerr << "1";
	if (vis[i]) return false;
	if (crapi[i]) return false;
	vis[i]=true;
	for (int j=0;j<nvert;++j) if (crapj[j]==false && graph[i][j]) if (match[j]<0 || augment(match[j])) {
		match[j]=i; return true;
	}
	return false;
}

void bipmatch() {
	for (int i=0;i<nvert;++i) {
		//cerr << endl;
		vis = vector<bool>(nvert, false);
		augment(i);
	}
	return;
}

char addcross(char c) {
	if (c=='.') return 'c';
	if (c=='+' || c=='p') return 'r';
	return '!';
}

char addplus(char c) {
	if (c=='.') return 'p';
	if (c=='x' || c=='c') return 'r';
	cerr << "forbidden char: " << c << endl;
	return '!';
}

char lettertosymb(char c) {
	if (c=='p') return '+';
	if (c=='c') return 'x';
	if (c=='r') return 'o';
	return '!';
}

int main() {
	int T;
	cin >> T;
	for (int tc=1;tc<=T;++tc) {
		int n, m;
		cin >> n >> m;
		//vector<vector<char> > karta(n, vector<char>(n, '.'));
		char karta[100][100];
		for (int i=0;i<n;++i) for (int j=0;j<n;++j)karta[i][j]='.';
		while (m--) {
			char c;
			int i, j;
			cin >> c >> i >> j;
			karta[i-1][j-1]=c;
		}

/*		for (int i=0;i<n;++i) {
			for (int j=0;j<n;++j) cout << karta[i][j];
			cout << endl;
		}*/

		// add x
		nvert = n;
		crapi = vector<bool>(n, false);
		crapj = vector<bool>(n, false);

		graph = vector<vector<bool> >(n, vector<bool>(n, false));
		match = vector<int>(n, -1);

		for (int i=0;i<n;++i) for (int j=0;j<n;++j) {
			if (karta[i][j]=='x' || karta[i][j]=='o'){
				crapi[i]=true;
				crapj[j]=true;
			} else {
				graph[i][j]=true;
			}
		}

		bipmatch();

		for (int j=0;j<n;++j) if (match[j] != -1) karta[match[j]][j] = addcross(karta[match[j]][j]);

		// add +
		nvert = 2*n-1;
		crapi = vector<bool>(nvert, false);
		crapj = vector<bool>(nvert, false);

		graph = vector<vector<bool> >(nvert, vector<bool>(nvert, false));
		match = vector<int>(nvert, -1);

		for (int x=0;x<n;++x) for (int y=0;y<n;++y) {
			if (karta[x][y]=='+' || karta[x][y]=='o' || karta[x][y]=='r'){
				crapi[x+y]=true;
				crapj[x-y+(n-1)]=true;
			} else {
				graph[x+y][x-y+(n-1)]=true;
			}
		}
		bipmatch();
//		for (int i=0;i<nvert;++i) cout << "Match: " << match[i] << " " << i << endl;


		for (int j=0;j<2*n-1;++j) if (match[j] != -1) {
			int x=(match[j]+j-(n-1))/2, y=(match[j]-j+(n-1))/2;
			if (x<0 || x>=n || y<0 || y>=n) continue;
//			cerr << x << " " << y << endl;
			karta[x][y] = addplus(karta[x][y]);

		}
/*		for (int i=0;i<n;++i) {
			for (int j=0;j<n;++j) cout << karta[i][j];
			cout << endl;
		}*/
		int points=0, sp=0;
		for (int i=0;i<n;++i) for (int j=0;j<n;++j) {
			if (karta[i][j]!='.') ++points;
			if (karta[i][j]=='o' || karta[i][j]=='r') ++points;
			if (karta[i][j]=='p' || karta[i][j]=='c' || karta[i][j]=='r') ++sp;
		}
		cout << "Case #" << tc << ": " << points << " " << sp << endl;
		for (int i=0;i<n;++i) for (int j=0;j<n;++j) if (karta[i][j]=='p' || karta[i][j]=='c' || karta[i][j]=='r') {
			cout << lettertosymb(karta[i][j]) << " " << i+1 << " " << j+1 << endl;
		}
	}

	return 0;
}