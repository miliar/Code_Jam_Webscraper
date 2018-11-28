#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#ifdef _DEBUG_
	#define debug(...) printf(__VA_ARGS__)
#else
	#define debug(...) (void)0
#endif
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

// g: b+y
// v: r+b
// o: r+y

typedef pair<int, char> PIC;
vector<char> raw;
void small(PIC a, PIC b, PIC c) {
	raw.clear();
	if(a.F<b.F)
		swap(a, b);
	if(a.F<c.F)
		swap(a, c);
	if(b.F<c.F)
		swap(b, c);
	while(a.F > b.F) {
		raw.PB(a.S);
		raw.PB(c.S);
		a.F--, c.F--;
	}
	while(a.F > c.F) {
		raw.PB(a.S);
		raw.PB(b.S);
		a.F--, b.F--;
	}
	while(a.F--) {
		raw.PB(a.S);
		raw.PB(b.S);
		raw.PB(c.S);
	}
}

bool jud(int a, int b, int c) {
	if(a<b)
		swap(a, b);
	if(a<c)
		swap(a, c);
	return a<=b+c;
}

int main() {
	int t;
	scanf("%d", &t);
	for(int kase=1; kase<=t; kase++) {
		printf("Case #%d: ", kase);
		int n;
		int r, o, y, g, b, v;
		scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
		if(!jud(r, y, b)) {
			puts("IMPOSSIBLE");
			continue;
		} else {
			small(MP(r,'R'), MP(y, 'Y'), MP(b, 'B'));
			assert(n==SZ(raw));
			for(char c : raw)
				putchar(c);
			putchar('\n');
		}
	}
	return 0;
}
