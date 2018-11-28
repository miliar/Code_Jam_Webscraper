#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for(int i=(a);i<(b);i++)
#define MOD 1000000007
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef long double ld;
#define PI ((ld)acos(-1.))
#define asdf(x...) fprintf(stderr, x)

int T, N, M, C;
vector<int> v[1100];

namespace MF {
	const int N = 2200, M = 1100100;
	int f[N], e[2*M], c[2*M], fl[2*M], nxt[2*M], ce;
	int n, s, t;
	int Q[N], lvl[N];
	int le[N];

	void init(int _n) {
		n = _n+2; s = _n; t = _n+1; ce = 0;
		fo(i,0,n) f[i]=-1;
	}

	void add(int a, int b, int cap) {
		nxt[ce]=f[a]; f[a]=ce; e[ce]=b; fl[ce]=0; c[ce]=cap; ce++;
		nxt[ce]=f[b]; f[b]=ce; e[ce]=a; fl[ce]=0; c[ce]=0; ce++;
	}

	bool bfs() {
		fo(i,0,n) lvl[i]=-1;
		int qi = 1;
		Q[0] = s; lvl[s] = 0;
		fo(i,0,qi) {
			int x=Q[i];
			le[x]=f[x];
			for (int j=f[x];j>=0;j=nxt[j]) if (c[j]-fl[j]>0) {
				int y=e[j];
				if (lvl[y]==-1) {
					lvl[y]=lvl[x]+1;
					Q[qi++]=y;
				}
			}
		}
		return lvl[t]!=-1;
	}

	int aug(int cu, int cf) {
		if (cu == t) return cf;
		for (int &i=le[cu];i>=0;i=nxt[i]) if (c[i]-fl[i]>0) {
			int x=e[i];
			if (lvl[x]!=lvl[cu]+1) continue;
			int rf = aug(x,min(cf,c[i]-fl[i]));
			if (rf>0) {
				fl[i]+=rf;
				fl[i^1]-=rf;
				assert(fl[i] == -fl[i^1]);
				return rf;
			}
		}
		lvl[cu]=-1;
		return 0;
	}

	int mf() {
		int tot = 0;
		while (bfs())
			for (int x=aug(s,1e9);x;x=aug(s,1e9)) tot+=x;
		return tot;
	}
}


int main () {
	scanf("%d", &T);
	fo(t, 1, T+1) {
		//REMEMBER CLEAR DS
		fo(i, 0, 1100) v[i].clear();
		//REMEMBER CLEAR DS
		asdf("Doing case %d... ", t);
		scanf("%d %d %d", &N, &C, &M);
		assert(C==2);
		fo(i, 0, M) {
			int x, y; scanf("%d %d", &x, &y);
			v[y-1].PB(x-1);
		}
		fo(i, 0, N) sort(v[i].begin(), v[i].end());

		int ans = 0, fix = 0;
		int X = (int) v[0].size();
		int Y = (int) v[1].size();

		vector<pair<int, int>> e;
		MF::init(X+Y);
		fo(i, 0, X) fo(j, 0, Y) if (v[0][i] != v[1][j]) {
			MF::add(i, j+X, 1);
			e.PB(MP(i, j));
		}
		fo(i, 0, X) MF::add(MF::s, i, 1);
		fo(i, 0, Y) MF::add(X+i, MF::t, 1);

		MF::mf();
		set<int> sa, sb;
		vector<int> a, b;
		fo(i, 0, (int) e.size()) {
			if (MF::fl[i*2]) {
				ans++;
				sa.insert(e[i].first);
				sb.insert(e[i].second);
			}
		}

		fo(i, 0, X) if (!sa.count(i)) a.PB(v[0][i]);
		fo(i, 0, Y) if (!sb.count(i)) b.PB(v[1][i]);

		if (a.size() || b.size()) {
			int col = a.size() ? a[0] : b[0];

			if (a.size() && b.size()) {
				asdf("%d %d\n", (int) a.size(), (int) b.size());
				for (int i : a) assert(i == col);
				for (int i : b) assert(i == col);
				if (col == 0) {
					ans += (int) (a.size() + b.size());
					fix = 0;
				} else {
					ans += (int) max(a.size(), b.size());
					fix = (int) min(a.size(), b.size());
				}
			} else {
				//if it's only one, need to use all of them anyway
				ans += (int) (a.size() + b.size());
				fix = 0;
			}
		}

		printf("Case #%d: %d %d\n", t, ans, fix);
		asdf("%d %d\n", ans, fix);
	}
	return 0;
}
