#include <stdio.h>
#include <bits/stdc++.h>			

#define pb push_back
#define pp pop_back
#define sz(a) (int)(a.size())
#define mp make_pair
#define F first
#define S second
#define next _next
#define prev _prev
#define left _left
#define right _right
#define y1 _y1
#define all(x) x.begin(), x.end()

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int N = (int)1e6 + 123;
const ll INF = (ll)1e18 + 123;
const int inf = (int)1e9 + 123;
const int MOD = (int)1e9 + 7;

void megaRandom() {
	unsigned int FOR;
 	asm("rdtsc" : "=A"(FOR));
  	srand(FOR);
}

int n, a[10];
bool was[1111];
char s[1111];
pii b[5];

void solve(int test) {
	cin >> n;
	for(int i = 1; i <= 6; i ++) // R O Y G B V
		cin >> a[i];
	b[1] = mp(a[1], 'R');
	b[2] = mp(a[3], 'Y');
	b[3] = mp(a[5], 'B');
	memset(was, 0, sizeof was);
	sort(b + 1, b + 3 + 1);
	int p = 1, j = 3;
	int n1 = n;
	while(n1 --) {
		if(was[p]) break;
		while(j >= 1 && !b[j].F)
			j --;
		//cout << "p: " << p << " ch: " << char(b[j].S) << "\n";
		s[p] = b[j].S;
		b[j].F --;	
		was[p] = 1;
		p += 2;
		if(p > n) p -= n;		
	}
	p ++;
	n1 ++;
	while(n1 --) {
		if(was[p]) break;
		while(j >= 1 && !b[j].F)
			j --;
		//cout << "p: " << p << " ch: " << char(b[j].S) << "\n";
		s[p] = b[j].S;
		b[j].F --;	
		was[p] = 1;
		p += 2;
		if(p > n) p -= n;		
	}
	s[n + 1] = s[1];
	bool ok = 1;
	for(int i = 2; i <= n; i ++)
		if(s[i - 1] == s[i] || s[i] == s[i + 1])
			ok = 0;	
	if(!ok) cout << "Case #" << test << ": IMPOSSIBLE\n";
	else {
		cout << "Case #" << test << ": ";
		for(int i = 1; i <= n; i ++)
			cout << s[i];
		cout << "\n";
	}
}

int main() {
	freopen(".in", "r", stdin);
	freopen(".out", "w", stdout);
	megaRandom();
	int t;
	cin >> t;
	for(int it = 1; it <= t; it ++)
		solve(it);
	return 0;
}
