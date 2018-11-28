#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
	int T;
	cin >> T;
	for(int _t = 1; _t <= T; _t++) {
		int d, n;
		cin >> d >> n;
		vector<double> k(n), s(n);
		
		double t1, t2;
		vector< pair<double, double> > p(n);
		for(int i=0; i<n; i++) {
			cin >> t1 >> t2;
			p[i] = make_pair(t1, t2);
		}
		
		sort(p.begin(), p.end());
		
		p.push_back(make_pair(2e9, 2e9));
		
		for(int i=n-2; i>=0; i--) {
			double k1 = p[i].first, s1 = p[i].second;
			double k2 = p[i+1].first, s2 = p[i+1].second;
			
			if(s2 >= s1) continue;
			double t = (k1 - k2)/(s2 - s1);
			double t_add = (d - k1 - s1*t)/(s2);
			
			if(t_add < 0) continue;
			double v_avg = (d - k1)/(t + t_add);
			p[i] = make_pair(k1, v_avg);
		}
	
		double k1 = p[0].first, s1 = p[0].second;
		printf("Case #%d: ", _t);
		printf("%.7f\n", d*s1/(d - k1));
	}
	return 0;
}
