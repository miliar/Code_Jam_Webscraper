#include <bits/stdc++.h>
using namespace std;

const int maxN = 1e3+100;

int n, k;
int d[maxN], v[maxN];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for(int dem = 1; dem <= test; dem++) {
		cin >> n >> k;
		for(int i=0; i<k; i++)
			scanf("%d %d", &d[i], &v[i]);
		double time = 0;
		for(int i=k-1; i>=0; i--) 
			time = max(time, (n-d[i]) / (v[i]*1.0));
		printf("Case #%d: %.9lf\n", dem, n/time);
	}
	fclose(stdin);
	fclose(stdout);
}