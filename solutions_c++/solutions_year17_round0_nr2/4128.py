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

ll int_pow(int base, int power) {
  	if (power == 0) {
  		return 1;
  	}
  	if (power == 1) {
  		return base;
  	}
  	ll tmp = int_pow(base, power / 2);
  	if (power % 2 == 0)  {
  		return tmp * tmp;
  	} else {
  		return base * tmp * tmp;
  	}
}

bool can_change(string &n) {
	for(int i = n.size() - 1; i > 0; i--) {
		if (n[i] < n[i - 1]) {
			char c = n[i - 1];
			n[i - 1] = c - 1;
			rep(j, i, n.size()) {
				n[j] = '9';
			}
			return true;
		}
	}
	return false;
}

int main() {
	ifstream in("input.txt");
	ofstream out("output.txt");
	int t;
	string n;
	in >> t;
	rep(i, 0, t) {
		in >> n;
		bool change = can_change(n);
		while (change) {
			change = can_change(n);
		}
		while (n[0] == '0' && n.size() > 1) {
			n.erase(0, 1);
		}
		out << "Case #" << i + 1 << ": " << n;
		if (i != t - 1) {
			out << endl;
		}
	}
}