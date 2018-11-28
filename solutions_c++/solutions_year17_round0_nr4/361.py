#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define F first
#define S second

bool cb1[105][105], cb2[105][105];
vector<int> gr[404];
bool cap[404][404];
bool visit[404];

bool dfs(int x, int t) {
	if (visit[x]) return false;
	if (x==t) return true;
	visit[x]=true;
	for (int y : gr[x]) {
		if (cap[x][y]) {
			if (dfs(y,t)) {
				cap[x][y]=false;
				cap[y][x]=true;
				return true;
			}
		}
	}
	return false;
}

char result(int r, int c) {
	if (cb1[r][c]&&cb2[r][c]) return 'o';
	if (cb1[r][c]) return '+';
	if (cb2[r][c]) return 'x';
	return '.';
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	for (int tc=1;tc<=tcs;tc++) {
		int n,m;
		cin>>n>>m;
		for (int i=1;i<=n;i++) {
			for (int j=1;j<=n;j++) {
				cb1[i][j]=false;
				cb2[i][j]=false;
			}
		}
		for (int i=0;i<m;i++) {
			string s;
			int r,c;
			cin>>s>>r>>c;
			if (s[0]=='+' || s[0]=='o') cb1[r][c]=true;
			if (s[0]=='x' || s[0]=='o') cb2[r][c]=true;
		}
		set<pair<int,int>> toChange;
		set<int> rRow, rCol;
		int score=0;
		for (int i=1;i<=n;i++) {
			for (int j=1;j<=n;j++) {
				if (cb2[i][j]) {
					rRow.insert(i);
					rCol.insert(j);
					score++;
				}
			}
		}
		int cCol=1;
		for (int i=1;i<=n;i++) {
			if (rRow.count(i)) continue;
			while (rCol.count(cCol)) cCol++;
			cb2[i][cCol]=true;
			toChange.insert({i,cCol});
			score++;
			cCol++;
		}
		for (int i=1;i<=4*n;i++) gr[i].clear();
		set<int> bdia1, bdia2;
		for (int i=1;i<=n;i++) {
			for (int j=1;j<=n;j++) {
				if (cb1[i][j]) {
					score++;
					bdia1.insert(i+j);
					bdia2.insert(i-j);
				}
			}
		}
		for (int i=2;i<=2*n;i++) {
			gr[1].push_back(i);
			gr[i].push_back(1);
			cap[1][i]=true;
			cap[i][1]=false;
		}
		for (int i=1;i<=n;i++) {
			for (int j=1;j<=n;j++) {
				if (bdia1.count(i+j) || bdia2.count(i-j)) continue;
				gr[i+j].push_back(3*n+(i-j));
				gr[3*n+(i-j)].push_back(i+j);
				cap[i+j][3*n+(i-j)]=true;
				cap[3*n+(i-j)][i+j]=false;
			}
		}
		for (int i=2*n+1;i<4*n;i++) {
			gr[i].push_back(4*n);
			gr[4*n].push_back(i);
			cap[i][4*n]=true;
			cap[4*n][i]=0;
		}
		while (true) {
			for (int i=1;i<=4*n;i++) visit[i]=false;
			bool changed=dfs(1,4*n);
			if (changed) score++;
			else break;
		}
		for (int i=2;i<=2*n;i++) {
			if (cap[i][1]==0) continue;
			for (auto x : gr[i]) {
				if (cap[i][x]==false) {
					int d1=i;
					int d2=x-3*n;
					int r=(d1+d2)/2;
					int c=(d1-d2)/2;
					toChange.insert({r,c});
					cb1[r][c]=true;
				}
			}
		}
		cout<<"Case #"<<tc<<": "<<score<<" "<<toChange.size()<<"\n";
		for (auto x : toChange) {
			cout<<result(x.F,x.S)<<" "<<x.F<<" "<<x.S<<"\n";
		}
	}
}
