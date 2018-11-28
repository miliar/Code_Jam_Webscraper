#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <set>

#define LL long long int
#define FOR(i, s, e) for (int i=(s); i<(e); i++)
#define FOE(i, s, e) for (int i=(s); i<=(e); i++)
#define FOD(i, s, e) for (int i=(s)-1; i>=(e); i--)
#define CLR(x, a) memset(x, a, sizeof(x))

using namespace std;
#define N 30

int test, n, m, mxx[N], mxy[N], mnx[N], mny[N], b[N];
char s[N][N];

void fill(int x1, int y1, int x2, int y2) {
	int cnt = 0, p = -1;
	int in[30];
	
	FOR(i, 0, 26)
		if (x1 <= mnx[i] && y1 <= mny[i] && mxx[i] < x2 && mxy[i] < y2) {
			in[i] = 1;
			if (b[i]) {
				cnt++;
				p = i;
			}
		}
		else in[i] = 0;
	
	if (cnt == 1) {
		FOR(i, x1, x2) FOR(j, y1, y2) s[i][j] = 'A' + p;
	}
	else {
	
		int done = 0;
		FOR(i, x1 + 1, x2) {
			int cnt = 0, ca = 0, cb = 0;
			FOR(j, 0, 26) {
				if (!in[j]) continue; 
				if (b[j] && mnx[j] < i && i <= mxx[j]) cnt++;
				else if (b[j] && mxx[j] < i) ca++;
				else if (b[j] && mnx[j] >= i) cb++; 
			}
			if (cnt == 0 && ca >= 1 && cb >= 1) {
				fill(x1, y1, i, y2);
				fill(i, y1, x2, y2);
				done = 1;
				break;
			}
		}
		
		if (!done) {
			FOR(i, y1 + 1, y2) {
				int cnt = 0, ca = 0, cb = 0;
				FOR(j, 0, 26) {
					if (!in[j]) continue;
					if (b[j] && mny[j] < i && i <= mxy[j]) cnt++;
					else if (b[j] && mxy[j] < i) ca++;
					else if (b[j] && mny[j] >= i) cb++; 
				}
				if (cnt == 0 && ca >= 1 && cb >= 1) {
					fill(x1, y1, x2, i);
					fill(x1, i, x2, y2);
					break;
				}
			}
		}
	
	}
	
}

void solve(int test) {
	scanf("%d%d", &n, &m);
	CLR(b, 0);
	FOR(i, 0, n){
		scanf("%s", s[i]);
		//printf("%s\n", s[i]);
		FOR(j, 0, m)
			if ('A' <= s[i][j] && s[i][j] <= 'Z')
				b[s[i][j] - 'A'] = 1;
	}
	
	
	
	FOR(c, 0, 26) {
		if (!b[c]) continue;
		mnx[c] = mny[c] = 999;
		mxx[c] = mxy[c] = -1;
		FOR(i, 0, n)
		FOR(j, 0, m)
			if (s[i][j] == 'A' + c) {
				mnx[c] = min(mnx[c], i);
				mny[c] = min(mny[c], j);
				mxx[c] = max(mxx[c], i);
				mxy[c] = max(mxy[c], j);
			}
	}
	
	fill(0, 0, n, m);
	
	printf("Case #%d:\n", test);
	FOR(i, 0, n) printf("%s\n", s[i]); 
	
	 
}

int main(){
	scanf("%d", &test);
	FOR(i, 0, test) solve(i + 1);
	return 0;
}
