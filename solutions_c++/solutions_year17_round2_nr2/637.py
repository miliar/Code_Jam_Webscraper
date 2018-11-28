#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
#include <cstring>
using namespace std;

int T, n;
int input[6];
char colors[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};
int principles[3] = {0, 2, 4};

int main() {
	scanf("%d", &T);
	for (int it = 1; it <= T; it++) {
		scanf("%d", &n);
		for (int i = 0; i < 6; i++) {
			scanf("%d", &input[i]);
		}
		printf("Case #%d: ", it);

		int max_cnt = 0;
		for (int i = 0; i < 6; i++) {
			if (input[max_cnt] < input[i]) {
				max_cnt = i;
			}
		}
		
		if (n/2 < input[max_cnt]) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		int l1 = (max_cnt + 2) % 6;
		int l2 = (max_cnt + 4) % 6;
		int last_pos;
		while (input[max_cnt] > 0 || input[l1] > 0 || input[l2] > 0) {
			if (input[max_cnt] > 0) {
				int pos = (input[l1] > input[l2]) ? l1 : l2;
				cout << colors[max_cnt];
				cout << colors[pos];
				input[max_cnt]--;
				input[pos]--;
				last_pos = pos;
			}
			else {
				int pos = (l1 == last_pos) ? l2 : l1;
				int alt_pos = (l1 == last_pos) ? l1 : l2;
				if (input[pos] > 0) {
					cout << colors[pos];
					input[pos]--;
				}
				if (input[alt_pos] > 0) {
					cout << colors[alt_pos];
					input[alt_pos]--;
				}
			}
		}
		printf("\n");
	}
	return 0;
}