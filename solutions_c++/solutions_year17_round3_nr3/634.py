#include <iostream>
#include <string>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <bitset>
#include <iomanip>
#include <cmath>
#include <queue>

# define M_PI           3.14159265358979323846

using namespace std;

typedef long long ll;
typedef pair<string, int> si;
typedef pair<int, int> ii;

const int CMAX = 1e5+10;
const double eps = 1e-7;

double Z[55];

int main() {
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif // _DEBUG
	ios::sync_with_stdio(false);

	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		int N, K;
		double U;

		cin >> N >> K >> U;

		double sum = 0;

		for (int i = 0; i < N; i++) {
			cin >> Z[i];
			sum += Z[i];
		}

		sum += U;

		sort(Z, Z + N);

		int cnt;

		for (int i = N - 1; i >= 0; i--) {
			if (sum / (i + 1) >= Z[i]) {
				cnt = i + 1;
				break;
			}
			else {
				sum -= Z[i];
			}
		}

		double prob = 1;

		for (int i = 0; i < cnt; i++) {
			Z[i] = sum / cnt;
			prob *= Z[i];
		}
		for (int i = cnt; i < N; i++) {
			prob *= Z[i];
		}

		cout << "Case #" << i + 1 << ": " << fixed << setprecision(9) << prob << endl;

	}

	return 0;
}