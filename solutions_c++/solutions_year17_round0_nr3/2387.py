#pragma warning (disable : 4996)

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <string>

using namespace std;

typedef long double ld;
typedef long long ll;
#define mp make_pair

const ll ONE = 1LL;
const ll TWO = 2LL;

int main() {
#ifdef MANO
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int qn;
	cin >> qn;
	string s;
	for (int uu = 0; uu < qn; ++uu) {
		ll n, k;
		cin >> n >> k;
		ll p2 = 0;
		while (k >= (ONE << p2)) {
			++p2;
		}
		k -= (ONE << (p2 - ONE)) - ONE;
		
		ll na = 0;
		ll nb = 1;
		ll a = n - 1;
		ll b = n;
		for (int i = 0; i < p2 - 1; ++i) {
			ll d, r;
			ll nnb = 0;
			ll nna = 0;
			
			d = (b - ONE) / TWO;
			r = (b - ONE) % TWO;
			if (r == 0) {
				nnb += TWO * nb + na;
				nna += na;
				b = (b - ONE) / TWO;
				a = b - 1;
			}
			else {
				nnb += nb;
				nna += TWO * na + nb;
				b = (b - ONE) / TWO + ONE;
				a = b - 1;
			}

			na = nna;
			nb = nnb;
		}

		cout << "Case #" << uu + 1 << ": ";
		if (k <= nb) {
			ll d = (b - ONE) / TWO;
			ll r = (b - ONE) % TWO;
			cout << d + r << ' ' << d;
		}
		else {
			ll d = (a - ONE) / TWO;
			ll r = (a - ONE) % TWO;
			cout << d + r << ' ' << d;
		}
		cout << '\n';
		//cout << k << ' ';
		//cout << a << ' ' << b << ' ';
		//cout << na << ' ' << nb << '\n';
	}

	return 0;
}