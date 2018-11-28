#include <iostream>
#include <cstring>
using namespace std;

const int MAXN = 20;
char num[MAXN];
char result[MAXN];

bool feasible(int x) {
	for (int i = x + 1; num[i]; i++) {
		if (num[i] > num[x]) {
			return true;
		}
		else if (num[i] < num[x]) {
			return false;
		}
	}

	return true;
}

void getResult() {
	int len = strlen(num);
	result[len] = 0;

	for (int i = 0; i < len; i++) {
		if (!feasible(i)) {
			result[i] = num[i] - 1;
			for (int j = i + 1; j < len; j++) {
				result[j] = '9';
			}

			if (result[0] == '0') {
				cout << result + 1;
			}
			else {
				cout << result;
			}

			return;
		}
		else {
			result[i] = num[i];
		}
	}

	cout << result;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("b_large.out", "w", stdout);

	int nCases;
	cin >> nCases;

	for (int cnt = 1; cnt <= nCases; cnt++) {
		cin >> num;
		cout << "Case #" << cnt << ": ";
		getResult();
		cout << endl;
	}

	return 0;
}