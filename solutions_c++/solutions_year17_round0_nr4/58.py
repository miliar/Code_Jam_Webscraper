#include <bits/stdc++.h>
using namespace std;

#define LL 					long long
#define ULL 				unsigned long long
#define pii 				pair<int,int>
#define fi 					first
#define se 					second
#define mp 					make_pair
#define vi 					vector<int>
#define psb 				push_back
#define ppb 				pop_back
#define all(x)			 	(x).begin(),(x).end()
#define sz 					size()
#define endln 				printf("\n")
#define gc					getchar_unlocked
#define pipi				pair < int, pii >
#define setmin(x)			memset((x), -1, sizeof((x)))
#define setnul(x)			memset((x), 0, sizeof((x)))
#ifndef getchar_unlocked
#define getchar_unlocked 	getchar
#endif
const int inf = (1<<30)-1+(1<<30);
const int mod = 1e9 + 7;

void gi( int &ret ) {
	ret = 0; char inp=gc(); int kl=1;
	while (inp<'0' || inp>'9') {if (inp=='-') kl=-1; inp=gc();}
	while ('0'<=inp && inp<='9') ret=(ret<<3)+(ret<<1)+(int)(inp-'0'), inp=gc();
	if (kl<1) ret=-ret;
}

const int maxn = 105;
int n, m, tot, aw[maxn][maxn], vis[maxn][maxn];
bool da[maxn<<1], db[maxn<<1], r[maxn], c[maxn], pa[maxn][maxn], pb[maxn][maxn];

vector < pipi > ans;
/* + -> 0, x -> 1, o ->2 */
int valid(int y, int x) {
	if (y<1 || y>n) return 0;
	if (x<1 || x>n) return 0;
	return 1;
}
int dir1[4] = {-1,1,0,0};
int dir2[4] = {0,0,-1,1};
void solve() {
	ans.clear();
	for (int i=1; i<=n; i++)
		for (int j=1; j<=n; j++) 
			if (r[i]==0 && c[j]==0) {
				r[i] = c[j] = 1;
				pa[i][j] = 1;
			}
	setnul(vis);
	queue < pii > q;
	q.push(mp(1,1)); q.push(mp(n,n));
	while (!q.empty()) {	
		int i = q.front().fi, j = q.front().se; q.pop();
		int a = i+j, b = (i-j)+n;
		if (da[a]==0 && db[b]==0) {
			da[a] = db[b] = 1;
			pb[i][j] = 1;
		}
		for (int ar=0; ar<4; ar++) {
			int nexy = i+dir1[ar], nexx = j+dir2[ar];
			if (valid(nexy,nexx) && !vis[nexy][nexx]) {
				vis[nexy][nexx] = 1;
				q.push(mp(nexy,nexx));
			}
		}
	}
	for (int i=1; i<=n; i++)
		for (int j=1; j<=n; j++) {
			int id = -1;
			if (pa[i][j] && pb[i][j]) id = 2;
			else if (pa[i][j]) id = 1;
			else if (pb[i][j]) id = 0;
			if (id>=0) tot++;
			if (id==2) tot++;
			if (aw[i][j]==id) continue;
			ans.psb(mp(id, mp(i,j)));
		}
	return;
}

int main() {
	int tc; gi(tc);
	for(int cs=1; cs<=tc; cs++) {
		setnul(da); setnul(db); setnul(r); setnul(c);
		setnul(pa); setnul(pb); setmin(aw);
		gi(n); gi(m);
		tot = 0;
		while(m--) {
			char inp[5]; int y,x;
			scanf("%s %d %d", inp, &y, &x);
			if (inp[0]=='+') aw[y][x] = 0;
			else if (inp[0]=='x') aw[y][x] = 1;
			else aw[y][x] = 2;
			if (inp[0]=='x' || inp[0]=='o') {
				pa[y][x] = 1;
				r[y] = c[x] = 1;
			}
			if (inp[0]=='+' || inp[0]=='o') {
				pb[y][x] = 1;
				int a = y+x, b = (y-x)+n;
				da[a] = db[b] = 1;
			}
		}
		solve();
		printf ("Case #%d: %d %d\n", cs, tot, (int)ans.sz);
		for (auto pr : ans) {
			if (pr.fi==0) printf ("+ ");
			else if (pr.fi==1) printf ("x ");
			else printf ("o ");
			printf ("%d %d\n", pr.se.fi, pr.se.se);
		}
	}
	return 0;
}


