#include <iostream>
using namespace std;

void solve(int* arr, int k) {
	bool skip = false;
	for (int i = k - 2; i >= 0; i--) {
		if (arr[i] < arr[i + 1] && !skip) {
			skip = true;
			arr[i + 1]--;
			for (int j = i + 1; j < k; j++) {
				if (arr[j] < arr[j + 1]) {
					arr[j + 1]--;
					arr[j] = 9;
				}
				else {
					break;
				}
			}
		}
		if (skip) {
			arr[i] = 9;
		}
	}
}

int main() {
	int t, n;
	cin >> t;

	for (int i = 1; i <= t; i++) {
		cin >> n;
		int k = 0;
		int arr[19] = { 0 };
		while (n != 0) {
			arr[k] = n % 10;
			n /= 10;
			k++;
		}

		cout << "Case #" << i << ": ";
		solve(arr, k);
		int ans = 0;
		for (int j = k - 1; j >= 0; j--) {
			ans *= 10;
			ans += arr[j];
		}
		cout << ans << endl;
	}
}