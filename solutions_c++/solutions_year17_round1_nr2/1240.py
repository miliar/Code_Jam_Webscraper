#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
const int maxn = 1e3 + 5;

bool check(double a, int b) {
	double c = a / b - 1;
	//cout << a  << " " << b << " " << c << endl;
	double up = 0.10000001, down = -0.100000001;
	if(c > down && c < up) return 1;
	return 0;
}

void solve() {
	int n, p, cnt = 0;
	cin >> n >> p;
	vector<int> need;
	double Q[maxn][maxn] = {};
	for(int i = 0; i < n; i++) {
		int tmp;
		cin >> tmp;
		need.push_back(tmp);
	}

	for(int i = 0; i < n; i++) for(int j = 0; j < p; j++) {
		int tmp;
		cin >> tmp;
		Q[i][j] = (double) tmp / need[i];
		//check(Q[i][j]);
	}
	for(int i = 0; i < n ; i++) sort(Q[i], Q[i]+p);
	/*for(int i = 0; i < n; i++) {
		for(int j = 0; j < p; j++) {
			cout << Q[i][j] << " ";
		}
		cout << endl;
	}*/
	int cur[maxn] = {};
	int ok = 1;
	while(ok) {
		for(int i = 0; i < n && ok; i++) if(cur[i] >= p) ok = 0;
		if(!ok) break;
		int mid = 0;
		double tmp = 0;
		for(int i = 0; i < n; i++) tmp += Q[i][cur[i]];
		tmp /= n;
		mid = (int) floor(tmp+0.5);
		bool wa = 0;
		for(int i = 0; i < n; i++) if(!check(Q[i][cur[i]], mid)) wa = 1;
		if(!wa){
			cnt++;
			for(int i = 0; i < n; i++) cur[i]++;
		}
		else{
			double mini = Q[0][cur[0]];
			int N = 0;
			for(int i =1; i < n; i++)
				if(Q[i][cur[i]] < mini) mini = Q[i][cur[i]], N = i;
			cur[N]++;
		}

	}
	cout << cnt << endl;
}



int main() {
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		cout << "Case #"<< i << ": ";
		solve();
	}
	return 0;
}
