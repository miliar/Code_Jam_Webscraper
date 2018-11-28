#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int casen;
	cin>>casen;
	for (int casex=1; casex<=casen; casex++) {
		int n, k;
		cin>>n>>k;
		double u;
		cin>>u;
		double p[100];
		for (int i=0; i<n; i++) {
			cin>>p[i];
		}
		sort(p, p+n);
		while (u > 1e-8) {
			int same = 1;
			for (int i=0; i<n-1; i++) {
				if (abs(p[i+1] - p[i]) < 1e-8) {
					same++;
				}
				else
					break;
			}
			double diff = same == n ? 1 - p[0] : p[same] - p[0];
			if (diff * same <= u) {
				for (int i=0; i<same; i++)
					p[i] += diff;
				u -= diff * same;
			}
			else {
				for (int i=0; i<same; i++)
					p[i] += (u / same);
				u = 0;
			}
		}
		double pr = 1;
		for (int i=0; i<n; i++) {
			pr *= p[i];
		}
		cout<<"Case #"<<casex<<": ";
		printf("%.6f\n", pr);
	}
	return 0;
}
