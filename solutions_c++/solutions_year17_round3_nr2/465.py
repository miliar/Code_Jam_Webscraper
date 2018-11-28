#include <iostream>
#include <algorithm>
#include <vector>
#include <climits>
using namespace std;

const int MAXN = 201;

struct Shift {
	int s, t;
	int owner;
} shifts[MAXN];

int X, Y;

bool comp(Shift s1, Shift s2) {
	return s1.s < s2.s;
}

int getResult() {
	int t[2] = { 0, 0 }, t_free = 0;
	t[shifts[0].owner] += shifts[0].t - shifts[0].s;

	//t[shifts[0].owner] += shifts[0].t;
	//t[shifts[X + Y - 1].owner] += 1440 - shifts[X + Y - 1].t;
	int result = 0;

	for (int i = 1; i < X + Y; i++) {
		if (shifts[i].owner == shifts[i - 1].owner) {
			t[shifts[i].owner] += shifts[i].s - shifts[i - 1].t;
		}
		else {
			t_free += shifts[i].s - shifts[i - 1].t;
			result++;
		}

		t[shifts[i].owner] += shifts[i].t - shifts[i].s;
	}

	if (shifts[0].owner == shifts[X + Y - 1].owner) {
		t[shifts[0].owner] += 1440 - shifts[X + Y - 1].t + shifts[0].s;
	}
	else {
		t_free += 1440 - shifts[X + Y - 1].t + shifts[0].s;
		result++;
	}

	int ind_small, ind_large;
	if (t[0] <= t[1]) {
		ind_small = 0;
		ind_large = 1;
	}
	else {
		ind_small = 1;
		ind_large = 0;
	}

	t[ind_small] += t_free;
	if (t[ind_small] >= 720) {
		return result;
	}

	vector<int> arr;
	for (int i = 0; i + 1 < X + Y; i++) {
		if (shifts[i].owner == ind_large && shifts[i + 1].owner == ind_large) {
			arr.push_back(shifts[i + 1].s - shifts[i].t);
		}
	}

	if (shifts[0].owner == ind_large && shifts[X + Y - 1].owner == ind_large) {
		arr.push_back(1440 - shifts[X + Y - 1].t + shifts[0].s);
	}

	sort(arr.begin(), arr.end());
	reverse(arr.begin(), arr.end());

	// Without any end
	//int final_result = INT_MAX;
	int result1 = result;
	int temp = t[ind_small];
	for (int i = 0; i < arr.size(); i++) {
		temp += arr[i];
		result1 += 2;

		if (temp >= 720) {
			break;
		}
	}

	return result1;

	/*
	if (temp >= 720) {
		final_result = min(final_result, result1);
	}
	*/

	/*
	// Left end
	if (shifts[0].owner == ind_large) {
		result1 = result + 1;
		temp = t[ind_small] + shifts[0].s;

		for (int i = 0; i < arr.size(); i++) {
			temp += arr[i];
			result1 += 2;

			if (temp >= 720) {
				break;
			}
		}
		if (temp >= 720) {
			final_result = min(final_result, result1);
		}
	}

	// Right end
	if (shifts[X + Y - 1].owner == ind_large) {
		result1 = result + 1;
		temp = t[ind_small] + 1440 - shifts[X + Y - 1].t;

		for (int i = 0; i < arr.size(); i++) {
			temp += arr[i];
			result1 += 2;

			if (temp >= 720) {
				break;
			}
		}
		if (temp >= 720) {
			final_result = min(final_result, result1);
		}
	}

	// Both ends
	if (shifts[0].owner == ind_large && shifts[X + Y - 1].owner == ind_large) {
		result1 = result + 2;
		temp = t[ind_small] + 1440 - shifts[X + Y - 1].t + shifts[0].s;

		for (int i = 0; i < arr.size(); i++) {
			temp += arr[i];
			result1 += 2;

			if (temp >= 720) {
				break;
			}
		}
		if (temp >= 720) {
			final_result = min(final_result, result1);
		}
	}
	*/

	//return final_result;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("b-large.out", "w", stdout);

	int nCases;
	cin >> nCases;

	for (int cnt = 1; cnt <= nCases; cnt++) {
		cin >> X >> Y;

		for (int i = 0; i < X + Y; i++) {
			cin >> shifts[i].s >> shifts[i].t;
			if (i < X) {
				shifts[i].owner = 0;
			}
			else {
				shifts[i].owner = 1;
			}
		}

		sort(shifts, shifts + X + Y, comp);

		cout << "Case #" << cnt << ": " << getResult() << endl;
	}

	return 0;
}