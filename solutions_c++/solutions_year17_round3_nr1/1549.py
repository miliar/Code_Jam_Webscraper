#include<stdio.h>
#include<algorithm>
using namespace std;
struct data {
	long long int x, y;
	inline bool operator<(const data &temp)const {
		return x > temp.x || (x==temp.x && y > temp.y);
	}
}b[2000];
long long int map[2000][2000];
long double pi = 3.14159265358979;
int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n,t,i,j,k,m;
	scanf("%d", &t);
	for (i = 1; i <= t; i++) {
		scanf("%d %d", &n, &m);
		for(j=1;j<=n;j++) scanf("%d %d", &b[j].x, &b[j].y);
		for (j = 1; j <= n; j++) {
			for (k = 0; k <= m; k++) map[j][k] = 0;
		}
		sort(b + 1, b + n + 1);
		for (j = 1; j <= n; j++) {
			for (k = 0; k < m; k++) {
				if (j == k) break;
				map[j][k + 1] = map[j - 1][k + 1];
				if (k == 0 && map[j][k + 1] < b[j].x*b[j].x + b[j].y * 2 * b[j].x) { map[j][k + 1] = b[j].x*b[j].x + b[j].y * 2 * b[j].x; continue; }
				if ((map[j - 1][k] + b[j].y * 2 * b[j].x) > map[j][k + 1]) map[j][k + 1] = map[j - 1][k] + b[j].y * 2 * b[j].x;
			}
		}
		printf("Case #%d: %.9llf\n",i, (long double)(map[n][m]) * pi);
	}
	return 0;
}