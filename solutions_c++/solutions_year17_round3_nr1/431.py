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

typedef pair<double, double> cake;
int T, n, k;
vector<cake> a;
double PI = 3.14159265;

bool check(cake& c1, cake& c2) {
	return c1.first*c1.second>c2.first*c2.second;
}

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin>>T;
	for (int tt = 0; tt < T; tt++) {
		cin>>n>>k;
		a.clear();
		for (int i = 0; i < n; i++) {
			double r, h;
			cin>>r>>h;
			a.push_back(make_pair(r, h));
		}
		sort(a.begin(), a.end(), check);
		double ans = 0;
		int j = 0; 
		for (int i = 0; i < k; i++) {
			ans += 2*a[i].first*a[i].second;
			if (a[i].first>a[j].first)
				j = i;
		}
		double sum = ans - 2*a[k-1].first*a[k-1].second;
		ans += a[j].first*a[j].first;
		for (int i = k; i < n; i++)
			if (a[i].first>a[j].first)
				ans = max(ans, sum+2*a[i].first*a[i].second+a[i].first*a[i].first);
		cout<<"Case #"<<tt+1<<": "<<setprecision(8)<<PI*ans<<endl;
	}
	return 0;
}