#include<iostream>
using namespace std;

int main()
{
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C_small_1.out", "w", stdout);

	int T;
	cin >> T;

	for (int t=1; t<=T; ++t) {

		int N, K;
		cin >> N >> K;

		bool occ[N+2];
		memset(occ, false, sizeof occ);

		occ[0] = occ[N+1] = true;

		int mn, mx;

		int L[N+2], R[N+2];

		while (K--) {

			int l;
			for (int i=0; i<N+2; ++i) {
				if (occ[i]) {
					L[i] = -1;
					l = 0;
				}
				else {
					L[i] = l;
					++l;
				}
			}

			int r;
			for (int i=N+1; i>=0; --i) {
				if (occ[i]) {
					R[i] = -1;
					r = 0;
				}
				else {
					R[i] = r;
					++r;
				}
			}

			mn = -1;
			mx = -1;
			int p;

			for (int i=1; i<=N; ++i) {
				if (min(L[i], R[i]) > mn || (min(L[i], R[i]) == mn && max(L[i], R[i]) > mx)) {
					mn = min(L[i], R[i]);
					mx = max(L[i], R[i]);
					p = i;
				}
			}

			occ[p] = true;
		}

		cout << "Case #" << t << ": " << mx << " " << mn << endl;
	}

	return 0;
}