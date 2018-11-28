#include<iostream>
#include<string>
#include<vector>
#include <algorithm>
using namespace std;

int main() {
	unsigned int T, N;
	cin >> T;

	for (int i = 1; i <= T; i++){
		cin >> N;
		if (N < 10) {
			cout << "Case #" << i << ": " << N << endl;;
		}
		else {
			unsigned int tmp, rem;
			int num[20] = { 0, };
			int l, p = 0;
			while (true) {
				tmp = N % 10;
				rem = N / 10;
				num[p] = tmp;
				N = rem;
				if (N == 0)
					break;
				p++;

			}
			l = p;
			p = -1;
			for (int j = l; j >= 0; j--) {
				if (j == 0) {
					p = -1;
				} else if (num[j] > num[j - 1]) {
					p = j;
					break;
				}			
			}

			for (int j = p+1; j <= l; j++) {
				if (num[j - 1] == num[j])
					p = j;
				else
					break;
			}

			if (p == -1) {
				cout << "Case #" << i << ": ";
				for (int j = l; j >= 0; j--)
					cout << num[j];
				cout << endl;
			}
			else {
				for (int j = 0; j < p; j++) {
					num[j] = 9;
				}
				if (num[p] == 1)
					l--;
				num[p]--;

				cout << "Case #" << i << ": ";
				for (int j = l; j >= 0; j--)
					cout << num[j];
				cout << endl;
			}

		}
	}
	return 0;
}