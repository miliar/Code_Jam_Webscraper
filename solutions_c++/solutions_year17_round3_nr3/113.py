#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <string>
#include  <cstring>
#include <cstdlib>

using namespace std;

#define EPS 1e-9

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int test = 1; test<=t; test++) {
		int n, k;
		scanf("%d %d", &n, &k);
		double u;
		scanf("%lf", &u);
		vector<double> mch;
		for(int i = 0; i<n; i++) {
			double x;
			scanf("%lf", &x);
			mch.push_back(x);
		}
		mch.push_back(1);
		sort(mch.begin(), mch.end());
		for(int i = 0; i<n; i++) {
			//printf("-> %lf\n", mch[i]);
			if(u < EPS) continue;
			if(mch[i] + EPS < mch[i+1]) {
				double up = min(u, (mch[i+1]-mch[i])*(i+1));
				u -= up;
				up /= (i+1);
				for(int j = 0; j<=i; j++) {
					mch[j] += up;
				}
			}
		}
		double p = 1;
		for(int i = 0; i<n; i++) {
			p *= mch[i];
		}
		printf("Case #%d: %.7lf\n", test, p);
	}
	return 0;
}
