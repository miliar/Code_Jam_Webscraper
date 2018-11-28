#include <algorithm>
#include <cstdio>
#include <iostream>
#include <vector>


using namespace std;

#define PI 3.141592653587932

int t, k;
double R, H;
int N, K;
typedef pair<double, double> Pair;
vector<Pair> c;

int cmp(Pair x, Pair y) {
	return x.first * x.second > y.first * y.second;
}

void fun () {
	double sum  = 0;
	double sum_h = 0;
	double max_r = -1;
	int max_r_p = 0;
	sort(c.begin(), c.end(), cmp);
	double mx = 0;
	for (int i = 0; i < N; i ++ ) {
    	double ans = c[i].first * c[i].first + 2.0 * c[i].first * c[i].second;
		int cnt = 0;
        for(int j = 0; j < N; j++) {
        	if (cnt == K - 1) { 
        		break;
        	}
        	if (j != i && c[j].first <= c[i].first) {
            	cnt++;
            	ans += 2.0 * c[j].first * c[j].second;
        	}
     	}
    	mx = max(mx, ans);
    }
	// for (int i = 0; i < K; i ++ ) {
	// 	// max_r = max(max_r, c[i].first);
	// 	if (c[i].first > max_r) {
	// 		max_r = c[i].first;
	// 		max_r_p = i;
	// 	} else {
	// 		sum_h += c[i].second * c[i].first * 2 * PI;
	// 	}
	// }
	// double max_r_s = PI * max_r * max_r + c[max_r_p].second * max_r * max_r * 2 * PI;
	// for (int i = K; i < N; i ++ ) {
	// 	double r = c[i].first;
	// 	double h = c[i].second;
	// 	double tmp_s = r * r * PI + h * PI * 2;
	// 	if (tmp_s > max_r_s) {
	// 		max_r_p = tmp_s;
	// 	}
	// }
	// double res = max_r_p + 2 * sum_h * max_r * PI;
	printf("%.9lf\n", mx * PI);
}

int main () {
	freopen("A-large.in", "r", stdin);
	freopen("out", "w", stdout);
	cin >> t;
	for (int i = 0; i < t ; i ++ ) {
		c.clear();
		cin >> N >> K;
		cout << "Case #" << i + 1 << ": ";
		for (int j = 0; j < N; j ++ ) {
			cin >> R >> H;
			c.push_back(make_pair(R, H));
		}
		fun();
	}
	return 0;
}

