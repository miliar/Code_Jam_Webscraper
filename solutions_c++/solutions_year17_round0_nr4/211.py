#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for (int i = (a); i < (b); i++)
#define N 234

int tc;
char ty, gr[N][N], ngr[N][N];
int n, m, r, c;
int ans, ur[N], uc[N], ud1[N], ud2[N];
typedef tuple<char,int,int> aty;
vector<aty> anss;
void gg(int y, int x) {
	if (y >= n || x >= n) return;
	if (!ud1[y+x] && !ud2[y-x+n-1]) {
		ud1[y+x] = 1;
		ud2[y-x+n-1] = 1;
		if (ngr[y][x] == 'x') ngr[y][x] = 'o';
		else ngr[y][x] = '+';
	}
}
int main() {
	scanf("%d", &tc);
	fo(_,1,tc+1) {
		printf("Case #%d: ", _);
		scanf("%d %d", &n, &m);
		fo(i,0,m) {
			scanf(" %c %d %d", &ty, &r, &c); r--; c--;
			gr[r][c] = ngr[r][c] = ty;
			if (ty=='x' || ty=='o') ur[r] = uc[c] = 1;
			if (ty=='+' || ty=='o') ud1[r+c] = ud2[r-c+n-1] = 1;
		}
		fo(i,0,n) fo(j,0,n) if (!ur[i] && !uc[j]) {
			ur[i] = 1; uc[j] = 1;
			if (ngr[i][j] == '+') ngr[i][j] = 'o';
			else ngr[i][j] = 'x';
		}
		fo(i,0,2*n-1) fo(j,0,i+1) {
			gg(j, i-j);
			gg(i-j, j);
		}
		fo(i,0,n) fo(j,0,n) {
			if (ngr[i][j] == 'o') ans += 2;
			else if (ngr[i][j]) ans++;
			if (ngr[i][j] != gr[i][j]) anss.push_back(aty(ngr[i][j], i+1, j+1));
		}
		printf("%d %d\n", ans, anss.size());
		fo(i,0,anss.size()) {
			char ch; int y, x;
			tie(ch, y, x) = anss[i];
			printf("%c %d %d\n", ch, y, x);
		}

		ans = 0;
		fo(i,0,2*n) ur[i] = uc[i] = ud1[i] = ud2[i] = 0;
		fo(i,0,n) fo(j,0,n) gr[i][j] = ngr[i][j] = 0;
		anss.clear();
	}

	return 0;
}