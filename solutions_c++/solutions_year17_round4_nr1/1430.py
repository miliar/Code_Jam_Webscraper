#include<iostream>
#include<vector>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	cin >> T;

	for (int t=1; t<=T; ++t) {

		cout << "Case #" << t << ": ";

		int N, P;
		cin >> N >> P;

		int G;

		vector<int> mod(P, 0);

		for (int i=0; i<N; ++i) {
			cin >> G;
			++mod[G%P];
		}

		int ans = mod[0];

		if (P == 2) {
			ans += (mod[1]/2);
			ans += (mod[1]%2);
		}
		else if (P == 3) {
			int g = min(mod[1], mod[2]);
			ans += g;
			
			mod[1] -= g;
			mod[2] -= g;

			ans += (mod[1]/3);
			ans += (mod[2]/3);

			ans += (mod[1]%3>0 ? 1 : 0);
			ans += (mod[2]%3>0 ? 1 : 0);
		}
		else if (P == 4) {
			ans += (mod[2]/2);

			int g = min(mod[1], mod[3]);
			ans += g;

			mod[1] -= g;
			mod[3] -= g;

			if (mod[2]%2 == 1 && mod[1]+mod[3] >= 2) {
				++ans;
				mod[1] -= 2;
			}
			else if (mod[2]%2 == 1) {
				++ans;
				if (mod[1]+mod[3] == 1) {
					--mod[1];
				}
			}

			ans += (mod[1]+mod[3]) / 4;

			ans += (((mod[1]+mod[3]) % 4 > 0) ? 1 : 0);
		}

		cout << ans << endl;
	}

	return 0;
}