#include <bits/stdc++.h>
using namespace std;

#define error(args...) { vector<string> _v = split(#args, ','); err(_v.begin(), args); }
vector<string> split(const string& s, char c) { vector<string> v; stringstream ss(s); string x; while (getline(ss, x, c)) v.push_back(move(x)); return v; }
void err(vector<string>::iterator it) {}
template<typename T, typename... Args> void err(vector<string>::iterator it, T a, Args... args) { cerr << it->substr((*it)[0] == ' ', it->length()) << " = " << a << '\n'; err(++it, args...); }

typedef long long LL;
#define INF (1LL<<62)
int T;
LL Hd, Ad, Hk, Ak, B, D;

LL f(LL nd, LL nb) {
	// compute number of turns using nd debuffs and nb buffs
	// this works for small case, too slow for big case
	LL ret = 0;
	LL health = Hd;
	LL health2 = Hk;
	LL attack = Ad;
	LL attack2 = Ak;
	// error(nd, nb);
	while (nd) {
		if (health > attack2 - D) {
			attack2 = max(attack2 - D, 0LL);
			nd--;
		}
		else {
			health = Hd;
		}
		health -= attack2;
		ret++;
	}
	if (attack2 * 2 >= Hd) {
		return INF;
	}
	while (nb) {
		if (health > attack2) {
			attack += B;
			nb--;
		}
		else {
			health = Hd;
		}
		health -= attack2;
		ret++;
	}
	while (health2 > 0) {
		if (health > attack2 || health2 <= attack) {
			health2 -= attack;
		}
		else {
			health = Hd;
		}
		health -= attack2;
		ret++;
	}
	// error(ret);
	return ret;
}

LL solvenb(LL nd) {
	LL lo = 0;
	LL hi = Hk;
	// while (hi - lo > 2) {
	// 	LL mid = (lo + hi) / 2;
	// 	LL ans1 = f(nd, mid);
	// 	LL ans2 = f(nd, mid + 1);
	// 	if (ans1 > ans2) {
	// 		lo = mid;
	// 	}
	// 	else {
	// 		hi = mid + 1;
	// 	}
	// }

	LL ans = INF;
	for (LL i = lo; i <= hi; i++) {
		ans = min(ans, f(nd, i));
	}
	return ans;
}

LL solve() {
	// ternary search on nd
	LL lo = 0;
	LL hi = Ak;
	// while (hi - lo > 2) {
	// 	LL mid = (lo + hi) / 2;
	// 	LL ans1 = solvenb(mid);
	// 	LL ans2 = solvenb(mid + 1);
	// 	if (ans1 > ans2) {
	// 		lo = mid;
	// 	}
	// 	else {
	// 		hi = mid + 1;
	// 	}
	// }

	LL ans = INF;
	for (LL i = lo; i <= hi; i++) {
		ans = min(ans, solvenb(i));
	}
	return ans;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	freopen("C.txt", "r", stdin);
	freopen("C.out", "w", stdout);

	
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cout << "Case #" << tc << ": ";

		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		
		if (Ad >= Hk) {
			cout << 1 << '\n';
			continue;
		}
		if (Ak < Hd && Ad + max(Ad, B) >= Hk) {
			cout << 2 << '\n';
			continue;
		}

		if (Ak - D > Hd || (Ak - D) * 2 - D >= Hd) {
			cout << "IMPOSSIBLE" << '\n';
			continue;
		}

		cout << solve() << '\n';
	}

	cout.flush();
	return 0;
}
