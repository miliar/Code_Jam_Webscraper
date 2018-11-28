#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <iomanip>
using namespace std;

const int MAXN = 51;
int N, K;
double arr[MAXN];
double quota;

int main() {
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("c-small.out", "w", stdout);

	int nCases;
	cin >> nCases;
	cout << fixed << setprecision(8);

	for (int cnt = 1; cnt <= nCases; cnt++) {
		cin >> N >> K;
		cin >> quota;

		for (int i = 0; i < N; i++) {
			cin >> arr[i];
		}

		sort(arr, arr + N);
		arr[N] = 1.0;

		double used = 0.0;
		for (int i = 0; i < N; i++) {
			if (used + (i + 1) * (arr[i + 1] - arr[i]) <= quota) {
				used += (i + 1) * (arr[i + 1] - arr[i]);

				for (int k = 0; k <= i; k++) {
					arr[k] = arr[i + 1];
				}
			}
			else {
				for (int k = 0; k <= i; k++) {
					arr[k] += (quota - used) / (i + 1);
				}

				break;
			}
		}

		double result = 1.0;

		for (int i = 0; i < N; i++) {
			result *= arr[i];
		}

		cout << "Case #" << cnt << ": " << result << endl;
	}

	return 0;
}