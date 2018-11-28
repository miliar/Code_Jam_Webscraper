#include <algorithm>
#include <climits>
#include <cmath>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <string.h>
#include <vector>
using namespace std;

int n; // # of ingredients
int p; // # of packages of each ingredient
int r[50]; // required for 1 serving
int a[50][50];

int calc_kits() {
	int j[50];
	for (int i = 0; i < n; i++)
		j[i] = 0;

	int kits = 0;
	for (int s = 1; s <= 1000000;) {

		bool can = true;
		for (int i = 0; i < n; i++) {
			int required = s * r[i];
			while (j[i] < p && a[i][j[i]] < 9 * required / 10.0)
				j[i]++;
			if (j[i] >= p)
				return kits;
			if (a[i][j[i]] > 11 * required / 10.0) {
				can = false;
				break;
			}
		}
		if (can) {
			kits++;
			for (int i = 0; i < n; i++)
				j[i]++;
		} else {
			s++;
		}
	}
	return kits;
}

int main() {
	int cases;
	cin >> cases;
	for (int case_counter = 1; case_counter <= cases; case_counter++) {

		cin >> n >> p;
		for (int i = 0; i < n; i++)
			cin >> r[i];
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < p; j++)
				cin >> a[i][j];
			sort(a[i], a[i] + p);
		}

		cout << "Case #" << case_counter << ": " << calc_kits() << endl;
	}
	return 0;
}
