#include<cstdio>
#include<utility>
#include<vector>
#include<algorithm>
using namespace std;

const int NMAX = 50;
const int PMAX = 50;

int R[NMAX];
int Q[NMAX][PMAX];
typedef pair<int, int> pii;
pii range[NMAX][PMAX];
int N, P;

void input(){
	scanf("%d%d", &N, &P);
	for (int i = 0; i < N; i++) scanf("%d", R + i);
	for (int i = 0; i < N; i++)for (int j = 0; j < P; j++) scanf("%d", &Q[i][j]);

	for (int i = 0; i < N; i++) for (int j = 0; j < P; j++){
		int r = R[i], q = Q[i][j];
		int lo, hi;
		if ((10 * q) % (11 * r)) lo = (10 * q) / (11 * r) + 1;
		else lo = (10 * q) / (11 * r);
		if (!lo) lo = 1;
		hi = (10 * q) / (9 * r);
		range[i][j] = { lo, hi };
	}
}

int process(){
	vector<int> cands;
	for (int i = 0; i < N; i++) for (int j = 0; j < P; j++)
		cands.push_back(range[i][j].first), cands.push_back(range[i][j].second);
	sort(cands.begin(), cands.end());
	cands.erase(unique(cands.begin(), cands.end()), cands.end());

	vector<vector<pii>> M(N);
	for(int i=0;i<N;i++) for(int j=0;j<P;j++)
		if (range[i][j].first <= range[i][j].second) M[i].push_back(range[i][j]);

	int ret = 0;
	for (int c : cands){
		while (1){
			vector<int> idx(N, -1);
			for (int i = 0; i < N; i++) for (int j = 0; j < M[i].size(); j++){
				if (M[i][j].first <= c && c <= M[i][j].second){
					if (idx[i] == -1) idx[i] = j;
					else{
						if (M[i][idx[i]].second > M[i][j].second) idx[i] = j;
					}
				}
			}
			bool ok = true; for (int i = 0; i < N; i++) if (idx[i] == -1) ok = false;
			if (ok){
				ret++;
				for (int i = 0; i < N; i++) M[i].erase(M[i].begin() + idx[i]);
			}
			else break;
		}
	}
	return ret;
}

int main(){
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);

	int T; scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++){
		printf("Case #%d: ", tc);
		input();
		printf("%d\n", process());
	}
}