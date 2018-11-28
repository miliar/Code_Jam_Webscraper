#include <bits/stdc++.h>
using namespace std;

double pi = 3.14159265359;
vector< pair<double, double> >  a;
int N, K;

double solve() {
	cin >> N >> K;
	a.resize(N);
	double ans = 0;
	for (int i = 0; i < N; i++) {
		double r, h;
		cin >> r >> h;
		a[i].first = 2 * pi * r * h;
		a[i].second = pi * r * r; 
	}
	sort(a.begin(), a.end()); 
	reverse(a.begin(), a.end());
	for (int i = 0; i < N; i++) {
		//cout << i << ' ';
		double tmp = a[i].second, sum = a[i].first;
		int cnt = 1;
		for (int j = 0; j < N && cnt < K; j++) 
			if (a[j].second <= tmp && j != i) {
				cnt += 1;
				sum += a[j].first;
			}
		if (cnt == K)
			ans = max(ans, sum + tmp);	
	}
	//cout << endl;
	return ans;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		printf("%.8f\n", solve());
	}
	return 0;
}

