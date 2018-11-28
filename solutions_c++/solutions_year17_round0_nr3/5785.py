#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <assert.h>

using numT = int;

numT n;
numT * L;
numT * R;
numT * Min;
numT * Max;
bool * O;

void init() {
	for (int i = 0; i < n; ++i) {
		L[i] = (i - 1);
		R[i] = (n - 2 - i);

		O[i] = false;

		Min[i] = (L[i] < R[i]) ? L[i] : R[i];
		Max[i] = (L[i] > R[i]) ? L[i] : R[i];
	}

	O[0] = O[n - 1] = true;
}

void refresh(numT left, numT right) {
	for (int i = left; i <= right; ++i) {
		L[i] = (i - left);
		R[i] = (right - i);

		Min[i] = (L[i] < R[i]) ? L[i] : R[i];
		Max[i] = (L[i] > R[i]) ? L[i] : R[i];
	}
}

numT chooseBest(numT & min, numT & max) {
	std::vector<numT> candidates;
	numT max1 = -1;
	numT max2 = -1;
	numT min3 = 10000000;

	for (numT i = 0; i < n; ++i) {
		if (O[i])
			continue;

		if (Min[i] > max1) {
			max1 = Min[i];
			max2 = Max[i];
			min3 = i;
			candidates.clear();
			candidates.push_back(i);
		}
		else if (Min[i] == max1) {
			if (Max[i] == max2) {
				if (i == min3) {
					candidates.push_back(i);
				}
				else if (i < min3) {
					min3 = i;
					candidates.clear();
					candidates.push_back(i);
				}
			}
			else if (Max[i] > max2) {
				max2 = Max[i];
				min3 = i;
				candidates.clear();
				candidates.push_back(i);
			}
		}
	}

	assert(candidates.size() == 1);

	auto i = candidates[0];
	min = max1;
	max = max2;
	return i;
}

numT findLeftNotEmpty(numT index) {
	while (O[index] == false && index > 0)
		index--;

	return index;
}
numT findRightNotEmpty(numT index) {
	while (O[index] == false && index < n - 1)
		index++;

	return index;
}

void solve(numT N, numT K, numT & max, numT & min) {
	n = N + 2;
	L = new numT[N+2];
	R = new numT[N+2];
	Min = new numT[N + 2];
	Max = new numT[N + 2];
	O = new bool[N+2];

	init();

	numT left = 1;
	numT right = N;
	refresh(left, right);

	for (int i = 0; i < K; ++i) {
		auto c = chooseBest(min, max);
		left = findLeftNotEmpty(c - 1);
		numT leftLeft = findLeftNotEmpty(left - 1);

		right = findRightNotEmpty(c + 1);
		numT rightRight = findRightNotEmpty(right + 1);

		refresh(leftLeft + 1, left - 1);
		refresh(left + 1, c - 1);
		refresh(c+ 1, right - 1);
		refresh(right + 1, rightRight - 1);

		O[c] = true;
	}

	delete[] Min;
	delete[] Max;
	delete[] L;
	delete[] R;
	delete[] O;
}

int main(int argc, char ** args) {
	int testCount;
	std::istream & input = std::cin;
	input >> testCount;

	for (int i = 0; i < testCount; ++i) {
		numT N;
		numT K;

		input >> N;
		input >> K;

		numT max, min;
		solve(N, K, max, min);

		std::cout << "Case #" << i + 1 << ": " << max << " " << min << std::endl;
	}

}