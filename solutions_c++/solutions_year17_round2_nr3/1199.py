#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <queue>
#include <iomanip>
#include <cassert>

using namespace std;

const int MAXN = 111;

long inp[MAXN][MAXN];
double f[MAXN][MAXN];
long E[MAXN];
long S[MAXN];
int N;

int main()
{
	int T;
	cin >> T;
	for (int casen = 1; casen <= T; ++casen) {
		int Q;
		cin >> N >> Q;
		for (int i = 0; i < N; ++i) {
			cin >> E[i] >> S[i];
		}
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				cin >> inp[i][j];
			}
		}
		int _, __;
		cin >> _ >> __;
		double d[MAXN];
		fill(d, d + N, numeric_limits<double>::infinity());
		d[0] = 0;
		for (int i = 0; i < N; ++i) {
			long long totalDist = 0;
			for (int j = i + 1; j < N; ++j) {
				assert(inp[j-1][j] >= 0);
				totalDist += inp[j - 1][j];
				if (E[i] >= totalDist) {
					d[j] = min(d[j], d[i] + static_cast<double>(totalDist)/S[i]);
				}
				else {
					break;
				}
			}
		}
		cout << "Case #" << casen << ": " << fixed << setprecision(6) << d[N - 1] << '\n';
	}

	return 0;
}

