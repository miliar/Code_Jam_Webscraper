#include <bits/stdc++.h>
using namespace std;

#define pb         push_back

typedef long long ll;
const ll INF = 1000000000000000000ll;
const ll MOD = 1000000007ll;
const double EPS = 1e-8;

int main(void) {
	//ios_base::sync_with_stdio(false);
	//cin.tie(0);
	
	int t;
	cin >> t;

	for(int l=0; l<t; l++){
		int n, d;
		cin >> d >> n;
		vector<int> k;
		vector<int> s;

		double maxt = 0;
		for(int i=0; i<n; i++){
			int t1, t2;
			cin >> t1 >> t2;
			k.pb(t1);
			s.pb(t2);

			double time = (d - k[i]) * 1.0 / s[i];
			if(time > maxt){
				maxt = time;
			}
		}

		double ans = d / maxt;
		printf("Case #%d: %.8f\n", l+1, ans);
	}
	
	
	return 0;
}
