#include <algorithm>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

void solve()
{
	int D, N;
	cin >> D >> N;

	vector<int> K(N), S(N);

	for (int i = 0; i < N; ++i)
	{
		cin >> K[i] >> S[i];
	}

	double X = 0;

	for (int i = 0; i < N; ++i)
	{
		X = max(X, (double)(D - K[i]) / S[i]);
	}

	cout << fixed << setprecision(6) << D / X;
}

int main(int argc, char *argv[])
{
	int T;
	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
}