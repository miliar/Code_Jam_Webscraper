#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <functional>
#include <math.h>
#include <iomanip>
#include <utility>

using namespace std;

vector<double> a;
int T, n, k;
double u;

int main() {

	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1-attempt0.out", "w", stdout);
	cin>>T;
	for (int tt = 0; tt < T; tt++) {
		cin>>n>>k;
		cin>>u;
		a.clear();
		for (int i = 0; i < n; i++) {
			double p;
			cin>>p;
			a.push_back(p);
		}
		sort(a.begin(), a.end());
		double ans = 1;
		if (n==k) {
			double p = u, q = 1;
			a.push_back(1);
			for (int i = 1; i <= n; i++)
				if (i*(a[i]-a[i-1])<=p) 
					p -= i*(a[i]-a[i-1]);
				else {
					q = a[i-1]+p/i;
					break;
				}
			for (double i : a)
				ans *= max(q, i);
		}
		cout<<"Case #"<<tt+1<<": "<<ans<<endl;
	}
	return 0;
}