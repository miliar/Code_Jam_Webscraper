#include <iostream>
#include <utility>
#include <vector>

using namespace std;


void solve() {
	int N, P;
	cin >> N >> P;
	vector<int> t(P, 0);
	for (int i = 0; i < N; i++) {
		int tmp;
		cin >> tmp;
		t[tmp % P]++;
	}
	int min, left, sum = 0;
	switch (P) {
	case 2:
		sum = t[0] + t[1] / 2;
		if (t[1] % 2 == 1)
			sum++;
		break;
	case 3:
		sum = 0;
		while (t[0] > 0) {
			sum++; t[0]--;
		}
		while (t[1] > 0 && t[2]>0) {
			sum++; t[1]--; t[2]--;
		}
		while (t[1] > 2) {
			sum++; t[1] -= 3;
		}
		while (t[2] > 2) {
			sum++; t[2] -= 3;
		}
		if (t[1] + t[2] > 0) {
			sum++;
		}
		break;
	case 4:
		sum = 0;
		while (t[0] > 0) {
			sum++; t[0]--;
		}
		while (t[1] > 0 && t[3]>0) {
			sum++; t[1]--; t[3]--;
		}
		while (t[2] > 1) {
			sum++; t[2] -= 2;
		}
		if (t[2] > 0 && t[1] > 1) {
			sum++; t[2]--; t[1] -= 2;
		}
		if (t[2] > 0 && t[3] > 1) {
			sum++; t[2]--; t[3] -= 2;
		}
		while (t[1] > 3) {
			sum++; t[1] -= 4;
		}
		while (t[3] > 3) {
			sum++; t[3] -= 4;
		}
		if (t[1] + t[3] > 0) {
			sum++;
		}
		break;
	}
	printf("%d", sum);
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