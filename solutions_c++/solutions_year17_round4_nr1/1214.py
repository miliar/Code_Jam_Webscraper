#include <deque>
#include <vector>
#include <algorithm>
#include <iostream>

#include <map>
#include <set>

using namespace std;

int f[101][101][101];
int g[101][101][101];

int sum(int a1, int a2, int a3, int p) {
	if (((a1+a2*2+a3*3) % p) == 0)
		return 1;
	else
		return 0;
}

void init(int p) {
	memset(f, 0, sizeof(0));

	f[0][0][0] = 0;
	for (int i = 0; i <= 100; ++i)
		for (int j = 0; j <= 100; ++j) 
			for (int k = 0; k <= 100; ++k) {
				int g1 = INT_MIN;
				int g2 = INT_MIN;
				int g3 = INT_MIN;
				if (i > 0)
					g1 = f[i-1][j][k]+sum(i-1,j,k, p);
				if (j > 0)
					g2 = f[i][j-1][k]+sum(i,j-1,k, p);
				if (k > 0)
					g3 = f[i][j][k-1]+sum(i,j,k-1, p);

				if (i == 0 && j == 0 && k == 0) continue;

				f[i][j][k] = max(g1,max(g2,g3));
			};
};



int solve(int i0) {	
	vector<int> count(4);

	int n, p;
	cin >> n >> p;

	for (int i = 0; i < n; ++i) {
		int g;
		cin >> g;
		g = g % p;
		count[g]++;
	};

	if (p == 2) {
		return count[1]/2 + count[0] + count[1] % 2;
	}
	else if (p == 3) {
		return f[count[1]][count[2]][count[3]]+count[0];		
	}
	else {
		return g[count[1]][count[2]][count[3]]+count[0];			
	}


};

int main() {
	//freopen("A.in", "r", stdin);

	//freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out2", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);


	init(4);
	for (int i = 0; i<=100;++i)
		for (int j = 0; j <= 100; ++j)
			for (int k = 0; k <= 100; ++k)
				g[i][j][k] = f[i][j][k];

	init(3);


	int t;
	cin >> t;
	for (int i0=1; i0<=t; ++i0) {
		int ans = solve(i0);
		printf("Case #%d: %d\n", i0, ans);
	};

}