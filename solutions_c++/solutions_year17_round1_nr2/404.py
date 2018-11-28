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

#define N 59

int n, p, r[N], q[N][N];

int down(int i, int j) {
	int num = 10*q[i][j];
	int denom = 11*r[i];
	
	return (num+denom-1)/denom;
}

int proc() {
	int j[N];
	cl(j, 0);
	
	int ret = 0;
	
	while (1) {
		int s = 0;
		rp(i, n) {
			if (j[i] == p) return ret;
			int op = down(i, j[i]);
			//db(i _ op);
			s = max(s, op);
		}
		
		while (1) {
			bool ok = 1;
			rp(i, n) {
				ll qq = 10ll*q[i][j[i]];
				ll v = 9ll*ll(s)*ll(r[i]);
				//db(v _ qq);
				if (v > qq) {
					j[i]++;
					if (j[i] == p) return ret;
					int op = down(i, j[i]);
					s = max(s, op);
					ok = 0;
					break;
				}
			}
			if (ok) break;
		}
		
		ret++;
		rp(i, n) j[i]++;
	}
	
	return ret;
}

int main() {
	int t, cn = 1; sc(t);
	while (t--) {
		sc2(n, p);
		rp(i, n) sc(r[i]);
		rp(i, n) {
			rp(j, p) sc(q[i][j]);
			sort(q[i], q[i]+p);
		}
		
		printf("Case #%d: %d\n", cn++, proc());
	}
	return 0;
}




































