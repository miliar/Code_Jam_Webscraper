#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

// R = 0, Y = 1, B = 2
std::string placementSmall(int prev, int R, int Y, int B) {

	if (R == 0 && Y == 0 && B == 0) {
		return "";
	}

	if (prev == 0) {
		if (Y > B) {
			return "Y" + placementSmall(1, R, Y - 1, B);
		}
		else {
			return "B" + placementSmall(2, R, Y, B - 1);
		}
	}
	else if (prev == 1) {
		if (B > R) {
			return "B" + placementSmall(2, R, Y, B - 1);
		}
		else {
			return "R" + placementSmall(0, R - 1, Y, B);
		}
	}
	else if (prev == 2) {
		if (R > Y) {
			return "R" + placementSmall(0, R - 1, Y, B);
		}
		else {
			return "Y" + placementSmall(1, R, Y - 1, B);
		}
	}
	else {

		auto Min = std::min(R, std::min(Y, B));
		auto Max = std::max(R, std::max(Y, B));

		if ((R >= Y && R <= B) || (R >= B && R <= Y)) {
			return "R" + placementSmall(0, R - 1, Y, B);
		}
		else if ((Y >= R && Y <= B) || (Y >= B && Y <= R)) {
			return "Y" + placementSmall(1, R, Y - 1, B);
		}
		else if ((B >= R && B <= Y) || (B >= Y && B <= R)) {
			return "B" + placementSmall(2, R, Y, B - 1);
		}
		else{
			return "";
		}
	}
}


void small(int c, int R, int Y, int B) {
	if (R > Y + B || Y > R + B || B > R + Y) {
		std::cout << "Case #" << c << ": IMPOSSIBLE\n";
	}
	else {
		auto res = placementSmall(-1, R, Y, B);
		std::cout << "Case #" << c << ": " << res << "\n";
	}
}

int main() {

	int t;
	std::cin >> t;

	for (auto c = 1; c <= t; c++) {
		
		int N, R, O, Y, G, B, V;
		std::cin >> N >> R >> O >> Y >> G >> B >> V;

		small(c, R, Y, B);	
	}

	getchar();
	return 0;
}