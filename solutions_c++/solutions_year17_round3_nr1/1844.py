#include <math.h>
#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <deque>
# define M_PIl          3.141592653589793238462643383279502884L /* pi */
using namespace std;


class pancake {
	public:
		pancake(){};
		pancake (int r, int h) {
			_r = r;
			_h = h;
			area = (long long)r * r;
			side = (long long)r * h * 2;
		}
		void print() {
			cout << _r << "," << _h << ":" << area << "," << side << endl;
		}
		bool operator > (const pancake& tmp) const {
			return tmp._r > _r;
		}
		bool operator < (const pancake& tmp) const {
			return tmp._r < _r;
		}
		int _r;
		int _h;
		long long area;
		long long side;
};

bool mycomp(pancake a, pancake b) {
	return a.side > b.side;
}
int main() {
	int ncase = 0;
	cin >> ncase;
	for (int round = 1; round <= ncase; ++round) {
		int n, k;
		cin >> n >> k;
		k = k - 1;

		vector<pancake> pancake_list;
		for (int i = 0; i < n; ++i) {
			int r, h;
			cin >> r >> h;
			pancake tmp(r, h);
			pancake_list.push_back(tmp);
		}

		sort(pancake_list.begin(), pancake_list.end());


		long long max_tot = 0;
		long long max_side = 0;
		deque<pancake> pend_list;
		pend_list.resize(k);
		long long side_list[n + 1];
		for(int i = 0; i < n + 1; ++i) {
			side_list[i] = 0;
		}

		if(k > 0){
			for (int i = 0; i < k; ++i) {
				int tar = n - 1 -i;
				pend_list[i] = pancake_list[tar];
				max_side += pancake_list[tar].side;
			}
			sort(pend_list.begin(), pend_list.end(), mycomp);
			side_list[n - k] = max_side;
			for(int i = n - 1- k; i > 0; --i) {
				if (pancake_list[i].side > pend_list[k - 1].side){
					max_side += pancake_list[i].side - pend_list[k - 1].side;
					pend_list[k - 1] = pancake_list[i];
					sort(pend_list.begin(), pend_list.end(), mycomp);
				}
				side_list[i] = max_side;
			}
		}

		/*
		for(int i = 0; i < n; ++i) {
			cout << side_list[i] << endl;
		}
		for(int i = 0; i < n; ++i) {
			pancake_list[i].print();
		}
		*/

		for(int i = 0; i < n - k; ++i) {
			long long tot;
			tot = pancake_list[i].area + side_list[i + 1] + pancake_list[i].side;
			if (tot > max_tot) {
				max_tot = tot;
			}
		}

		std::cout << std::fixed;
		std::cout << std::setprecision(10);

		cout << "Case #" << round << ": ";
		cout << (long double)max_tot * M_PIl;
		cout << endl;
	}
	return 0;
}
