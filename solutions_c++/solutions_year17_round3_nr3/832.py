#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>


using namespace std;

const double eps = 1e-12;


int t;
int n, k;
double u;
double p[54];
double sum_p;

void fun () {
	double res = 1.0;
	double av;
	int cnt = 0;
	double les = 0.0;
	int end;
	sort(p, p + n);
	p[n] = 1.0;
	for (int i = 0; i < n; i ++ ) {
		double tmp = (i + 1) * (p[i + 1] - p[i]);
		// cout << "tmp" << tmp << endl;
		if (tmp <= u) {
			u -= tmp;
			av = p[i + 1];
		} else {
			av = p[i] + u / (i + 1);
			// cout << i << " ";
			end = i;
			break;
		}
		if (u <= 0.0) break;
	}
	// cout << av << " ";
	for (int i = 0; i < n; i ++ ) {
		if (i <= end) {
			res += log(av);
		} else {
			res += log(p[i]);
		}
	}
	printf("%.8lf\n", exp(res));
}

int main () {
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> t;
	for (int i = 0; i < t ; i ++ ) {
		cin >> n >> k;
		// sum_p = 0;
		cin >> u;
		for (int j = 0; j < n; j ++ ) {
			cin >> p[j];
			// sum_p += p[j];
		}
		cout << "Case #" << i + 1 << ": ";
		fun();
	}
	return 0;
}

