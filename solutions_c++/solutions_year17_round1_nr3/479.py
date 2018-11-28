#include <algorithm>
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;

map <pair <pair <int, int>, pair <int, int> >, int> arr;

int sol(int Hd, int Ad, int Hk, int Ak, int B, int D, int Heal) {
	// cout << Hd << " " << Ad << " " << Hk << " " << Ak << " " << B << " " << D << endl; 
	if (arr.count({{Hd, Ad}, {Hk, Ak}}) > 0)
		return arr[{{Hd, Ad}, {Hk, Ak}}];
	int ans = 1e9;
	
	arr[{{Hd, Ad}, {Hk, Ak}}] = ans;

	
	if (Hk <= 0) {
		ans = 0;
	} else if (Hd <= 0) {
		ans = 1e9;
	} else if (Ad >= Hk){
		ans = 1;
	} else {
	// if (Heal <= 2 * Ak && Hk > Ad && (D + B == 0)) {
	// 	return 1e9;
	// }
	// if (Ak == 0 && Ad < Hk) {
	// 	return 1 + min(sol(Hd, Ad, Hk - Ad, Ak, B, D, Heal), sol(Hd, Ad + B, Hk, Ak, B, D, Heal));
	// }
	// if (Ak == 0 && Ad >= Hk) {
	// 	return 1;
	// }
	// if (Ak >= Hd) {
	// 	if (Hd < Heal - Ak)
	// 		return 1 + sol(Heal - Ak, Ad, Hk, Ak, B, D, Heal);
	// 	else
	// 		return 1e9;
	// }

		if (Hd < Heal - Ak) {
			ans = min(ans, sol(Heal - Ak, Ad, Hk, Ak, B, D, Heal));
		}
		ans = min(ans, sol(Hd - Ak, Ad, Hk - Ad, Ak, B, D, Heal));
		// cout << "GO";
		if (B != 0)
			ans = min(ans, sol(Hd - Ak, Ad + B, Hk, Ak, B, D, Heal));
		if (D != 0)
			ans = min(ans, sol(Hd - max(0, (Ak - D)), Ad, Hk, max(0, (Ak - D)), B, D, Heal));
		ans++;
	}
	arr[{{Hd, Ad}, {Hk, Ak}}] = ans;
	return ans;
}

void sol() {
	int Hd, Ad, Hk, Ak, B, D;
	cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
	int ans = sol(Hd, Ad, Hk, Ak, B, D, Hd);
	if (ans >= 1e9) {
		cout << "IMPOSSIBLE";
	} else {
		cout << ans;
	}
	cout << endl;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		arr.clear();
		cout << "Case #" << i + 1 << ": ";
		sol();
	}

	fclose(stdin);
	fclose(stdout);
}