
#include <iostream>

struct acti {
	int s, e;
};

bool oneblock(const acti &a1, const acti &a2) {
	//std::cout << std::endl << "oneblock of " << a1.s << " -  " << a1.e << " vs " << a2.s << " - " << a2.e;

	if (a1.s > a2.s) return oneblock(a2, a1);

	//std::cout << std::endl << "base variant: " << (a1.s + 720 <= a2.e) << " alternative: " << (a2.s + 720 <= a1.e + 1440);

	return (a1.s + 720 >= a2.e) || (a2.s + 720 >= a1.e + 1440);
}

int main() {
	int T;

	std::cin >> T;
	for (int t = 1; t <= T; t++) {
		int AC, AJ;

		std::cin >> AC >> AJ;

		acti C[AC], J[AJ];
		for (int i = 0; i < AC; i++) std::cin >> C[i].s >> C[i].e;
		for (int i = 0; i < AJ; i++) std::cin >> J[i].s >> J[i].e;

		int x;
		if (AC <= 1 && AJ <= 1) {
			x = 2;
		} else {
			if (AC == 2) {
				//std::cout << "interesting one: " << C[0].s << " " C[0].e << " " << C[1].s << " " << C[1].e << std::endl;
				x = oneblock(C[0], C[1]) ? 2 : 4;
			} else {
				//std::cout << "interesting one: " << C[0].s << " " C[0].e << " " << C[1].s << " " << C[1].e << std::endl;
				x = oneblock(J[0], J[1]) ? 2 : 4;
			}
		}

		std::cout << "Case #" << t << ": " << x << std::endl;
	}


	return 0;
}
