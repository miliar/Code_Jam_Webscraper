#include <bits/stdc++.h>
using namespace std;

const int
	MAXN = 60;
	
const int
	MAXV = MAXN * MAXN * 2;	

int testCount;
int N, P;
int R[MAXN];
int I[MAXN][MAXN];

const pair<int, int> NONE = {-1, -1};

pair<int, int> get_k(int i, int p) {
	int hk = (10 * I[i][p]) / (R[i] * 9);
	int lk = (10 * I[i][p] + R[i] * 11 - 1) / (R[i] * 11);
	//if (lk != hk)
		//cerr << lk << " -> " << hk << endl;	
		
	if (!(9LL * lk * R[i] <= 10 * I[i][p] && 10 * I[i][p] <= 11 * lk * R[i]))
		return NONE;
	if (!(9LL * hk * R[i] <= 10 * I[i][p] && 10 * I[i][p] <= 11 * hk * R[i]))
		return NONE;
		
	return {lk, hk};
}

deque<pair<int, int>> p[MAXN];

int main() {
	
	cin >> testCount;
	for (int test = 1; test <= testCount; ++test) {
		
		cerr << test << endl;
		
		cin >> N >> P;
		for (int i = 0; i < N; ++i)
			cin >> R[i];
			
		for (int i = 0; i < N; ++i) {
			p[i].clear();
			for (int j = 0; j < P; ++j) {
				cin >> I[i][j];
				auto r = get_k(i, j);
				//cerr << I[i][j] << " " << r.first << " " << r.second << endl; 
				if (r != NONE)
					p[i].push_back(r);
			}
		}
		
		//cerr << endl;
			
		for (int i = 0; i < N; ++i)
			sort(p[i].begin(), p[i].end());
				
		int ans = 0;
		for (int c = 0; c < 1100000; ++c) {
			int cnt = 0;
			for (int i = 0; i < N; ++i) {
				if (p[i].empty()) break;
				if (p[i][0].first > c) { c = p[i][0].first - 1; break; }
				while (!p[i].empty() && p[i][0].second < c) p[i].pop_front();
				if (p[i].empty()) break;
				if (p[i][0].first <= c && c <= p[i][0].second) cnt++;
				else break;
			}
			if (cnt == N) {
				for (int i = 0; i < N; ++i)
					p[i].pop_front();
				ans++;
				c--;
			}
		}				
				
		cout << "Case #" << test << ": " << ans << endl;
	}
	
	return 0;
}
