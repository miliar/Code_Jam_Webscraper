#include <bits/stdc++.h>

#define i64 long long
#define u64 unsigned long long
#define i32 int
#define u32 unsigned int

#define pii pair<int, int>
#define pll pair<long long, long long>

#define ld long double
#define defmod 1000000007

#define mati64(a,b) vector<vector<i64>>(a, vector<i64>(b, 0));
using namespace std;

i64 e[110], s[110];
ld d[110][110];
void solve1(){
	int n, q; cin >> n >> q;
	for(int i = 1; i <= n; ++i)
		cin >> e[i] >> s[i];
	for(int i = 1; i <= n; ++i){
		for(int j = 1; j <= n; ++j)
			cin >> d[i][j];
	}
	cout << setprecision(20);
	while(q--){
		int a, b; cin >> a >> b;
		unordered_map<int, i64> dist[110];
		unordered_map<int, bool> d1[110];
		priority_queue<pair<ld, pair<int, pll>>> pq;
		pq.push({0, {a, {0, 0}}});
		while(!pq.empty()){
			ld dis = -pq.top().first;
			int cur = pq.top().second.first;
			pll ho = pq.top().second.second;
			pq.pop();
			if(d1[cur][ho.first])
				continue;
			d1[cur][ho.first] = 1;
			d1[cur][ho.first] = dis;
			if(cur == b){
				cout << dis << " ";
				break;
			}
			for(int i = 1; i <= n; ++i){
				if(i == cur || d[cur][i] == -1)
					continue;
				if(ho.first >= d[cur][i]){
					pq.push({-(dis+d[cur][i]/ho.second), {i, {ho.first-d[cur][i], ho.second}}});
				}
				if(e[cur] >= d[cur][i]){
					pq.push({-(dis+d[cur][i]/s[cur]), {i, {e[cur]-d[cur][i], s[cur]}}});
				}
			}
		}
	}
	cout << endl;
}

int main(){
	cin.sync_with_stdio(0);
	cin.tie(0);
	int tests;
	cin >> tests;
	for(int i = 1; i <= tests; ++i){
		cout << "Case #" << i << ": ";
		solve1();
	}
	return 0;
}
