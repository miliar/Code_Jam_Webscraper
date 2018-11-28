#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <iomanip>
#include <tuple>

using namespace std;

#define REP(i,n) for(int i = 0; i < (n); i++)
#define FOR(i,a,b) for(int i = (a); i <= (b); i++)
#define FORD(i,a,b) for(int i = (a); i >= (b); i--)

typedef pair<int, int> pii;
typedef tuple<double, int, int, int> tpl;
typedef long long ll;

const int MAX = 100 + 10;

int E[MAX], S[MAX];
int D[MAX][MAX];
double bests[MAX][MAX];
bool vis[MAX][MAX];
int N, Q;

double solveQ(int U, int V) {
	REP(i, N) REP(j, N) vis[i][j] = false;
	priority_queue<tpl> q;
	q.push(tpl(0, U, U, E[U]));
	while(q.size() > 0) {
		double time;
		int city, horse, ELeft;
		tie(time, city, horse, ELeft) = q.top();
		// cout << time << ' ' << city << ' ' << horse << ' ' << ELeft << endl;
		q.pop();
		time = -time;
		// cout << "N " << N << endl;
		if (vis[city][horse]) {
			if (bests[city][horse] < time) continue;
		}
		vis[city][horse] = true;
		bests[city][horse] = time;
		// cout << "N " << N << endl;
		while(true) {
			REP(i, N) {
				int dist = D[city][i];
				// cout << "dist " << dist << ' ' << city << ' ' << i << endl;
				if (dist == -1) continue;
				if (dist > ELeft) continue;
				double addTime = dist / (double) S[horse];
				q.push(tpl(-(time + addTime), i, horse, ELeft - dist));
			}
			if (horse == city) break;
			horse = city;
			ELeft = E[city];
		}
	}
	double best = INFINITY;
	REP(i, N) {
		if (vis[V][i]) {
			best = min(best, bests[V][i]);
		}
	}
	return best;
}

void solve() {
	cin >> N >> Q;
	REP(i, N) cin >> E[i] >> S[i];
	REP(i, N) REP(j, N) cin >> D[i][j];
	int U, V;
	REP(i, Q) {
		cin >> U >> V;
		cout << ' ' << solveQ(U-1, V-1);
	}
}

int main() {
	cout << fixed << setprecision(10);
	int t;
	cin >> t;
	REP(i, t) {
		cout << "Case #" << (i+1) << ":";
		solve();
		cout << endl;
	}
}