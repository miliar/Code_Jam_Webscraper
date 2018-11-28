#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;

struct Pancake {
	int radius, height;
};

class ComparePancakeByRadius {
public:
	bool operator() (Pancake lhs, Pancake rhs) {
		return lhs.radius < rhs.radius;
	}
} comparePancakeByRadius;

class ComparePancakeByHeight {
public:
	bool operator() (Pancake lhs, Pancake rhs) {
		return lhs.height < rhs.height;
	}
};

int main(int argc, char const *argv[]) {
	int T;
	cin >> T;
	for (int caseNum = 1; caseNum <= T; caseNum++) {
		int K, N;
		cin >> N >> K;
		vector<Pancake> selectedPancakes;
		long currentMaxRadius = 0;
		double currentAnswer = 0;
		for (int i = 0; i < N; i++) {
			long R, H;
			cin >> R >> H;
			if (selectedPancakes.size() < K) {
				Pancake pancake;
				pancake.radius = R;
				pancake.height = H;
				selectedPancakes.push_back(pancake);
				if (R <= currentMaxRadius) {
					currentAnswer += 2 * 1.0 * R * H;
				} else {
					currentAnswer += 2 * 1.0 * R * H + 1.0 * (R * R - currentMaxRadius * currentMaxRadius);
					currentMaxRadius = R;
				}
				// cout << "Selecting pancake [" << i << "]" << endl;
			} else {
				// exchange with one of the existing
				if (R > currentMaxRadius) {
					int replacing = -1;
					double increase = 0;
					for (int j = 0; j < selectedPancakes.size(); j++) {
						Pancake pancake = selectedPancakes[j];
						double localIncrease = -2 * 1.0 * pancake.radius * pancake.height + 2 * 1.0 * R * H + 1.0 * (R * R - currentMaxRadius * currentMaxRadius);
						if (localIncrease > increase) {
							// cout << "localIncrease > increase" << endl;
							// cout << localIncrease << " > " << increase << endl;
							increase = localIncrease;
							replacing = j;
						}
					}
					if (replacing != -1) {
						Pancake newPancake;
						newPancake.radius = R;
						newPancake.height = H;
						selectedPancakes[replacing] = newPancake;
						currentAnswer += increase;
						// cout << "Larger: Selecting pancake [" << i << "] replacing [" << replacing << "]" << endl;
					}
				} else {
					int replacing = -1;
					int startOfLargest = -1;
					double increase = 0;
					for (int j = 0; j < selectedPancakes.size(); j++) {
						Pancake pancake = selectedPancakes[j];
						if (pancake.radius == currentMaxRadius) {
							startOfLargest = j;
							break;
						}
						double localIncrease = -2 * 1.0 * pancake.radius * pancake.height + 2 * 1.0 * R * H + 1.0;
						if (localIncrease > increase) {
							// cout << "localIncrease > increase" << endl;
							// cout << localIncrease << " > " << increase << endl;
							increase = localIncrease;
							replacing = j;
						}
					}
					if (startOfLargest != selectedPancakes.size() - 1) {
						for (int j = startOfLargest; j < selectedPancakes.size(); j++) {
							Pancake pancake = selectedPancakes[j];
							double localIncrease = -2 * 1.0 * pancake.radius * pancake.height + 2 * 1.0 * R * H;
							if (localIncrease > increase) {
								// cout << "localIncrease > increase" << endl;
								// cout << localIncrease << " > " << increase << endl;
								increase = localIncrease;
								replacing = j;
							}
						}
					} else {
						// find the 2nd largest
						Pancake pancake = selectedPancakes[startOfLargest];
						double localIncrease = -2 * 1.0 * pancake.radius * pancake.height + 2 * 1.0 * R * H - 1.0 * pancake.radius * pancake.radius;
						Pancake secondLargestPancake = selectedPancakes[startOfLargest - 1];
						if (secondLargestPancake.radius > R) {
							localIncrease += 1.0 * secondLargestPancake.radius * secondLargestPancake.radius;
						} else {
							localIncrease += 1.0 * R * R;
						}
						if (localIncrease > increase) {
							increase = localIncrease;
							replacing = startOfLargest;
						}
					}
					if (replacing != -1) {
						Pancake newPancake;
						newPancake.radius = R;
						newPancake.height = H;
						selectedPancakes[replacing] = newPancake;
						currentAnswer += increase;
						// cout << "Smaller: Selecting pancake [" << i << "] replacing [" << replacing << "]" << endl;
					}
				}
			}
			sort(selectedPancakes.begin(), selectedPancakes.end(), comparePancakeByRadius);
			currentMaxRadius = selectedPancakes.back().radius;
			// cout << "currentMaxRadius: " << currentMaxRadius << endl;
		}
		cout << "Case #" << caseNum << ": " << setiosflags(ios::fixed) << setprecision(6) << M_PI * currentAnswer << endl;
	}
	return 0;
}