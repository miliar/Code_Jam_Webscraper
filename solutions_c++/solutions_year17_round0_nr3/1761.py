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
ll n, k;
int tc;
map<ll, __int128> cnt;

void pre () {
}

void load () {          
	cin >> n >> k;
}

void solve () {
	tc++;
	cout << "Case #" << tc << ": ";
	
	cnt.clear ();
	cnt[n]++;

	while (k) {
		auto it = *cnt.rbegin ();
		cnt.erase (cnt.find (it.first));
		ll l = it.first - 1;
		ll f = l >> 1;
		ll s = l - f;
		if (it.second >= k) {
			cout << s << ' ' << f << '\n';
			return;
		}
		k -= it.second;
        if (f)
        	cnt[f] += it.second;
		if (s)
			cnt[s] += it.second;				
	}
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