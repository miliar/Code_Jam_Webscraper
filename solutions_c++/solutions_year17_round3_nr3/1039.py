#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;
const double eps = 1e-9;

priority_queue <double> q;

void solve()
{
	int n, k;
	cin >> n >> k;
	double u;
	cin >> u;
	vector<double> v(n);

	while (!q.empty()) q.pop();
	
	for(int i = 0; i < n; i++) {
		cin >> v[i];
		q.push(-v[i]);
	}

	double res = 1;
	sort(v.begin(), v.end());
	double const delta = 0.0001;
	double go = 0;
	
	while(go + eps < u) {
		//q.top() -= delta;
		

		v[0] += delta;
		go += delta;
		int i = 1;
		while(i < n) {
			if (v[i - 1] - v[i] > eps) {
				swap(v[i], v[i-1]);

			} else break;
			i++;

		}
	}

	//while(!q.empty()) {
 //       res *= -(q.top());
 //       q.pop();
	//}

	for(int i = 0; i < n; i++) res *= v[i];
	printf("%.9f", res);

}


int main()
{
	freopen("small.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}

	return 0;
}
