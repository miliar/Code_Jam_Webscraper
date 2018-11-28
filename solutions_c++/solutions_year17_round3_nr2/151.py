#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <list>
#include <array>
#include <map>
#include <algorithm>
#include <tuple>
using namespace std;

static void solve() {
	enum OWNER {
		C, J
	};
	int Ac, Aj;
	cin >> Ac >> Aj;
	vector<tuple<int, int, OWNER>> A;
	vector<int> S(2, 0);
	for (int i = 0; i < Ac; i++) {
		int Ci, Di;
		cin >> Ci >> Di;
		S[C] += Di - Ci;
		A.emplace_back(Ci, Di, C);
	}
	for (int i = 0; i < Aj; i++) {
		int Ji, Ki;
		cin >> Ji >> Ki;
		S[J] += Ki - Ji;
		A.emplace_back(Ji, Ki, J);
	}
	sort(A.begin(), A.end(), [](auto &lhs, auto &rhs) {
		return get<0>(lhs) < get<0>(rhs);
	});

	//cerr << S[C] << "\t" << S[J] << endl;

	int now = get<1>(A.back()) - 60 * 24;
	OWNER prevWho = get<2>(A.back());
	vector<vector<int>> betweenAct(2);
	int exchange = 0;
	for (auto &a : A) {
		auto from = get<0>(a);
		auto to = get<1>(a);
		auto who = get<2>(a);

		if (prevWho == who) {
			//cerr << from << "\t" << now << "\t" << from - now << endl;
			betweenAct[who].push_back(from - now);
		} else {
			exchange++;
		}

		now = to;
		prevWho = who;
	}

	sort(betweenAct[C].begin(), betweenAct[C].end());
	sort(betweenAct[J].begin(), betweenAct[J].end());

	for (auto who : std::list<OWNER>{C, J}) {
		for (auto t : betweenAct[who]) {
			//cerr << "betweenAct" <<  who << "\t" << t << endl;
			if (S[who] + t > 720) {
				exchange += 2;
			} else {
				S[who] += t;
			}
		}
	}

	cout << exchange;
}

int main() {
	int T;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	return 0;
}
