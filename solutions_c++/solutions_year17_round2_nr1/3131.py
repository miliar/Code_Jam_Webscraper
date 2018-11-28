#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>

using namespace std;

typedef long long ll; typedef unsigned long long ull; typedef vector<ll> vi; typedef pair<ll,ll> pi;
const int _1e5 = 100000; const int _1e7 = 10000000; const int _1e9 = 1000000000;

template<typename A, typename B> ostream& operator<<(ostream& str, const pair<A,B>& p) { str << "(" << p.first << ", " << p.second << ")"; return str; }
template<typename T> ostream& operator<<(ostream& str,             const vector<T>& v) { str << "["; for(auto n : v) str << n << ", "; str << "]"; return str; }
template<typename T> ostream& operator<<(ostream& str,             const set<T>& v) { str << "{"; for(auto n : v) { str << n << ", "; } str << "}"; return str; }
template<typename K, typename V> ostream& operator<<(ostream& str, const unordered_map<K, V>& v) { str << "{"; for(auto&& p : v) { str << p.first << " => " << p.second << ", "; } str << "}"; return str; }

#define debug(x) cout <<  #x  << ": " << x << endl

struct horse {
	long long km;
	long long speed;
};

int main() {
	ios_base::sync_with_stdio(false);
	
	long long t;
	cin >> t;

	for (long long i=1; i<=t; ++i) {
		long long d,n;
		cin >> d >> n;


		vector<long double> finish(n);
		for (long long i=0; i<n; ++i) {
			long long k,s;
			cin >> k >> s;
			long double long_dist = 1.*(d - k) / s;
			finish.at(i) = long_dist;
		}

		sort(finish.begin(), finish.end());

		auto time = finish.back();

		std::cout << "Case #" << i << ": " << setprecision(8) << fixed << (d/time) << std::endl;
	}
}
