#include <algorithm>
#include <bitset>
#include <cassert>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <math.h>
#include <memory>
#include <queue>
#include <sstream>
#include <stdio.h>
#include <string>
#include <vector>

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define POW(n) ((n) * (n))
#define ALL(a) (a).begin(), (a).end()
#define dump(v) (cerr << #v << ": " << v << endl)
#define cerr                                                                   \
  if (true)                                                                    \
  cerr

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<unsigned long long> vull;

int T;
string S; int K;

// ll n = to_T<ll>("114514")
template <class T> T to_T(const string &s) {
	istringstream is(s);
	T res;
	is >> res;
	return res;
}
template <class T> string to_s(const T &a) {
	ostringstream os;
	os << a;
	return os.str();
}

ll solve(string S,int K) {
	ll ans = 0;

	vi l(S.size());
	REP(i, S.size())l[i] = S[i] == '+' ? 1 : 0;

	REP(i, l.size() - K +1) if (l[i] == 0){
		ans++;
		FOR(j, i, min(i + K, (int)l.size())){
			l[j] ^= 1;
		}
	}

	REP(i, l.size()){
		if (l[i] == 0) return -1;
	}

	int num = 0;
	num = num | 1 << 10;
	

	return ans;
}


int main() {
	ios::sync_with_stdio(false);
	cin >> T;

	REP(t, T){
		cin >> S;
		cin >> K;
		ll ans = solve(S, K);
		if (ans < 0){
			cout << "Case #" << t + 1 << ": IMPOSSIBLE" << endl;
		}
		else{
			cout << "Case #" << t + 1 << ": " << ans << endl;
		}
	}

	return 0;
}
