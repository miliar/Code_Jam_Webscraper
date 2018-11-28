#include <bits/stdc++.h>
#define maxn 210
using namespace std;

struct str { int v, nex; } edge[maxn * maxn];
int top, T, t_;
int n, m, e, ans;
int vis[maxn], nex[maxn], markl[maxn], markr[maxn], fst[maxn];
int x[maxn * maxn], y[maxn * maxn], X[maxn * maxn], Y[maxn * maxn];
char ch[maxn * maxn];
char s[maxn][maxn], S[maxn][maxn];

void make_edge(int a, int b) {
	edge[++e].nex = fst[a]; fst[a] = e; edge[e].v = b;
	edge[++e].nex = fst[b]; fst[b] = e; edge[e].v = a;
}

bool path(int u) {
	for (int i = fst[u]; i; i = edge[i].nex) {
		int v = edge[i].v;
		if (vis[v] || markr[v]) continue;
		vis[v] = 1;
		if (!nex[v] || (path(nex[v]))) {
			nex[v] = u;
			return true;
		}
	}
	return false;
}

void hungary() {
	memset(nex, 0, sizeof(nex));
	for (int i = 1; i <= 2 * n; i++) {
		if (markl[i]) continue;
		memset(vis,0,sizeof(vis));
		path(i);
	}	
	return;
}

int main() {
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	for (scanf("%d",&T); T; T--) {
		scanf("%d %d\n",&n,&m);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++)
				s[i][j] = S[i][j] = '.';
		for (int i = 1; i <= m; i++) {
			scanf("%c %d %d\n",&ch[i],&x[i],&y[i]);		
			s[x[i]][y[i]] = S[x[i]][y[i]] = ch[i];
		}	
		memset(markl,0,sizeof(markl));
		memset(markr,0,sizeof(markr));
		memset(fst,0,sizeof(fst)); e = 0;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++) {
				if (s[i][j] == '.' || s[i][j] == '+') make_edge(i, j);
				else markl[i] = markr[j] = 1;
			}
		hungary();
		for (int j = 1; j <= n; j++)
			if (nex[j]) {
				int i = nex[j];
				if (s[i][j] == '.') s[i][j] = 'x';
				else s[i][j] = 'o';
			}
		memset(markl,0,sizeof(markl));
		memset(markr,0,sizeof(markr));
		memset(fst,0,sizeof(fst)); e = 0;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++) {
				if (s[i][j] == '.' || s[i][j] == 'x') make_edge(i - j + n + 1, i + j);
				else markl[i - j + n + 1] = markr[i + j] = 1;
			}
		hungary();
		for (int j = 1; j <= 2 * n; j++)
			if (nex[j]) {
				int i = nex[j];
				int a = (i + j - n - 1) / 2;
				int b = (j - i + n + 1) / 2;
				if (s[a][b] == '.') s[a][b] = '+';
				else s[a][b] = 'o';
			}
		top = 0; ans = 0;
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++) {
				if (s[i][j] != S[i][j]) {
					X[++top] = i;
					Y[top] = j;
				}
				if (s[i][j] == '+' || s[i][j] == 'x') ans++;
				else if (s[i][j] == 'o') ans += 2;
			}
		printf("Case #%d: %d %d\n",++t_, ans, top);
		for (int i = 1; i <= top; i++) {
			printf("%c %d %d\n",s[X[i]][Y[i]], X[i], Y[i]);
		}
	}
	return 0;
}
