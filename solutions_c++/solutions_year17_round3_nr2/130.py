#define _CRT_SECURE_NO_WARNINGS

#include <algorithm>
#include <assert.h>
#include <bitset>
#include <cmath>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_set>
#include <unordered_map>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> llp;

const ll INF = 1000000000000;

int main() {
	ll t;
	cin >> t;

	for (ll q = 0; q < t; q++) {
		
		ll ac, aj;
		vector<pair<llp, ll>> tl;
		cin >> ac >> aj;

		for (ll i = 0; i < ac; i++) {
			pair<llp, int> pr;
			cin >> pr.first.first >> pr.first.second;
			pr.second = 1;
			tl.push_back(pr);
		}

		for (ll i = 0; i < aj; i++) {
			pair<llp, int> pr;
			cin >> pr.first.first >> pr.first.second;
			pr.second = 2;
			tl.push_back(pr);
		}

		sort(tl.begin(), tl.end());

		ll swps = 0;
		ll fc = 0, fj = 0;
		ll st = 0, ct = 0, jt = 0;
		multiset<ll> cs, js;

		if (tl[0].second != tl[tl.size() - 1].second) {
			swps++;
			st += tl[0].first.first + 1440 - tl[tl.size() - 1].first.second;
		}
		else {
			if (tl[0].second == 1) {
				ct += tl[0].first.first + 1440 - tl[tl.size() - 1].first.second;
				cs.insert(tl[0].first.first + 1440 - tl[tl.size() - 1].first.second);
			}
			else {
				jt += tl[0].first.first + 1440 - tl[tl.size() - 1].first.second;
				js.insert(tl[0].first.first + 1440 - tl[tl.size() - 1].first.second);
			}
		}

		if (tl[0].second == 1) {
			fc += tl[0].first.second - tl[0].first.first;
		}
		else {
			fj += tl[0].first.second - tl[0].first.first;
		}

		for (ll i = 1; i < ac + aj; i++) {
			if (tl[i].second != tl[i - 1].second) {
				swps++;
				st += tl[i].first.first - tl[i - 1].first.second;
			}
			else {
				if (tl[i].second == 1) {
					ct += tl[i].first.first - tl[i - 1].first.second;
					cs.insert(tl[i].first.first - tl[i - 1].first.second);
				}
				else {
					jt += tl[i].first.first - tl[i - 1].first.second;
					js.insert(tl[i].first.first- tl[i - 1].first.second);
				}
			}

			if (tl[i].second == 1) {
				fc += tl[i].first.second - tl[i].first.first;
			}
			else {
				fj += tl[i].first.second - tl[i].first.first;
			}
		}

		auto itc = cs.rbegin();
		while (fc + ct > 720) {
			ct -= *itc;
			itc++;

			swps += 2;
		}

		auto itj = js.rbegin();
		while (fj + jt > 720) {
			jt -= *itj;
			itj++;

			swps += 2;
		}

		cout << "Case #" << q + 1 << ": " << swps << "\n";
	}

	return 0;
}