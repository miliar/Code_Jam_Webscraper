
#include <iostream>
#include <iomanip>
#include <algorithm>

#include <math.h>

struct pancake {
	long long r, h;

	double top() {
		return M_PI * r * r;
	}

	double around() {
		return 2.0 * M_PI * r * h;
	}
};

bool by_radius(const pancake &a, const pancake &b) {
	return a.r > b.r || (a.r == b.r && a.h > b.h);
}

bool by_add_area(const pancake &a, const pancake &b) {
	return a.h * a.r > b.h * b.r;
}

int main() {
	int T;

	std::cin >> T;
	for (int t = 1; t <= T; t++) {
		std::cout << "Case #" << t << ": ";

		// do the magic...
		int N, K;

		std::cin >> N >> K;

		pancake cakes[N];
		for (int i = 0; i < N; i++) {
			std::cin >> cakes[i].r >> cakes[i].h;
		}

		std::sort(cakes, cakes + N, by_radius);
		//std::cout << "max: " << cakes[0].r << " " << cakes[0].h << std::endl;

		double max = -1;
		for (int i = 0; i <= N-K; i++) {
			pancake select[N-i];
			for (int j = 0; j < N-i; j++) select[j] = cakes[i+j];
			std::sort(select + 1, select + N-i, by_add_area);

			double area = select[0].top();
			for (int j = 0; j < K; j++) {
				area += select[j].around();
			}

			if (max < area) max = area;
			//std::cout << "area for #" << i << " (" << select[0].r << " " << select[0].h << "): " << area << std::endl;
		}

		std::cout << std::fixed << std::setprecision(7) << max << std::endl;
	}


	return 0;
}
