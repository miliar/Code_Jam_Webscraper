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

char s[30], *p;

int main() {
	int t, cn = 1; sc(t);
	while (t--) {
		scs(s);
		
		p = s+1;
		while (p[0] != 0) {
			if ((p != s) && (*(p-1)) > (*p)) {
				p--;
				p[0]--;
				
				char *q = p+1;
				while (*q) {
					q[0] = '9';
					q++;
				}
			} else p++;
		}
		
		printf("Case #%d: ", cn++);
		p = s;
		while (p[0] == '0') p++;
		if (p[0] == 0) p--;
		puts(p);
	}
	return 0;
}




































