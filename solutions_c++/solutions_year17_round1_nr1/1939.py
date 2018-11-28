#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#define PB push_back
#define MP make_pair
#define X first
#define Y second
#define lc (k<<1)
#define rc ((k<<1)|1)
#define mi ((l+r)>>1)
#define fk puts("fuck!")
using namespace std;
typedef long long ll;
typedef unsigned long long ull;

char s[33][33];
int vis[33][33], R, C;

void work(int x, int y) {
	char now = s[x][y];
	int l = y, r = y;
	while(l-1>0 && !vis[x][l-1] && s[x][l-1]=='?')
		--l, s[x][l] = now, vis[x][l] = 1;
	while(r+1<=C&& !vis[x][r+1] && s[x][r+1]=='?')
		++r, s[x][r] = now, vis[x][r] = 1;
	
	int up = x, dn = x;
	while(up - 1 > 0) {
		int flag = 1;
		for(int i=l; i<=r; ++i)
			if(vis[up-1][i] || s[up-1][i]!='?') {
				flag = 0;
				break;
			}
		if(flag) {
			--up;
			for(int i=l; i<=r; ++i)
				s[up][i] = now, vis[up][i] = 1;
		} else break;
	}
	while(dn + 1 <= R) {
		int flag = 1;
		for(int i=l; i<=r; ++i)
			if(vis[dn+1][i] || s[dn+1][i]!='?') {
				flag = 0;
				break;
			}
		if(flag) {
			++dn;
			for(int i=l; i<=r; ++i)
				s[dn][i] = now, vis[dn][i] = 1;
		} else break;
	}
}

int main()
{
	int T; scanf("%d", &T);
	for(int cas=1; cas<=T; ++cas) {
		memset(vis, 0, sizeof vis);
		scanf("%d%d", &R, &C);
		for(int i=1; i<=R; ++i)
			scanf("%s", s[i]+1);
		for(int i=1; i<=R; ++i)
			for(int j=1; j<=C; ++j)
				if(!vis[i][j] && s[i][j]!='?') work(i,j);
		printf("Case #%d:\n", cas);
		for(int i=1; i<=R; ++i) {
			for(int j=1; j<=C; ++j)
				printf("%c",s[i][j]);
			puts("");
		}
	}
	return 0;
}





