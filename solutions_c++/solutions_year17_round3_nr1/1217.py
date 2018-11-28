#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;

const int T = 100;
const int N = 1000;
const int K = 1000;

class Pancake {

public:

	int r, h;
	double sideArea;
	double topArea;
	double totalSideArea;//
	double rangeSideArea;//
	double rangeMaxTopArea;//
	
	Pancake() : Pancake(0, 0) {}
	Pancake(int r, int h) {

		setDimenstions(r, h);

	}

	void setDimenstions(int r, int h) {

		this->r = r;
		this->h = h;
		sideArea = 2 * M_PI * r * h;
		topArea = M_PI * r * r;
		totalSideArea = 0;
		rangeSideArea = 0;
		rangeMaxTopArea = 0;

	}

	friend bool operator<(const Pancake& p1, const Pancake& p2) {
		
		return p1.sideArea > p2.sideArea;

	}

};

Pancake pancake[N];

int main() {

	int t;
	cin >> t;

	for (int caseNo = 1; caseNo <= t; caseNo++) {

		int n, k;
		cin >> n >> k;

		for (int i = 0; i < n; i++) {
			int r, h;
			cin >> r >> h;
			pancake[i].setDimenstions(r, h);
		}

		sort(pancake, pancake + n);

		double maxTopArea = 0;
		for (int i = 0; i < k; i++) {
			maxTopArea = max(maxTopArea, pancake[i].topArea);
		}

		int lastChoice = k - 1;
		for (int i = k; i < n; i++) {
			if (pancake[i].topArea + pancake[i].sideArea > maxTopArea + pancake[lastChoice].sideArea) {
				maxTopArea = pancake[i].topArea;
				lastChoice = i;
			}
		}

		double maxArea = 0;
		for (int i = 0; i < k - 1; i++) {
			maxArea += pancake[i].sideArea;
		}
		maxArea += pancake[lastChoice].sideArea;
		maxArea += maxTopArea;

		cout << "Case #" << caseNo << ": " << setprecision(9) << fixed << maxArea << endl;

		/*pancake[0].totalSideArea = pancake[0].sideArea;
		for (int i = 1; i < n; i++) {
			pancake[i].totalSideArea = pancake[i - 1].totalSideArea + pancake[i].sideArea;
		}*/

		/*pancake[k - 1].rangeSideArea = pancake[k - 1].totalSideArea;
		for (int i = k + 1; i <= n; i++) {
			pancake[i - 1].rangeSideArea = pancake[i - 1].totalSideArea - pancake[i - k - 1].totalSideArea;
			for (j = i - k; j < k; j++) {
				pancake[i - 1].rangeMaxTopArea = max(pancake[i - 1].rangeMaxTopArea, pancake[j].topArea);
			}
		}*/

	}
}