#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int T; cin >> T;
	for(int x = 1; x <= T; ++x)
	{
		int D, N; cin >> D >> N;

		double h = 0;
		for(int i = 0; i < N; ++i) {
			int K, S; cin >> K >> S;
			h = max(h, double(D - K)/S);
		}

		cout << "Case #" << x << ": " << fixed << setprecision(6) << D/h << endl;
	}
}