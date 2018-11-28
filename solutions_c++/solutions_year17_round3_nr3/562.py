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
		cout << "Case #" << t + 1 << ": ";
		/*
		int Ac, Aj; cin >> Ac >> Aj;
		vector<pair<int, int>>CD(Ac),JK(Aj);
		for (int i = 0; i < Ac; i++) {
			cin >> CD[i].first >> CD[i].second;
		}
		sort(CD.begin(), CD.end());
		for (int i = 0; i < Aj; i++) {
			cin >> JK[i].first >> JK[i].second;
		}
		sort(JK.begin(), JK.end());

		if (Ac == 1 && Aj == 1) {
			if (CD[0].second <= 720 && JK[0].first >= 720)cout << 2 << endl;
			else if (JK[0].second <= 720 && CD[0].first >= 720)cout << 2 << endl;
			else cout << 2 << endl;
		}
		else if (Ac == 2) {
			if (CD[1].second <= 720)cout << 2 << endl;
			else if (CD[0].first >= 720)cout << 2 << endl;
			else if (CD[1].second - CD[0].first <= 720)cout << 2 << endl;
			else if (CD[0].second + (1440 - CD[1].first) <= 720)cout << 2 << endl;
			else cout << 4 << endl;
		}
		else if (Aj == 2) {
			if (JK[1].second <= 720)cout << 2 << endl;
			else if (JK[0].first >= 720)cout << 2 << endl;
			else if (JK[1].second - JK[0].first <= 720)cout << 2 << endl;
			else if (JK[0].second + (1440 - JK[1].first) <= 720)cout << 2 << endl;
			else cout << 4 << endl;
		}
		else if (Ac == 1) {
			if (CD[0].first >= 720 || CD[0].second <= 720)cout << 2 << endl;
			else cout << 2 << endl;
		}
		else if (Aj == 1) {
			if (JK[0].first >= 720 || JK[0].second <= 720)cout << 2 << endl;
			else cout << 2 << endl;
		}
		*/

		int N, K; cin >> N >> K;
		double U; cin >> U;
		vector<double>P(N + 1);
		double sum = 0;
		for (int i = 0; i < N; i++) {
			cin >> P[i];
			sum += 1 - P[i];
		}
		P[N] = 1;
		sort(P.begin(), P.end());

		for (int i = 1; i < N + 1; i++) {
			if (P[i] != P[i - 1]) {
				double s = min(U / i, (P[i] - P[i - 1]));
				for (int j = 0; j < i; j++) {
					P[j] += s;
				}
				U -= i * s;
			}
		}

		double ans = 1;
		for (int i = 0; i < N; i++) {
			ans *= P[i];
		}
		cout << fixed << setprecision(7) << ans << endl;

	}
	return 0;
}

