#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;

double pi = M_PI;

struct B{
	double r, h, s1, s2;
};

B b[1005];

bool cmp(B a, B b){
	return a.s2 > b.s2;
}

int main(){
	int T;
	cin >> T;
	for (int K = 1; K <= T; K++){
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; i++){
			cin >> b[i].r >> b[i].h;
			b[i].s1 = pi * b[i].r * b[i].r;
			b[i].s2 = 2.0 * pi * b[i].r * b[i].h;
			//cout << b[i].s1 << " " << b[i].s2 << endl;
			//cout << b[i].s1 + b[i].s2 << endl;
		}
		sort(b, b + n, cmp);
		double ans = -1;
		for (int i = 0; i < n; i++){
			double cur = b[i].s1 + b[i].s2;
			int s = 1;
			for (int j = 0; j < n && s != k; j++){
				if (i == j) continue;
				if (b[j].r <= b[i].r){
					s++;
					cur += b[j].s2;
				}
			}
			ans = max(ans, cur);
		}
		cout << "Case #" << K << ": ";
		cout << fixed << setprecision(7) << ans << endl;
	}
	
	return 0;
}
