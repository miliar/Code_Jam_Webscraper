#pragma GCC target("sse4.1")
#pragma GCC optimize("O3")
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back

mt19937 rnd;

template<class T> inline void opt (T &a, T b) {
	a = max (a, b);
}

inline int rndInt (int x) {
	return rnd () % x;            
}

inline int R (int l, int r) {
	return l + rndInt (r - l + 1);
}

char Cur;

inline char getChar () {
	char t = Cur;
	Cur = getchar ();
	return t;
}

template<class telem> void readInt (telem &a) {
	a = 0;
	while (!isdigit (Cur)) getChar ();
	while (isdigit (Cur)) {
		a *= 10;
		a += getChar () - '0';
	}
}

typedef long double dbl;

int T = 1;


void pre () {

} 

int n;
long double D;
int pos[1111];
long double s[1111];

void load () {
	cin >> D >> n;
	for (int i = 0; i < n; i++)
		cin >> pos[i] >> s[i];
}


bool check (dbl v) {
	for (int i = 0; i < n; i++) {
		if (v - 1e-9 < s[i])
			continue;
		dbl t = pos[i];
		t /= (v - s[i]);
		dbl d = t * v;
		if (d < D)
			return false; 
	}
	return true;
}


void solve (int tc) {
	cout << "Case #" << tc << ": ";
	dbl l = 0;
	dbl r = 1e30;
	for (int i = 0; i < 333; i++) {
		dbl m = l + r;
		m *= 0.5;
		if (check (m))
			l = m;
		else
			r = m;
	}
	l += r;
	l *= 0.5;
	long double ans = l;
	cout.precision (20);
	cout << fixed << showpoint;
	cout << ans << '\n';
}
	

int main () {
	ios_base::sync_with_stdio (false);
	cin.tie (0);
	pre ();
#ifdef LOCAL
	auto ___ = freopen ("file.in", "r", stdin);
	___ = freopen ("file.out", "w", stdout);
	assert (___);
#endif

	double st = clock ();

	cin >> T;
	int tc = 0;

	while (T --> 0) {
		tc++;	
		load ();  
		solve (tc);
	}

	clog << (clock () - st) / CLOCKS_PER_SEC << endl;

	return 0;
}