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
int cnt[6];
char t[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};

void load () {
	cin >> n;
	for (int i = 0; i < 6; i++)
		cin >> cnt[i];
}

char ans[1111];

bool gen (int pos = 0, char last = -1) {
	ans[pos] = '\0';
	//clog << pos << ' ' << last << ' ' << ans << endl;
	if (pos == n) {
		return ans[0] != ans[n - 1];
	}
	int ct = 0;
	int p = -1;
	for (int i = 0; i < 6; i++) {
		if (last == t[i])
			continue;
		if (ct < cnt[i] || (cnt[i] == ct && pos > 0 && ans[pos] == t[i])) {
			ct = cnt[i];
			p = i;		
		}
	}
	if (ct == 0)
		return false;
	cnt[p]--;
	ans[pos] = t[p];
	if (gen (pos + 1, t[p]))
		return true;
	cnt[p]++;
	int np = p;
	ct = 0;
	for (int i = 0; i < 6; i++) {
		if (last == t[i] || p == np)
			continue;
		if (ct < cnt[i] || (cnt[i] == ct && pos > 0 && ans[pos] == t[i])) {
			ct = cnt[i];
			p = i;		
		}		
	}
	if (ct == 0)
		return false;
	cnt[p]--;
	ans[pos] = t[p];
	if (gen (pos + 1, t[p]))
		return true;
	cnt[p]++;
	return false;
}

void solve (int tc) {
	cout << "Case #" << tc << ": ";
	ans[n] = '\n';
	for (int i = 0; i < 6; i++) {
		if (cnt[i] == 0)
			continue;
		ans[0] = t[i];
		cnt[i]--;
		if (gen (1, ans[0])) {
			cout << ans << '\n';
			return;
		}
		cnt[i]++;
	}
	cout << "IMPOSSIBLE\n";
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