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
// #define cerr                                                                   \
//   if (true)                                                                    \
//   cerr

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<unsigned long long> vull;

int T;
ll N,K;

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

// ll get(ll n){
// 	if(n == 1)return N;
// 	ll ret = 0;
// 	if(n % 2 == 0){
// 		ret = (get(n / 2) -1) / 2;
// 	}else{
// 		ll nn = get(n / 2);
// 		ret = nn - ((nn -1) / 2);
// 	}
//
// 	return ret;
// }
vi V;
void solve(ll t,ll N , ll K) {
	V.clear();
	V.push_back(N);

	REP(i,K){
		sort(ALL(V));
		int n = V.back();
		V.pop_back();
		int l = (n - 1) / 2;
		int r = (n-1) - l;
		V.push_back(l);
		V.push_back(r);

		// dump(n);
		// dump(l);
		// dump(r);
		if(i == K-1){
			cout << "Case #" << t + 1 << ": " << max(l,r) << " " << min(l,r) << endl;
			break;
		}
	}
}

int main() {
	V.reserve(10000000);
	ios::sync_with_stdio(false);
	cin >> T;

	REP(t, T){
		cin >> N >> K;
		solve(t,N,K);
	}

	return 0;
}
