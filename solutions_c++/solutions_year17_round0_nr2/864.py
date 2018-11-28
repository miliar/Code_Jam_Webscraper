#include <bits/stdc++.h>

#define maxn 200100
#define sq 333
#define logn 23
#define inf 0x3F3F3F3F
#define linf 0x3F3F3F3F3F3F3F3FLL
#define eps 1e-9
#define pb push_back
#define mp make_pair
#define mod 1000000007LL

using namespace std;

typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vii;
typedef priority_queue<pii, vii, greater<pii> > pq;

#ifdef ONLINE_JUDGE
#define debug(args...)
#else
#define debug(args...) fprintf(stderr,args)
#endif

int t, n;
char s[30];
int pd[30][10][2];
bool vis[30][10][2];
bool zero;

int f(int pos, int last, bool menor) {
	if(pos == n) {
		return 9;
	}
	int &p = pd[pos][last][menor];
	if(!vis[pos][last][menor]) {
		vis[pos][last][menor] = true;
		int ult = s[pos]-'0';
		if(menor) ult = 9;
		for(int i = ult; i >= last; --i) {
			if(f(pos+1, i, menor||(i < (s[pos]-'0'))) != -1) {
				p = i;
				break;
			}
		}
	}
	return p;
}

void rec(int pos, int last, bool menor) {
	if(pos == n) return;
	int &p = pd[pos][last][menor];
	if(p == 0) {
		if(!zero) printf("0");
	} else {
		zero = false;
		printf("%d", p);
	}
	rec(pos+1, p, menor||(p < (s[pos]-'0')));
}

int main() {
	scanf("%d", &t);
	for(int cas = 1; cas <= t; ++cas) {
		zero = true;
		scanf("%s", s);
		n = strlen(s);
		memset(pd, -1, sizeof pd);
		memset(vis, false, sizeof vis);
		printf("Case #%d: ", cas);
		f(0, 0, false);
		rec(0, 0, false);
		printf("\n");
	}

	return 0;
}