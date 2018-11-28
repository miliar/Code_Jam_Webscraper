#include <bits/stdc++.h>

using namespace std;

#define REP(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define one first
#define two second
typedef long long ll;
typedef pair<int, int> pi;
const int INF = 0x3f2f1f0f;

const int MAX_N = 55;

int N, M; char Mp[MAX_N][MAX_N];
pi move(pi p, int d) {
	pi r = p;
	r.one += "2101"[d] - '1';
	r.two += "1012"[d] - '1';
	return r;
}
bool isIn(pi r) {
	return r.one >= 0 && r.one < N && r.two >= 0 && r.two < M;
}
bool Vis[MAX_N][MAX_N];
vector<pair<pi, int> > Ed[MAX_N][MAX_N];
pi whereD(pi p, int d, int fillK) {
	pi r = move(p, d);
	while(isIn(r)) {
		char c = Mp[r.one][r.two];
		if(c == '-' || c == '|' || c == '#') return r;
		if(c == '/') d ^= 1;
		if(c == '\\') d ^= 3;
		if(fillK == 10) Vis[r.one][r.two] = true;
		if(fillK >= 0 && fillK < 4) {
			Ed[r.one][r.two].push_back(make_pair(p, fillK % 2));
//			printf("%d %d pushed by (%d %d (%d))\n", r.one, r.two, p.one, p.two, d);
		}
		r = move(r, d);
	}
	return r;
}

const int fre = 1;
void PROCESS(int tc) {
	printf("Case #%d: ", tc);
	scanf("%d%d", &N, &M);
	for(int i=0; i<N; i++) scanf("%s", Mp[i]);
	for(int i=0; i<N; i++) for(int j=0; j<M; j++) Vis[i][j] = false;
	for(int i=0; i<N; i++) for(int j=0; j<M; j++) Ed[i][j].clear(), Ed[i][j].shrink_to_fit();

	for(int i=0; i<N; i++) for(int j=0; j<M; j++) if(Mp[i][j] == '-' || Mp[i][j] == '|') {
		bool meets[2] = {false, false};
		pi list[4];
		for(int d=0; d<4; d++) list[d] = whereD(pi(i, j), d, -1);
		for(int d=0; d<4; d++) {
			if(isIn(list[d]) == false) continue;
			char c = Mp[list[d].one][list[d].two];
			if(c == '-' || c == '|') meets[d%2] = true;
		}
		if(meets[0] & meets[1]) {puts("IMPOSSIBLE");return;}
		if(meets[0]) {
			Mp[i][j] = '-';
			for(int d=1; d<4; d+=2) whereD(pi(i, j), d, 10);
		}else if(meets[1]) {
			Mp[i][j] = '|';
			for(int d=0; d<4; d+=2) whereD(pi(i, j), d, 10);
		}else Mp[i][j] = '*';
	}
	for(int i=0; i<N; i++) for(int j=0; j<M; j++) if(Mp[i][j] == '*')
		for(int d=0; d<4; d++) whereD(pi(i, j), d, d);
//	for(int i=0; i<N; i++, puts("")) for(int j=0; j<M; j++) printf("%d ", Vis[i][j]);
	while(1) {
		bool changed = false;
		for(int i=0; i<N; i++) for(int j=0; j<M; j++)  {
			if(Mp[i][j] == '.' && Vis[i][j] == false) {
			vector<pair<pi, int>> now;
			for(auto &list : Ed[i][j]) {
				pi p; int d; tie(p, d) = list;
				if(Mp[p.one][p.two] == '*') {
					now.push_back(list);
				}
			}
			if(now.size() == 0) { puts("IMPOSSIBLE");return; }
			if(now.size() == 1) {
				pi p; int nd; tie(p, nd) = now[0];
				if(nd == 1) {
					Mp[p.one][p.two] = '-';
					for(int d=1; d<4; d+=2) whereD(p, d, 10);
				}else{
					Mp[p.one][p.two] = '|';
					for(int d=0; d<4; d+=2) whereD(p, d, 10);
				}
				changed = true;
			}
		}
		}
		if(changed == false) break;
	}
	for(int i=0; i<N; i++) for(int j=0; j<M; j++) if(Mp[i][j] == '*') Mp[i][j] = '-';

	puts("POSSIBLE");
	for(int i=0; i<N; i++) printf("%s\n", Mp[i]);
}
int main() {
	if(fre) freopen("output.txt", "w", stdout);
	int TC; cin >> TC;
	for(int tc=1; tc<=TC; tc++) PROCESS(tc);
	return 0;
}