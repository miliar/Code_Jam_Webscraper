#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <queue>
#include <vector>
#include <functional>
#include <math.h>
#include <iomanip>

using namespace std;

const int maxn = 25;
int T, n;
double d;

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	cin>>T;
	for (int tt = 0; tt < T; tt++) {
		cin>>d>>n;
		double t = 0;
		for (int i = 0; i < n; i++) {
			double k, s;
			cin>>k>>s;
			t = max(t, (d-k)/s);
		}
		cout<<"Case #"<<tt+1<<": "<<setprecision(8)<<d/t<<endl;
	}
	return 0;
}