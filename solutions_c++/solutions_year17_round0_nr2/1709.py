#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back

mt19937 rnd;

inline int rndInt (int x) {
	return rnd () % x;
}

/*inline int R (int l, int r) {
	return l + rndInt (r - l + 1);
}*/

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

int T = 1;
string s;
int n;
char dp[20][10][2];
ll ten[19];
int tc;       

void pre () {
	ten[0] = 1;
	for (int i = 1; i < 19; i++)
		ten[i] = ten[i - 1] * 10;
}

void load () {
	cin >> s;
	n = (int) s.size ();
}

char get (int pos, int last, int l) { 
	auto &res = dp[pos][last][l];
	if (res != -1)
		return res;
	if (pos == n)
		return res = 1;
	res = 0;
	int up = s[pos] - '0';
	if (l) up = 9;
	for (int i = last; i <= up; i++) {
		res = max (res, get (pos + 1, i, l | (i + '0' < s[pos]))); 	
	}
	return res;
}



void solve () {
	tc++;
	cout << "Case #" << tc << ": ";
	for (int i = 0; i <= n; i++) {
		for (int j = 0; j < 10; j++) {
			for (int k = 0; k < 2; k++) {
				dp[i][j][k] = -1;	
			}
		}
	}
	ll ans = 0;

	for (int i = 0, k = 0, last = 0; i < n; i++) {
		int val = 0;
		int up = s[i] - '0';
		if (k) up = 9;
		for (int j = last; j <= up; j++) {
			if (get (i + 1, j, k | (j + '0' < s[i]))) {
				val = j;
			}
		} 
		ans *= 10;
		ans += val;
		last = val;
		k |= val + '0' < s[i];
	}

	cout << ans << endl;                   
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
             
	while (T --> 0) {	
		load ();  
		solve ();
	}

	clog << (clock () - st) / CLOCKS_PER_SEC << endl;

	return 0;
}