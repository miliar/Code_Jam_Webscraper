#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int main() {
	int t;
	cin>>t;
	for(int q=1;q<=t;q++) {
		int d, n, k, s;
		cin>>d>>n;
		double maxm = 0.0;
		for(int i=0;i<n;i++) {
			cin>>k>>s;
			double dis = (d-k)*1.0/s;
			maxm = max(dis, maxm);
		}

		printf("Case #%d: %lf\n", q, (d*1.0/maxm));
	}
	return 0;
}
