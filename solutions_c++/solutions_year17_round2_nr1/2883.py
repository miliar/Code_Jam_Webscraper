#include <algorithm>
#include <iomanip>
#include <fstream>
#include <iostream>
#include <memory>
#include <vector>

struct Horse
{
	int k, s;
};

double getSolution(int d, int n, std::vector<Horse>& horses)
{
	double max_time = 0;

	for (auto& horse : horses)
	{
		double horse_time = (d - horse.k) / static_cast<double>(horse.s);
		max_time = std::max(max_time, horse_time);
	}

	return d / max_time;
}

int main()
{
	std::ifstream input("D:\\inputa.txt");
	std::ofstream output("D:\\outputa.txt");

	int t;
	input >> t;

	for (int i = 0; i < t; ++i)
	{
		int d, n;
		input >> d >> n;

		std::vector<Horse> horses;

		for (int j = 0; j < n; ++j)
		{
			int k, s;
			input >> k >> s;
			horses.push_back(Horse{ k, s });
		}

		double result = getSolution(d, n, horses);
		output << "Case #" << i + 1 << ": " << std::fixed << std::setprecision(6) << result << std::endl;
	}
}