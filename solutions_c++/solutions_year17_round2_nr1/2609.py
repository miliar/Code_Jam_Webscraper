/*input

*/

#include <bits/stdc++.h>
using namespace std;
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define fst first
#define snd second
#define debug(x) cout << #x << " = " << x << endl;
typedef long long ll;
typedef pair<int, int> ii;

void arquivo(){
	freopen("a.in", "rt", stdin);
	freopen("a.out", "wt", stdout);
}

int main(){	

	arquivo();
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){

		int d, n;
		cin >> d >> n;
		double pos[n], vel[n];
		for(int i = 0; i < n; i++)
			cin >> pos[i] >> vel[i];

		double l = 0.0, r = 1e13;
		double ans = 0.0;

		for(int i = 0; i < 10000; i++){
			double mid = (l + r) / 2;
			bool ok = 1;
			double t1 = d / mid;	
			for(int j = 0; j < n && ok; j++){
				double t2 = (d - pos[j]) / vel[j];				
				if(t1 < t2)
					ok = 0;	
			}

			if(ok){
				ans = mid;
				l = mid;
			}
			else
				r = mid;

		}

		printf("Case #%d: ", t);
		printf("%.10lf\n", ans);
	}
	return 0;
}