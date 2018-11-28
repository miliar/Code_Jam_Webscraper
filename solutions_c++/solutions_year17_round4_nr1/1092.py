#include <bits/stdc++.h>
using namespace std;

const int maxN = 1e2+100;

int a[5];
int f[102][102][102];
int n, p;

int dq(int x1, int x2, int x3) {
	if (x1 + x2 + x3 == 0) 
		return 0;
	int du;
	int res = 0;
	if (f[x1][x2][x3] >= 0) 
		return f[x1][x2][x3];
	if (x1 > 0) {
		du = (x1-1 + x2*2 + x3*3) % p;
		if (du == 0)
			res = max(res, dq(x1-1, x2, x3)+1);
		else 
			res = max(res, dq(x1-1, x2, x3));
	}
	if (x2 > 0) {
		du = (x1 + (x2-1)*2 + x3*3) % p;
		if (du == 0)
			res = max(res, dq(x1, x2-1, x3)+1);
		else 
			res = max(res, dq(x1, x2-1, x3));
	}
	if (x3 > 0) {
		du = (x1 + x2*2 + (x3-1)*3) % p;
		if (du == 0)
			res = max(res, dq(x1, x2, x3-1)+1);
		else 
			res = max(res, dq(x1, x2, x3-1));
	}
	f[x1][x2][x3] = res;
	// printf("%i %i %i %i\n", x1, x2, x3, f[x1][x2][x3]);
	return res;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for(int dem = 1; dem <= test; dem++) {
		memset(a, 0, sizeof(a));
		printf("Case #%d: ", dem);
		cin >> n >> p;
		for(int i=0; i<n; i++) {
			int x;
			cin >> x;
			++a[x%p];
		}
		memset(f, 255, sizeof(f));
		f[0][0][0] = 0;
		printf("%d\n", (dq(a[1], a[2], a[3])) + a[0]);
	}		
	fclose(stdin);
	fclose(stdout);
}