#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <iostream>
#include <fstream>
#include <queue>
#include <map>
using namespace std;

struct Pos {
	int l, r;
	Pos(int l, int r) : l(l), r(r) {}
};

int main() {
	//freopen("input.txt", "r", stdin);
	freopen("C-small-2-attempt1.in", "r", stdin);
	//freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tt;
	cin >> tt;

	for (int t = 1; t <= tt; t++) {
		int n, k;
		cin >> n >> k;
		
		// len -> number
		map<int, int> lengths;
		lengths[n] = 1;

		for (int i = 0, pow = 1; ; i += pow, pow *= 2) {
			int len;

			map<int, int>::iterator it = lengths.begin();
			int shorter_len = it->first;
			int shorter_num = it->second;
			int longer_len = 0;
			int longer_num = 0;

			it++;
			if (it == lengths.end()) {
				len = shorter_len;
			}
			else {
				longer_len = it->first;
				longer_num = it->second;
				len = k <= i + longer_num ? longer_len : shorter_len;
			}

			if (i + pow >= k) {
				if (len % 2 == 0) {
					printf("Case #%d: %d %d\n", t, len / 2, len / 2 - 1);
				}
				else {
					printf("Case #%d: %d %d\n", t, len / 2, len / 2);
				}
				break;
			}

			lengths.clear();
			if (longer_len != 0) {
				if (longer_len % 2 == 0) {
					lengths[longer_len / 2 - 1] += longer_num;
					lengths[longer_len / 2] += longer_num;
				}
				else {
					lengths[longer_len / 2] += longer_num * 2;
				}
			}

			if (shorter_len != 0) {
				if (shorter_len % 2 == 0) {
					lengths[shorter_len / 2 - 1] += shorter_num;
					lengths[shorter_len / 2] += shorter_num;
				}
				else {
					lengths[shorter_len / 2] += shorter_num * 2;
				}
			}
		}
	}

	fclose(stdout);
	return 0;
}