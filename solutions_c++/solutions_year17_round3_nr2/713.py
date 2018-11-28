#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

bool compare(pair<char, int> t1, pair<char, int> t2) {
	return t1.second < t2.second;
}


void solve() {
	int Ac, Aj;
	cin >> Ac >> Aj;
	vector<char> Shift(1440, 'X'); 
	vector<pair<char, int> > order;
	int J = 720, C = 720;
	for (int i = 0; i < Ac; i++) {
		int s, f;
		cin >> s >> f;
		for (int j = s; j < f; j++) {
			Shift[j] = 'C';
		}
		C -= f - s;
	}
	for (int i = 0; i < Aj; i++) {
		int s, f;
		cin >> s >> f;
		for (int j = s; j < f; j++) {
			Shift[j] = 'J';
		}
		J -= f - s;
	}
	int cnt = 0;
	char last;
	for (int i = 1439; i >0; i--) {
		if (Shift[i] != 'X') {
			last = Shift[i];
			break;
		}
		cnt++;
	}
	int changes = 0;
	for (int i = 0; i < 1440; i++) {
		if (Shift[i] == 'C') {
			if (last == 'C' && cnt != 0)
				order.push_back(pair<char, int>('C', cnt));
			cnt = 0;
			if (last == 'J') {
				changes++;
			}
			last = 'C';
		}
		if (Shift[i] == 'J') {
			if (last == 'J' && cnt != 0)
				order.push_back(pair<char, int>('J', cnt));
			cnt = 0;
			if (last == 'C') {
				changes++;
			}
			last = 'J';
		}
		if (Shift[i] == 'X') {
			cnt++;
		}
	}
	sort(order.begin(), order.end(), compare);
	for (int i = 0; i < order.size(); i++) {
		if (order[i].first == 'C') {
			if (C >= order[i].second) {
				C -= order[i].second;
				order[i].first = 'X';
			}
		}
		if (order[i].first == 'J') {
			if (J >= order[i].second) {
				J -= order[i].second;
				order[i].first = 'X';
			}
		}
	}
	for (int i = 0; i < order.size(); i++) {
		if (order[i].first != 'X') {
			changes += 2;
		}
		
	}
	printf("%d", changes);
}

int  main() {
	int k;
	cin >> k;
	for (int i = 0; i < k; i++) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}