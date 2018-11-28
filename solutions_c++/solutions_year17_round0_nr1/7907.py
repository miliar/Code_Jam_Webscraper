#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>

using namespace std;

const int oo = 1 << 30;

bool idealPancakes (string pancakes) {
	for (int i = 0; i < pancakes.size(); i++)
		if (pancakes[i] == '-')
			return false;
	return true;
}

char flipPancake (char pancake) {
	return pancake == '-' ? '+' : '-';
}

string flipPancakes (string pancakes, int start, int k) {
	if (start + k - 1 >= pancakes.size()) {
		return pancakes;
	}
	for (int i = start, j = 0; i < pancakes.size() && j < k; i++, j++) {
		pancakes[i] = flipPancake(pancakes[i]);
	}
	return pancakes;
}

int getWithStupidWay (string pancakes, int k) {

	vector <int> intervals;

	for (int i = 0; i + k - 1 < pancakes.size(); i++) {
		intervals.push_back(i);
	}

	int res = oo;

	for (int mask = 0; mask < (1 << intervals.size()); ++mask) {
		string temp = pancakes;
		int cnt = 0;
		for (int i = 0; i < intervals.size(); i++) {
			if (mask & (1 << i)) {
				pancakes = flipPancakes(pancakes, intervals[i], k);
				cnt++;
			}
		}
		if (idealPancakes (pancakes)) {
			res = min(res, cnt);
		}
		pancakes = temp;
	}


	return res;
}

int getShortestWayToMakeIdealPancakes(string pancakes, int k) {

	int res = 0;

	for (int i = 0; i < pancakes.size(); i++) {
		if (pancakes[i] == '-') {
			pancakes = flipPancakes(pancakes, i, k);
			res++;
		}
	}

	if (idealPancakes (pancakes))
		return res;

	return oo;

}

int main () {

	int test;
	cin >> test;
	int cnt = 0;
	while (test--) {

		string pancakes;
		int k;

		cin >> pancakes >> k;

		int res = getShortestWayToMakeIdealPancakes(pancakes, k);
		cout << "Case #" << ++cnt << ": " << (res == oo ? "IMPOSSIBLE" : to_string(res));

		if (test)
			cout << "\n";

	}


	return 0;

}