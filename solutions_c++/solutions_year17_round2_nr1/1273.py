#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <queue>
#include <iomanip>

using namespace std;

int main()
{
	int T, casen;
	cin >> T;
	for (int casen = 1; casen <= T; ++casen) {
		int D, N;
		cin >> D >> N;
		double latest = -1;
		for (int i = 0; i < N; ++i) {
			int K, S;
			cin >> K >> S;
			double reaches_at = static_cast<double>(D - K) / S;
			latest = max(reaches_at, latest);
		}
		cout << "Case #" << casen << ": " << fixed << setprecision(7) << (D / latest) << '\n';
	}

	return 0;
}

