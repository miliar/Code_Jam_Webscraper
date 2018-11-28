#include <algorithm>
#include <cstdio>
#include <vector>
using namespace std;
struct Pancake
{
	int radius;
	int height;
};

bool sortByRadius(const Pancake& lhs, const Pancake& rhs)
{
	return lhs.radius > rhs.radius;
}

struct Input
{
	int totalNumberOfPancakes;
	int sizeOfTheStack;
	vector<Pancake> pancakes;
};

Input getInput()
{
	Input result;
	scanf("%d %d", &result.totalNumberOfPancakes, &result.sizeOfTheStack);
	for (int pancakeNumber = 0; pancakeNumber < result.totalNumberOfPancakes; ++pancakeNumber)
	{
		Pancake pancake;
		scanf("%d %d", &pancake.radius, &pancake.height);

		result.pancakes.push_back(pancake);
	}

	return result;
};

class Solver
{
public:
	Solver(Input input)
	{
		this->input = input;
		sort(this->input.pancakes.begin(), this->input.pancakes.end(), sortByRadius);
	}

	long double solve()
	{
		long double result = 0;
		const long double pi = 3.141592653589793;
		for (int firstCake = 0; firstCake < input.pancakes.size() - input.sizeOfTheStack + 1; ++firstCake)
		{
			const long double r = input.pancakes[firstCake].radius;
			const long double h = input.pancakes[firstCake].height;
			long double currentResult = r*r + 2*r*h;
			vector<long double> areas;
			for (int i = firstCake + 1; i < input.pancakes.size(); ++i)
				areas.push_back(2.0 * (long double)input.pancakes[i].height * (long double)input.pancakes[i].radius);

			sort(areas.begin(), areas.end(), greater<long double>());
			for (int i = 0; i < input.sizeOfTheStack - 1; ++i)
				currentResult += areas[i];

			currentResult *= pi;
			result = max(result, currentResult);
		}

		return result;
	}
private:
	Input input;
};

int main()
{
	int testCases;
	scanf("%d", &testCases);
	for (int testNumber = 1; testNumber <= testCases; ++testNumber)
	{
		Solver solver(getInput());
		printf("Case #%d: %.6Lf\n", testNumber, solver.solve());
	}
	return 0;
}