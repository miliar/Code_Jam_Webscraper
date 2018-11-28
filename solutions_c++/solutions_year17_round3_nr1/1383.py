#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

typedef pair<int, int> pii;
const double PI = 3.1415926535897932384626;

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		int N, K;
		cin >> N >> K;
		vector<pii> P(N);
		for(int i = 0; i < N; i++) {
			int R, H;
			cin >> R >> H;
			P[i] = make_pair(R, H);
		}
		sort(P.rbegin(), P.rend());
		double result = 0;
		for(int i = 0; i + K <= N; i++) {
			vector<double> V;
			for(int j = i + 1; j < N; j++)
				V.push_back(2 * PI * P[j].second * P[j].first);
			double temp = PI * P[i].first * P[i].first + 2 * PI * P[i].first * P[i].second;
			sort(V.rbegin(), V.rend());
			for(int j = 0; j + 1 < K; j++)
				temp += V[j];
			result = max(result, temp);
		}
		printf("Case #%d: %.10f\n", t, result);
	}
}
