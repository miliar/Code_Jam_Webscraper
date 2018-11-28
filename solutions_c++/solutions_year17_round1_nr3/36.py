#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;

#define A first
#define B second

ll hd, ad, hk, ak, b, d, t;

//after t1 turns what is the knights attack, and my health

ll max(ll x, ll y) {
	return (x<y)?y:x;
}
pii compatk(int t1) {
	int h = hd, a = ak;
	for (int i = 0; i < t1; ++i) {
		if (h-max(0, a-d) <= 0)
			h = hd-a;
		else
			a = max(0, a-d), h -= a;
		if (h <= 0) {
			h = 0; break;
		}
	}

	return pii(h, a);
}

pair<pii, int> compbuff(int t1, int t2) {
	pii p = compatk(t1);
	int h = p.A, a = p.B, a2 = ad;
	if (h == 0)
		return make_pair(pii(0, 0), 0);
	for (int i = 0; i < t2; ++i) {
		if (h-a <= 0)
			h = hd-a;
		else
			h -= a, a2 += b;
		if (h <= 0)
			return make_pair(pii(0, 0), 0);
	}

	return make_pair(pii(h, a), a2);
}

bool dead(int t1, int t2, int t3) {
	pair<pii, int> q = compbuff(t1, t2);
	if (q.A.A == 0)
		return 0;
	int hh = hk, h = q.A.A, a = q.A.B, a2 = q.B;
	for (int i = 0; i < t3; ++i) {
		if (hh-a2 <= 0)
			return 1;
		if (h-a <= 0)
			h = hd-a;
		else
			h -= a, hh -= a2;
		if (h <= 0)
			return 0;
	}

	return 0;
}

void doit(int abcd) {
	cout << "Case #" << abcd+1 << ": ";
	cin >> hd >> ad >> hk >> ak >> b >> d;

	int mini = 1000;

	for (int t1 = 1; t1 <= 605; ++t1)
		for (int t2 = 0; t2 <= t1; ++t2)
			for (int t3 = 0; t3 <= t1-t2; ++t3) {
				if (mini <= t1)
					continue;
				if (t2 >= 205 || t3 >= 205 || (t1-t2-t3 >= 205))
					continue;
				if (dead(t2, t3, t1-t2-t3))
					mini = min(mini, t1);
			}

	if (mini == 1000)
		cout << "IMPOSSIBLE\n";
	else
		cout << mini << endl;
}

int main() {
	cin >> t;
	for (int i = 0; i < t; ++i)
		doit(i);
}