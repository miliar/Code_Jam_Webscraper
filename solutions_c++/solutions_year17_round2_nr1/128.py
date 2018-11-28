#include<bits/stdc++.h>

using namespace std;

#define x first
#define y second
#define pb push_back
#define eb emplace_back

typedef long long ll;
typedef pair<int, int> pii;

const int maxn = 1000;

int D, N, K[maxn], S[maxn];

bool run(int tc)
{
	cin >> D >> N;
	for (int i = 0; i < N; i++) {
		cin >> K[i] >> S[i];
	}

	double ans = D;

	double maxT = 1e-10;
	for (int i = 0; i < N; i++) {
		maxT = max(maxT, 1.0 * (D - K[i]) / S[i]);
	}
	ans /= maxT;
	cerr << tc << ": " << maxT << endl;
	cout << "Case #" << tc << ": " << ans;
	cout << endl;
	return true;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	(cout << fixed).precision(10);

	int ntc;
	cin >> ntc;
	for (int i = 1; i <= ntc; i++) {
		if (!run(i)) {
			cerr << "Something went wrong" << endl;
		}
	}
	return 0;
}
