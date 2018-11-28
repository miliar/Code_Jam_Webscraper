#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;
typedef long long ll;

const int MAX_N = 2;
int n[2];
int a[2][MAX_N][2];

int solve() {
	scanf("%d%d", &n[0], &n[1]);

	for (int i=0; i<2; i++) {
		for (int j=0; j<n[i]; j++) {
			scanf("%d%d", &a[i][j][0], &a[i][j][1]);
		}
	}

	if (n[0]+n[1]==1) return 2;

	if (n[0]==2 || n[1]==2) {
		int person;
		if (n[0]==2) person = 0; else person = 1;
		int plan[2];
		plan[0] = a[person][1][1] - a[person][0][0];
		if (plan[0] < 0) plan[0] += 1440;
		plan[1] = a[person][0][1] - a[person][1][0];
		if (plan[1] < 0) plan[1] += 1440;
		if (plan[0] <= 720 || plan[1] <= 720) return 2;
		else return 4;
	}

	return 2;
}

int main() {
	int t;
	scanf("%d\n", &t);

	for (int i=1; i<=t; i++) {
		printf("Case #%d: %d\n", i, solve());
	}
}
