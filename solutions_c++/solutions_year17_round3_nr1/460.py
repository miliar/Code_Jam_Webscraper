#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;

const double PI = acos(-1.0);
const int MAXN = 1001;

int N, K;

struct Pancake {
	int r, h;
	double area_around;
} pancakes[MAXN];

bool comp(Pancake p1, Pancake p2) {
	return p1.area_around > p2.area_around;
}

double getLargest(int x) {
	int count = 1;
	double curr = PI * pancakes[x].r * pancakes[x].r + pancakes[x].area_around;

	for (int i = 0; i < N; i++) {
		if (count == K) {
			return curr;
		}

		if (i != x && pancakes[i].r <= pancakes[x].r) {
			curr += pancakes[i].area_around;
			count++;			
		}

		if (count == K) {
			return curr;
		}
	}

	return 0.0;
}

double getResult() {
	double result = 0.0;

	for (int i = 0; i < N; i++) {
		result = max(result, getLargest(i));
	}

	return result;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);

	int nCases;
	cin >> nCases;

	cout << fixed << setprecision(8);

	for (int cnt = 1; cnt <= nCases; cnt++) {
		cin >> N >> K;

		for (int i = 0; i < N; i++) {
			cin >> pancakes[i].r >> pancakes[i].h;
			pancakes[i].area_around = 2 * PI * pancakes[i].r * pancakes[i].h;
		}

		sort(pancakes, pancakes + N, comp);

		cout << "Case #" << cnt << ": " << getResult() << endl;
	}

	return 0;
}