#include "bits/stdc++.h"


using namespace std;
#define ll long long
#define sz(a) 			    (int) a.size()
#define all(a) 				a.begin(), a.end()

int main(){
	#ifdef KP
		freopen("zaa.in","r",stdin);
		freopen("zaa.out","w",stdout);
	#endif
	int testcases = 1;
	cin >> testcases;
	for(int tc = 1; tc <= testcases; ++tc){
		cout << "Case #" << tc << ": ";
		int d, n;
		cin >> d >> n;
		vector<pair<int, int> > one(n);
		int tmp, tmp2;
		for(int i = 0; i < n; ++i){
			cin >> tmp;
			cin >> tmp2;
			one[i].first = d-tmp;
			one[i].second = tmp2;
		}
		sort(all(one));
		vector<float> ans(n);
		for(int i = 0; i < n; ++i){
			ans[i] = (float)one[i].first/(float)one[i].second;
			// cout << ans[i] << " ";
		}
		sort(all(ans));
		float time = ans[sz(ans)-1];
		float ans1 = (float)d/time;
//		cout << time << endl;
		printf("%.6f\n", ans1);
	}
	return 0;
}