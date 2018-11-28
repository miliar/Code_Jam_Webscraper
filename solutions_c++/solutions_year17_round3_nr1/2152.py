#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;

const double pi = 3.14159265358979323846264338327950288419716939937510582097494459230781640628;

struct Cake {
	unsigned long long R, H, RH, R2;
};

vector<Cake> cakes;
vector<bool> picked;
unsigned long long max_area = 0.0, area = 0.0;
int N;

void search_next(unsigned long long ubound, int cnt) {
	if (!cnt) {
		if (max_area < area) {
			max_area = area;
		}
		return;
	}
	unsigned long long area_backup = area;
	for (int i=0; i<N; ++i) {
		if (!picked[i] && cakes[i].R <= ubound) {
			picked[i] = true;
			area += 2 * cakes[i].RH;
			//cout << "pick #" << (i+1) << " area=" << area << endl;
			search_next(cakes[i].R, cnt-1);
			area = area_backup;
			picked[i] = false;
		}
	}
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; ++i) {
		max_area = 0.0;
		cakes.clear();
		picked.clear();
		int K;
		cin >> N >> K;
		for (int j=0; j<N; ++j) {
			Cake cake;
			cin >> cake.R >> cake.H;
			cake.RH = cake.R * cake.H;
			cake.R2 = cake.R * cake.R;
			cakes.push_back(cake);
			picked.push_back(false);
		}
		for (int j=0; j<N; ++j) {
			picked[j] = true;
			area = 2 * cakes[j].RH + cakes[j].R2;
			//cout << "base #" << (j+1) << " area=" << area << endl;
			if (K > 1) {
				search_next(cakes[j].R, K-1);
			}
			else {
				if (max_area < area) {
					max_area = area;
				}
			}
			picked[j] = false;
		}
		//cout << "Case #" << (i+1) << ": " << max_area << endl;
		printf("Case #%d: %.9f\n", i+1, (double) pi * max_area);
	}
}