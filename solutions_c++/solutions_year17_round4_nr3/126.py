#include<stdio.h>
#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
#include<memory.h>
#include<map>
#include<set>
#include<queue>
#include<list>
#include<sstream>
#define mp make_pair
#define pb push_back      
#define F first
#define S second
#define SS stringstream
#define sqr(x) ((x)*(x))
#define m0(x) memset(x,0,sizeof(x))
#define m1(x) memset(x,63,sizeof(x))
#define CC(x) cout << (x) << endl
#define pw(x) (1ll<<(x))
#define M 1000000007
#define N 111111
using namespace std;
typedef pair<int,int> pt;

int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
int bad;

int n, m, k;
string fi[111];

vector<int> v[N], rev[N];
int was[N];
vector<int> order;
int id[111][111];

int turn(char mir, int d) {
	if (mir == '/') {
		if (d == 0) return 1;
		if (d == 1) return 0;
		if (d == 2) return 3;
		if (d == 3) return 2;
	} else {
		if (d == 0) return 3;
		if (d == 1) return 2;
		if (d == 2) return 1;
		if (d == 3) return 0;
	}
}



int nt(int x) {
	if (x < k) x += k; else x -= k;
	return x;
}

void go(int x) {
	if (was[x]) return;
	was[x] = 1;
	for (int i = 0; i < v[x].size(); i++) go(v[x][i]);
	order.pb(x);
}

void col(int x, int o) {
	if (was[x]) return;
	was[x] = o;
	for (int i = 0; i < rev[x].size(); i++) col(rev[x][i], o);
}


int main(){
	freopen("1.in","r",stdin);	
	freopen("1.out","w",stdout);
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		cin >> n >> m;
		for (int i = 0; i < n; i++) cin >> fi[i];

		k = 0;
		for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) if (fi[i][j] == '-' || fi[i][j] == '|') {
			id[i][j] = k++;
		}
		for (int i = 0; i < k + k; i++) v[i].clear();
		bad = 0;

		for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) if (fi[i][j] == '.' || fi[i][j] == '-' || fi[i][j] == '|') {
			vector<pair<int, int> > w;
			vector<int> types;
			vector<int> myt;
			for (int d = 0; d < 4; d++) {
				int dd = d;
				int x = i + dx[dd];
				int y = j + dy[dd];
				while (x >= 0 && x < n && y >= 0 && y < m && (fi[x][y] == '.' || fi[x][y] == '/' || fi[x][y] == '\\')) {
					if (fi[x][y] == '/' || fi[x][y] == '\\') {
						dd = turn(fi[x][y], dd);	
					}
					x += dx[dd];
					y += dy[dd];
				}
				if (x < 0 || x >= n || y < 0 || y >= m) continue;
				if (fi[x][y] == '-' || fi[x][y] == '|') {
					w.pb(mp(x, y));
					if (dd == 0 || dd == 2) types.pb(0); else types.pb(1);
					if (d == 0 || d == 2) myt.pb(0); else myt.pb(1);
				}
			}
			if (fi[i][j] != '.') {
				for (int j = 0; j < w.size(); j++) {
					int t = id[w[j].F][w[j].S];

					int bd = t;
					if (types[j] == 1) bd = nt(bd);
					v[bd].pb(nt(bd));

				}	
			} else {
				if (w.size() == 0 || w.size() > 3) bad = 1;

				vector<int> goods;
				for (int j = 0; j < w.size(); j++) {
					int t = id[w[j].F][w[j].S];
					int need = t;
					if (types[j] == 1) need = nt(need);
					goods.pb(need);
				}
				if (w.size() == 3) {
					int x = -1;
					if (myt[0] != myt[1] && myt[0] != myt[2]) x = 0; else
					if (myt[0] != myt[1] && myt[1] != myt[2]) x = 1; else x = 2;

					v[nt(goods[x])].pb(goods[x]);
				}

				if (w.size() == 1) {
					v[nt(goods[0])].pb(goods[0]);
				} else if (w.size() == 2) {
					v[nt(goods[0])].pb(goods[1]);
					v[nt(goods[1])].pb(goods[0]);
				}
			}
		}
		for (int i = 0; i < k + k; i++) rev[i].clear();
		for (int i = 0; i < k + k; i++) for (int j = 0; j < v[i].size(); j++) rev[v[i][j]].pb(i);
		order.clear();
		for (int i = 0; i < k + k; i++) was[i] = 0;
		for (int i = 0; i < k + k; i++) if (!was[i]) go(i);
		for (int i = 0; i < k + k; i++) was[i] = 0;
		int cmp = 0;
		for (int i = order.size() - 1; i >= 0; i--) if (!was[order[i]]) {
			cmp++;
			col(order[i], cmp);
		}
		for (int i = 0; i < k; i++) if (was[i] == was[i + k]) bad = 1;

		if (bad) {
			cout << "Case #" << tt << ": IMPOSSIBLE" << endl;
			continue;
		}


		cout << "Case #" << tt << ": POSSIBLE" << endl;
		for (int i = 0; i < n; i++) for (int j = 0; j < m; j++) if (fi[i][j] == '|' || fi[i][j] == '-') {
			int t = id[i][j];
			if (was[t] > was[t + k]) fi[i][j] = '|'; else fi[i][j] = '-';
		}
		for (int i = 0; i < n; i++) cout << fi[i] << endl;


	}
	return 0;
}