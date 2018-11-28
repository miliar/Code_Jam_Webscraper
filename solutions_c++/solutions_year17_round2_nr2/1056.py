#include <bits/stdc++.h>
using namespace std;

char color(int num) {
	if(num == 0) {
		return 'R';
	}
	else if(num == 1) {
		return 'O';
	}
	else if(num == 2) {
		return 'Y';
	}
	else if(num == 3) {
		return 'G';
	}
	else if(num == 4) {
		return 'B';
	}
	else if(num == 5) {
		return 'V';
	}
}

int main() {
	int cnt_tests;
	scanf("%d", &cnt_tests);

	for(int cs = 1; cs <= cnt_tests; cs++) {
		int n, a[6];
		scanf("%d%d%d%d%d%d%d", &n, &a[0], &a[1], &a[2], &a[3], &a[4], &a[5]);
		
		string s = "";
		int first, last = -1;
		for(int i = 0; i < n; i++) {
			int curr, curr_max = 0;

			for(int j = 0; j < 6; j++) {
				if(a[j] > curr_max && j != last || (a[j] == curr_max && j != last && j == first)) {
					curr = j;
					curr_max = a[j];
				}
			}

			s += color(curr);
			last = curr;
			a[curr]--;
			
			if(i == 0) {
				first = curr;
			}
		}

		if(first == last) {
			printf("Case #%d: IMPOSSIBLE\n", cs);
		}
		else {
			printf("Case #%d: %s\n", cs, s.c_str());
		}
	}

	return 0;
}
