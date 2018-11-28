#include <bits/stdc++.h>
using namespace std;
struct pk_t {
	double r;
	double h;
};

bool cmp (pk_t x, pk_t y) {
	return x.r * x.h > y.r * y.h;
}

double pi = acos(-1.0);

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int casen;
	cin>>casen;
	for (int casex=1; casex<=casen; casex++) {
		int n, k;
		cin>>n>>k;
		pk_t pk[1024];
		for (int i=0; i<n; i++) {
			cin>>pk[i].r>>pk[i].h;
		}
		sort(pk, pk+n, cmp);
		double maxarea = 0;
		for (int i=0; i<k; i++) {
			double area = 2 * pi * pk[i].r * pk[i].h;
			double maxbase = pi * pk[i].r * pk[i].r;
			for (int j=0; j<k; j++) {
				if (j != i) {
					area += 2 * pi * pk[j].r * pk[j].h;
					maxbase = max(maxbase, pi * pk[j].r * pk[j].r);
				}
			}
			area += maxbase;
			if (area > maxarea)
				maxarea = area;
		}
		for (int i=k; i<n; i++) {
			double area = 2 * pi * pk[i].r * pk[i].h;
			double maxbase = pi * pk[i].r * pk[i].r;
			for (int j=0; j<k-1; j++) {
				if (j != i) {
					area += 2 * pi*pk[j].r * pk[j].h;
					maxbase = max(maxbase, pi * pk[j].r * pk[j].r);
				}
			}
			area += maxbase;
			if (area > maxarea)
				maxarea = area;
		}
		cout<<"Case #"<<casex<<": ";
		printf("%.6f\n", maxarea);
	}
	return 0;
}
