#include <iostream>
#include <vector>
#include <numeric>
#include<limits>
#include <random>
#include <iomanip> 
#include <deque>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

int INF = 1e8;

int hd, ad, hk, ak, b, d, HD;

map<tuple<int, int, int, int>, int> memo;
set<tuple<int, int, int, int>> seen;

int search(int hd, int ad, int hk, int ak) {
	auto key = tuple<int, int, int, int>(hd, ad, hk, ak);
	if (memo.find(key) != memo.end())
		return memo[key];

	if (seen.find(key) != seen.end() && memo.find(key) == memo.end())
		return INF;

	seen.insert(key);

	if (hd <= 0)
		return memo[key] = INF;

	if (ad >= hk)
		return memo[key] = 1;
	
	int result = memo[key] = INF;
	if (hd > ak) {
		result = min(result, search(hd - ak, ad, hk - ad, ak));
		result = min(result, search(hd - ak, ad + b, hk, ak));
	}
	else {
		result = min(search(HD - ak, ad, hk, ak), result);
	}

	if (ak > 0)
		result = min(result, search(hd - max(ak - d, 0), ad, hk, max(ak - d, 0)));

	return memo[key] = 1 + result;
}

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t) {
		memo.clear();
		seen.clear();
		cin >> hd >> ad >> hk >> ak >> b >> d;
		HD = hd;

		/*if (hk > ad && hd <= ak) { // attack
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
			continue;
		}

		if (ak > d && hd <= (ak - d)) { // debuf
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
			continue;
		}*/

		//if (ak > 2 * d && hd <= (2 * ak - 3 * d)) {
		//	cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		//	continue;
		//}
		int result = search(hd, ad, hk, ak);


		if(result >= INF)
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << t << ": " << result << endl;


	}

	return 0;
}
