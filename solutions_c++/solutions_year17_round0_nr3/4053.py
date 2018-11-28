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

pair<int, int> kek(int x) {
	return mp(x / 2, (x - 1) / 2);
}

pair<int, int> get(int n, int k) {
	multiset<int> se;
  	se.insert(n);
  	for (int i = 0; i < k - 1; i++) {
  		int x = *se.rbegin();
  		se.erase(--se.end());
  		se.insert(x / 2);
  		se.insert((x - 1) / 2);
  	}
  	int x = *se.rbegin();
  	return kek(x);
}

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
		int n, k;
		cin >> n >> k;
		auto ans = get(n, k);

		
		cout << "Case #" << test + 1 << ": " << ans.first << " " << ans.second << endl;
		cerr << "test #" << test << " completed" << endl;
	}


    return 0;
}   