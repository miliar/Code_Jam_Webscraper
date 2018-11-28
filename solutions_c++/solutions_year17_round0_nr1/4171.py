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

char flip_1(char cake) {
	if (cake == '+') {
		return '-';
	} else if (cake == '-') {
		return '+';
	}
	return ' ';
}

void flip_k(string &cakes, ll k) {
	for (int i = cakes.size() - 1; i > cakes.size() - k - 1; i--) {
		cakes[i] = flip_1(cakes[i]);
	}
}

int main() {
	int n, k, m;
	ifstream in("input.txt");
	ofstream out("output.txt");
	in >> n;
	string cakes;
	rep(i, 1, n + 1) {
		in >> cakes >> k;
		m = 0;
		while (cakes.back() == '+') {
			cakes.pop_back();
		}
		if (cakes.empty()) {
			out << "Case #" << i << ": 0" << endl;
			continue;
		}
		while (cakes.back() == '-') {
			if (cakes.empty()) {
				break;
			}
			if (cakes.size() < k) {
				break;
			}
			flip_k(cakes, k);
			m++;
			while (cakes.back() == '+') {
				cakes.pop_back();
				if (cakes.empty()) {
					break;
				}
			}
			if (cakes.size() < k) {
				break;
			}
		}
		if (cakes.empty()) {
			out << "Case #" << i << ": " << m << endl;
		} else {
			out << "Case #" << i << ": IMPOSSIBLE" << endl;
		}
	}
}