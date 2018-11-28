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

		int Ac, Aj; cin >> Ac >> Aj;
		vector<pair<int, int>>CD(Ac),JK(Aj);
		vector<pair<pair<int, int>, int>>order;
		int AcSUM = 0, AjSUM = 0;
		for (int i = 0; i < Ac; i++) {
			cin >> CD[i].first >> CD[i].second;
			order.push_back(make_pair(CD[i], 1));
			AcSUM += CD[i].second - CD[i].first;
		}
		sort(CD.begin(), CD.end());
		for (int i = 0; i < Aj; i++) {
			cin >> JK[i].first >> JK[i].second;
			order.push_back(make_pair(JK[i], 2));
			AjSUM += JK[i].second - JK[i].first;
		}
		sort(JK.begin(), JK.end());

		sort(order.begin(), order.end());
		AjSUM = 720 - AjSUM;
		AcSUM = 720 - AcSUM;

		vector<int>C, J;
		int r = 0;
		for (int i = 1; i < Ac + Aj; i++) {
			if (order[i].second == 1 && order[i - 1].second == 1) {
				C.push_back(order[i].first.first - order[i - 1].first.second);
				r+=2;
			}
			else if (order[i].second == 2 && order[i - 1].second == 2) {
				J.push_back(order[i].first.first - order[i - 1].first.second);
				r+=2;
			}
			else r++;
		}
		if (order[0].second == 1 && order[order.size() - 1].second == 1) {
			C.push_back(order[0].first.first + (1440 - order[order.size() - 1].first.second));
			r+=2;
		}
		else if (order[0].second == 2 && order[order.size() - 1].second == 2) {
			J.push_back(order[0].first.first + (1440 - order[order.size() - 1].first.second));
			r+=2;
		}
		else r++;

		sort(C.begin(), C.end());
		sort(J.begin(), J.end());

		int s = 0;
		for (int i = 0; i < C.size(); i++) {
			if (AcSUM >= C[i]) {
				AcSUM -= C[i];
				s+=2;
			}
		}
		for (int i = 0; i < J.size(); i++) {
			if (AjSUM >= J[i]) {
				AjSUM -= J[i];
				s+=2;
			}
		}

		cout << r - s << endl;
	}
	return 0;
}

