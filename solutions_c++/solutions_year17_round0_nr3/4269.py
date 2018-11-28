#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> ii;
typedef pair<ll, ll> lll;
typedef vector<int> vi;
typedef vector<ii> vii;
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
const ll INF = 2147483647;

int main() {
	int t;
	ll n, k;
	set<ll>::iterator c;
	ll c_val;
	ifstream in("input.txt");
	ofstream out("output.txt");
	in >> t;
	rep(i, 1, t + 1) {
		in >> n >> k;
		multiset<ll> gaps;
		gaps.insert(n);
		rep(j, 0, k) {
			c = gaps.end();
			c--;
			c_val = *c;
			gaps.erase(c);
			if (c_val % 2 == 1) {
				gaps.insert((c_val - 1) / 2);
				gaps.insert((c_val - 1) / 2);
			} else {
				gaps.insert(c_val / 2);
				gaps.insert(c_val / 2 - 1);
			}
		}
		if (c_val % 2 == 1) {
			out << "Case #" << i << ": " << (c_val - 1) / 2 << " " << (c_val - 1) / 2 << endl;
		} else {
			out << "Case #" << i << ": " << c_val / 2 << " " << c_val / 2 - 1 << endl;
		}
	}
}