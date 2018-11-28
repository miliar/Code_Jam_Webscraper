#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll TC, N, R, O, Y, G, B, V;
list<char> L;
vector<pair<ll, char> > colours;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> TC;
	for (ll tc = 1; tc <= TC; tc++) {
		cin >> N >> R >> O >> Y >> G >> B >> V;
		L.clear();
		colours.clear();

		cout << "Case #" << tc << ": ";
		if (G > 0 && 2*G > R) {
			cout << "IMPOSSIBLE\n";
			continue;
		}
		else {
			R -= 2*G;
		}

		if (O > 0 && 2*O > B) {
			cout << "IMPOSSIBLE\n";
			continue;
		}
		else {
			B -= 2*O;
		}

		if (V > 0 && 2*V > Y) {
			cout << "IMPOSSIBLE\n";
			continue;
		}
		else {
			Y -= 2*V;
		}

		colours.push_back(make_pair(R, 'R'));
		colours.push_back(make_pair(O, 'O'));
		colours.push_back(make_pair(Y, 'Y'));
		colours.push_back(make_pair(G, 'G'));
		colours.push_back(make_pair(B, 'B'));
		colours.push_back(make_pair(V, 'V'));

		sort(colours.begin(), colours.end());

		for (ll i = 0; i < colours[5].first; i++) {
			L.push_back(colours[5].second);
		}

		for (ll i = 4; i >= 0; i--) {
			for (auto it = L.begin(); it != L.end(); it++) {
				if (colours[i].first == 0) break;
				auto it2 = it;
				advance(it2, 1);
				if (it2 == L.end()) continue;
				auto it3 = it;
				advance(it3, 1);
				if (*it == *it3) {
					L.insert(it3, colours[i].second);
					colours[i].first--;
				}
			}

			if (colours[i].first > 0 && *L.begin() == *L.rbegin()) {
				L.insert(L.begin(), colours[i].second);
				colours[i].first--;
			}

			for (auto it = L.begin(); it != L.end(); it++) {
				if (colours[i].first == 0) break;
				auto it2 = it;
				advance(it2, 1);
				if (it2 == L.end()) continue;
				auto it3 = it;
				advance(it3, 1);
				if (*it != colours[i].second && *it3 != colours[i].second) {
					L.insert(it3, colours[i].second);
					colours[i].first--;
				}	
			}

			while (colours[i].first > 0) {
				L.push_back(colours[i].second);
			}
		}

		bool ok = true;
		for (auto it = L.begin(); it != L.end(); it++) {
			auto it2 = it;
			advance(it2, 1);
			if (it2 == L.end()) continue;
			auto it3 = it;
			advance(it3, 1);
			if (*it == *it3) {
				cout << "IMPOSSIBLE\n";
				ok = false;
				break;
			}
		}
		if (ok && L.front() == L.back()) {
			cout << "IMPOSSIBLE\n";
			ok = false;
		}

		if (ok) {
			ll rc = 0, bc = 0, yc = 0;
			for (auto it = L.begin(); it != L.end(); it++) {
				cout << *it;
			}

			cout << "\n";
		}

	}
	
	return 0;
}
