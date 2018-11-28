#include <iostream>
#include <cstdio>

using namespace std;

int cnt[1000001];

int main() {
	int testCnt;
	cin >> testCnt;
	for (int testNum = 1; testNum <= testCnt; testNum++) {
		cout << "Case #" << testNum <<": ";
		int n, k;
		cin >> n >> k;
		for (int i = 0; i <= n; i++)
			cnt[i] = 0;
		cnt[n] = 1;
		int index = n;
		while (k > 0) {
			while (cnt[index] == 0) {
				index--;
			}
			if (k == 1) {
				cout << index / 2 << " " << index - 1 - index / 2 << endl;
				break;
			}
			cnt[index]--;
			cnt[index / 2]++;
			cnt[index - 1 - index / 2]++;
			k--;
		}
	}
	return 0;
}