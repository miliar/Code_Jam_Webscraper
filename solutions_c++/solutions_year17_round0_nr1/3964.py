#include <bits/stdc++.h>
using namespace std;

#ifdef WIN32
    #define lld "%I64d"
#else
    #define lld "%lld"
#endif

#define mp make_pair
#define pb push_back
#define put(x) { cout << #x << " = "; cout << (x) << endl; }

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef double db;

const int M = 1e6 + 15;
const int Q = 1e9 + 7;

int main() {
    srand(time(NULL));
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
	cin.tie(0);
	ios_base::sync_with_stdio(0);
	
	int T;
	cin >> T;
	for (int test = 0; test < T; test++) {

		string s;
		cin >> s;
		int k;
		cin >> k;

		int ans = 0;
		for (int i = 0; i <= (int)s.size() - k; i++) {
			if (s[i] == '+') continue;		
			ans++;
			for (int j = i; j < i + k; j++) {
				s[j] = (s[j] == '+' ? '-' : '+');
			}
		}
		bool ok = 1;
		for (int i = (int)s.size() - k + 1; i < (int)s.size(); i++) {
			ok &= (s[i] == '+');
		}

		if (ok)
			cout << "Case #" << test + 1 << ": " << ans << endl;
		else
			cout << "Case #" << test + 1 << ": " << "IMPOSSIBLE" << endl;
		cerr << "test #" << test << " completed" << endl;
	}


    return 0;
}   