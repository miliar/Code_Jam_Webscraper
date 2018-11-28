#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<int, int> PII;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

int T;
double D, N;
vector<double> K, S;

double solve() {
	double result = (D - K[0]) / S[0];
	for (int j = 1; j < N; j ++)
		result = max(result, (D - K[j]) / S[j]);
	return (D/result);
}

int main() {
	cin >> T;
	for (int i = 0; i < T; i ++) {
		cin >> D >> N;
		K.clear();
		S.clear();
		double tmp;
		for (int j = 0; j < N; j ++) {
			cin >> tmp;
			K.pb(tmp);
			cin >> tmp;
			S.pb(tmp);
		}
		printf("Case #%d: %.7f\n", i+1, solve());
	}
	return 0;
}
