#include<bits/stdc++.h>
using namespace std;
#define ALL(v) (v).begin(),(v).end()
int N, K;
double p0[55];
double calc(vector<double> p) {
	double answer = 1;
	for (auto d : p) answer *= d;
	return answer;
}
int main() {
	int T; cin >> T;
	for(int tc=1;tc<=T;tc++) {
		cin >> N >> K;
		double q; cin >> q;
		for (int i=0; i<N; i++) cin >> p0[i];
		double l=0, r=1;
		for (int it=0; it<100; it++) {
			double m = (l + r) / 2;
			double need = 0;
			for (int i=0; i<N; i++) need+=max(0.0, m-p0[i]);
			if (need <= q) l = m; else r = m;
		}
		for (int i=0; i<N; i++) p0[i] = max(p0[i], l);
		printf("Case #%d: %.9lf\n", tc, calc(vector<double>(p0,p0+N)));
	}
}
