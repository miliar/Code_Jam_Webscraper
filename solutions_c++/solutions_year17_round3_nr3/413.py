#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;

#define fi first
#define se second

vector<double> a;
double x;
double esp = 1e-8;

int main(){
	freopen("a.inp", "r", stdin);
	freopen("a.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		int n, k;
		cin >> n >> k;
		a.assign (n, 0);
		cin >> x;
		for (int i = 0; i < n; i++){
			cin >> a[i];
		}
		sort (a.begin (), a.end ());
		int id = 0;
		while (abs(x) > esp){
			while (id < n - 1 && abs(a[id] - a[id + 1]) < esp){
				id++;
			}

			double addup = x / (id + 1);
			if (id < n - 1 && a[id + 1] < a[id] + addup){
				addup = a[id + 1] - a[id];
			}

			for (int i = 0; i <= id; i++){
				x -= addup;
				a[i] += addup;
			}
		}
		double ret = 1;
		for (int i = 0; i < n; i++){
			ret = ret * (min (1.0, a[i]));
		}
		printf ("Case #%d: %.6f\n", t, ret);
	}

	return 0;
}