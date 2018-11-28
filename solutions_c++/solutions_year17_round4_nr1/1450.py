#include <bits/stdc++.h>

using namespace std;

int n, p;
int a[5];

map<vector<int>, bool> vs;
map<vector<int>, int> f;

int solve (vector<int> &x){
	bool isDone = true;
	for (int i = 0; i < p; i++){
		if (x[i] != 0) {
			isDone = false;
			break;
		}
	}
	if (isDone) return 0;
	
	if (vs[x]) 
		return f[x];
	vs[x] = 1;	
	int ret = 0;

	for (int i = 0; i < p; i++){
		if (x[i] == 0) continue;
		int tmp = (x[p] == 0);
		int leftover = 0;
		if (x[p] < i) leftover = x[p] + p - i;
		else leftover = x[p] - i;

		int last = x[p];
		x[p] = leftover;
		x[i]--;

		tmp += solve (x);

		x[p] = last;
		x[i]++;
		ret = max(ret, tmp);
	}
	f[x] = ret;
	return ret;
}

int main (){

	freopen("a.inp", "r", stdin);
	freopen("a.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		for (int i = 0; i < 5; i++)
			a[i] = 0;
		f.clear ();
		vs.clear ();
		cin >> n >> p;
		for (int i = 0 ; i < n; i++){
			int gi; cin >> gi;
			a[gi%p]++;
		}
		vector<int> x (p + 1, 0);
		for (int i = 0; i < p; i++){
			x[i] = a[i];
		}
		int ret = solve (x);

		cout << "Case #" << t << ": " << ret  << endl;
	}

    return 0;
}
