#include <bits/stdc++.h>

using namespace std;

#define fr(a,b,c) for(int (a) = (b); (a) < (c); ++(a))
#define rp(a,b) fr(a,0,b)
#define fre(a,b) for(int a = adj[b]; ~a; a = ant[a])
#define cl(a,b) memset((a), (b), sizeof(a))
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d%d", &a, &b)
#define sc3(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define scs(s) scanf("%s", s)
#define pri(x) printf("%d\n", x)

#define iter(a) __typeof((a).begin())
#define fore(a,b) for(iter(b) a = (b).begin(); a != (b).end(); ++a)

#define st first
#define nd second
#define mp make_pair
#define pb push_back

#define db(x) cerr << #x << " == " << x << endl
#define dbs(x) cerr << x << endl
#define _ << ", " <<

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector< vi > vii;

const int oo = 0x3f3f3f3f;

#define M 1009
#define N 1009
#define yn YN

int n, c, m, cnt[N][N], sb[N];
set<int> cs[N];
int sum[N], mv[N];

void muda(int i, int d) {
	//db(i _ d _ sum[i]);
	cs[sum[i]].erase(i);
	mv[i] += d;
	sum[i] += d;
	cs[sum[i]].insert(i);
}

int yn, yc, z;
int cur;

bool update() {
	//db(yn _ yc _ z _ cur);
	if (yn <= yc) return 0;
	
	int i = -1;
	fore(it, cs[yn]) {
		i = *it;
		if (i > 0 && sum[i-1] < yn) break;
		i = -1;
	}
	if (i == -1) return 0;
	//db(i _ sum[i] _ sum[i-1]);
	
	if (mv[i] == 0) {
		cur++;
		mv[i]++;
	}
	//puts("C");
	muda(i, -1);
	//puts("D");
	muda(i-1, 1);
	
	//puts("A");
	while (yn > 0 && cs[yn].empty()) {
		yn--;
		z = cur;
	}
	//puts("B");
	return 1;
}

int p[M], b[M];

int main() {
	int t, cn = 1; sc(t);
	while (t--) {
		//db(cn);
		sc3(n, c, m);
		cl(sum, 0); cl(sb, 0);
		cl(cnt, 0);
		rp(i, m) {
			sc2(p[i], b[i]);
			p[i]--;
			b[i]--;
			
			sum[p[i]]++;
			sb[b[i]]++;
			cnt[p[i]][b[i]]++;
		}
		
		rp(i, 1005) cs[i].clear();
		rp(i, n) cs[sum[i]].insert(i);
		yn = 1005;
		while (cs[yn].empty()) yn--;
		
		yc = *max_element(sb, sb+c);
		
		cl(mv, 0);
		z = cur = 0;
		while (update());
		
		printf("Case #%d: %d %d\n", cn++, max(yn, yc), z);
	}
	return 0;
}




































