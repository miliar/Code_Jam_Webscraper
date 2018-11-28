#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <list>
#include <vector>

constexpr long double PI_CONST = 3.141592653589793238462643383279502884L;

using namespace std;

using value_t = double;

struct pancake_t {
	value_t r;
	value_t h;

	constexpr long double upper_surface() const
	{
		return PI_CONST * r * r;
	}

	constexpr long double side_surface() const
	{
		return 2 * PI_CONST * r * h;
	}
};

class less_side_surface {
	constexpr bool operator()(const pancake_t& lhs, const pancake_t& rhs) const
	{
		return lhs.side_surface() < rhs.side_surface();
	}
};

long double solve(unsigned /*N*/, unsigned K, std::vector<pancake_t> pancakes, unsigned largest_pc_index)
{
	// Either we use the largest pancake at the bottom or we can replace that one with a better one.

	auto largest_pc = pancakes[largest_pc_index];
	pancakes[largest_pc_index] = pancakes.back();
	pancakes.pop_back();

	std::sort(pancakes.begin(), pancakes.end(), [](const pancake_t& lhs, const pancake_t& rhs) {
		return lhs.r * lhs.h > rhs.r * rhs.h;
	});

	size_t sl_pc_index = 0;
	value_t sl_pc_radius = 0;

	long double side_surface = 0;
	for (size_t i = 0; i < K - 1; ++i) {
		auto&& pancake = pancakes[i];

		if (pancake.r > sl_pc_radius) {
			sl_pc_radius = pancake.r;
			sl_pc_index = i;
		}

		side_surface += pancake.side_surface();
	}

	auto&& kth_pancake = pancakes[K - 1];

	if (kth_pancake.r > sl_pc_radius) {
		sl_pc_radius = kth_pancake.r;
		sl_pc_index = K - 1;
	}

	long double option_1 = largest_pc.upper_surface() + largest_pc.side_surface();
	long double option_2 = pancakes[sl_pc_index].upper_surface() + kth_pancake.side_surface();

	return side_surface + std::max(option_1, option_2);
}

int main(int argc, char *argv[])
{
	if (argc < 2) {
		std::cerr << "Need an input file" << std::endl;
	}
	else {
		std::fstream input;
		input.open(argv[1], std::fstream::in);

		if (!input.is_open())
			return -1;

		unsigned T;
		input >> T;

		for (unsigned t = 1; t <= T; ++t) {
			unsigned N, K;

			input >> N >> K;

			std::vector<pancake_t> pancakes;

			size_t largest_pc_index = 0;
			value_t largest_pc_height = 0;
			value_t largest_pc_radius = 0;

			for (size_t j = 0; j < N; ++j) {
				pancake_t pancake;

				input >> pancake.r >> pancake.h;

				if ((pancake.r > largest_pc_radius)
				 || ((pancake.r == largest_pc_radius) && (pancake.h > largest_pc_height))) {
					largest_pc_height = pancake.h;
					largest_pc_radius = pancake.r;
					largest_pc_index = j;
				}

				pancakes.push_back(std::move(pancake));
			}

			auto retval = solve(N, K, pancakes, largest_pc_index);

			std::cout << "Case #" << t << ": " << std::fixed << std::setprecision(9) << retval << std::endl;
		}
	}
	return 0;
}
