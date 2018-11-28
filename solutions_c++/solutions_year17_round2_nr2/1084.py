
#include <iostream>

struct rename {
	int a, b, c;
	char aN;
	char bN;
	char cN;

	void choose(char c1, char c2, int n1, int n2) {
		if (n1 >= n2) {
			bN = c1;
			b = n1;
			cN = c2;
			c = n2;
		} else {
			bN = c2;
			b = n2;
			cN = c1;
			c = n1;
		}
	}

	rename(int R, int Y, int B) {
		if (R >= Y && R >= B) {
			aN = 'R';
			a = R;
			choose('Y', 'B', Y, B);
		} else if (Y >= R && Y >= B) {
			aN = 'Y';
			a = Y;
			choose('R', 'B', R, B);
		} else {
			aN = 'B';
			a = B;
			choose('R', 'Y', R, Y);
		}
	}
};

int main() {
	
	int T;
	std::cin >> T;
	
	for (int t = 1; t <= T; t++) {
		std::cout << "Case #" << t << ": ";

		int N, R, O, Y, G, B, V;
		std::cin >> N >> R >> O >> Y >> G >> B >> V;

		rename x(R, Y, B);

		bool done = false;
		std::string r = "";

		while (x.a > 0 && !done) {
			if (x.a > x.b + x.c) {
				r = "IMPOSSIBLE";
				done = true;
				break;
			}

			if (x.a < x.b + x.c) {
				if (x.c > 0) {
					r += x.aN;
					r += x.bN;
					r += x.cN;
					x.a--;
					x.b--;
					x.c--;
				} else {
					r = "IMPOSSIBLE";
					done = true;
					break;
				}
			} else {
				while (x.c > 0) {
					r += x.aN;
					r += x.cN;
					x.a--;
					x.c--;
				}
				while (x.b > 0) {
					r += x.aN;
					r += x.bN;
					x.a--;
					x.b--;
				}
			}
		}

		std::cout << r << std::endl;

	}

	return 0;
}
