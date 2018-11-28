#include <bits/stdc++.h>

using namespace std;
#define maxn 111
typedef vector<int> vi;

int n, p;
int r[maxn];
vector<vi> a (maxn);
int stat [maxn];

bool check (int cnt){
	for (int i = 0; i < n; i++){
		double hi = 1.0 * r[i] * cnt * 1.1;
		double lo = 1.0 * r[i] * cnt * 0.9;

		if (!(lo <= a[i][stat[i]] && a[i][stat[i]] <= hi)){
			return false;
		}
	}
	return true;
}

void inc_stat (){
	double min_cnt = 1.0 * a[0][stat[0]] / r[0];
	int arc_min_cnt = 0;
	for (int i = 0; i < n; i++){
		if (1.0 * a[i][stat[i]] / r[i] < min_cnt){
			min_cnt = 1.0 * a[i][stat[i]] / r[i];
			arc_min_cnt = i;
		}
	}
	stat[arc_min_cnt]++;
}

int main (){
	ios_base::sync_with_stdio(0);
	freopen("a.inp", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		cin >> n >> p;
		for (int i = 0; i < n; i++){
			a[i].assign (p, 0);
			stat[i] = 0;
		}

		for (int i = 0; i < n; i++){
			cin >> r[i];
		}
		for (int i = 0; i < n; i++){
			for (int j = 0; j < p; j++){
				cin >> a[i][j];
			}
			sort (a[i].begin (), a[i].end ());
		}

		bool done = false;
		int ret = 0;
		while (!done){

			for (int i = 0; i < n; i++){
				if (stat[i] >= p) done = true; 
			}
			if (done) break;
			double cnt = 0;
			for (int i = 0; i < n; i++){
				cnt += 1.0 * a[i][stat[i]] / r[i];
			}
			cnt /= n;

			if (check ( (ceil (cnt))) || check (floor(cnt))) {
				for (int i = 0; i < n; i++){
					stat[i] += 1;
				}
				ret += 1;
			}
			else {
				inc_stat();
			}
		}
		cout << "Case #" << t << ": " << ret << endl; 
	}
}