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

#define N 1009

int n, k;
bool b[N];
char s[N];

int proc() {
	int r = 0;
	
	rp(i, n) if (!b[i]) {
		if (i+k > n) return -1;
		
		fr(j, i, i+k) b[j] = !b[j];
		r++;
	}
	
	return r;
}

int main() {
	int t, cn = 1; sc(t);
	while (t--) {
		scs(s);
		n = strlen(s);
		rp(i, n) b[i] = (s[i] == '+');
		sc(k);
		
		printf("Case #%d: ", cn++);
		
		int ans = proc();
		if (ans == -1) puts("IMPOSSIBLE");
		else pri(ans);
	}
	return 0;
}




































