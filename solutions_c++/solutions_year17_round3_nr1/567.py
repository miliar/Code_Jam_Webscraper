#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>
using namespace std;
typedef long long ll;
#define PI 3.14159265358979323846

struct PAN {
	double R, H;

	bool operator<(const PAN& right)const {
		if (right.R*right.H > R*H)return true;
		else if (right.R*right.H < R*H)return false;
		else {
			if (right.R > R)return true;
			else return false;
		}
	}
};

int main()
{
	int T; cin >> T;
	for (int t = 0; t < T; t++) {
		int N, K; cin >> N >> K;

		vector<PAN>pan(N);
		for (int i = 0; i < N; i++) {
			cin >> pan[i].R >> pan[i].H;
		}
		sort(pan.begin(), pan.end());
		reverse(pan.begin(), pan.end());


		double ans = 0;
		double maxR = 0;
		for (int i = 0; i < K - 1; i++) {
			ans += 2 * PI*pan[i].H*pan[i].R;
			maxR = max(maxR, pan[i].R);
		}

		double maxA = 0;
		for (int i = K - 1; i < N; i++) {
			double A = 2 * PI*pan[i].R*pan[i].H;
			if (maxR < pan[i].R) {
				A += pan[i].R*pan[i].R*PI;
			}
			else {
				A += maxR*maxR*PI;
			}

			maxA = max(maxA, A);
		}

		cout << "Case #" << t + 1 << ": ";
		cout << fixed << setprecision(9) << ans + maxA << endl;
	}
	return 0;
}

