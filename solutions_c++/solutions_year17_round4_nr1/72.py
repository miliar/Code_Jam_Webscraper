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

#define N 109

int n, p, cnt[N];

int main() {
	int t, cn = 1; sc(t);
	while (t--) {
		sc2(n, p);
		
		cl(cnt, 0);
		rp(i, n) {
			int g; sc(g);
			cnt[g%p]++;
		}
		
		int ans = cnt[0];
		if (p == 2) {
			printf("Case #%d: %d\n", cn++, ans + (cnt[1]+1)/2);
		} else if (p == 3) {
			while (cnt[1] > 0 && cnt[2] > 0) {
				cnt[1]--; cnt[2]--;
				ans++;
			}
			
			int m = 0;
			while (cnt[1] > 0) {
				cnt[1]--;
				if (m == 0) ans++;
				m = (m+1)%p;
			}
			while (cnt[2] > 0) {
				cnt[2]--;
				if (m == 0) ans++;
				m = (m+2)%p;
			}
			printf("Case #%d: %d\n", cn++, ans);
		} else {
			while (cnt[1] > 0 && cnt[3] > 0) {
				cnt[1]--; cnt[3]--;
				ans++;
			}
			
			int m = 0;
			while (cnt[2] > 0) {
				cnt[2]--;
				if (m == 0) ans++;
				m = (m+2)%p;
			}
			while (cnt[1] > 0) {
				cnt[1]--;
				if (m == 0) ans++;
				m = (m+1)%p;
			}
			while (cnt[3] > 0) {
				cnt[3]--;
				if (m == 0) ans++;
				m = (m+3)%p;
			}
			
			printf("Case #%d: %d\n", cn++, ans);
		}
	}
	return 0;
}




































