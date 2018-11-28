#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <math.h>

using namespace std;

const double PI = 3.14159265358979323846;
const double Epsilon = 1e-8;

struct panc
{
	double h;
	double r;

	double area() const
	{
		return PI * r * r + 2 * PI * r * h;
	}

	double sideArea() const
	{
		return 2 * PI * r * h;
	}
};

double solve(int last, int n, int k, const vector<panc>& pancackes, int level)
{
	if (level == k)
		return 0.0;

	auto maxArea = 0.0;

	for (auto i = last; i < min(n - k + last + 1, n); i++)
	{
		if (last != 0)
			maxArea = max(solve(i + 1, n, k, pancackes, level + 1) + pancackes[i].sideArea(), maxArea);
		else
			maxArea = max(solve(i + 1, n, k, pancackes, level + 1) + pancackes[i].area(), maxArea);
	}

	return maxArea;
}

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int t;
	in >> t;

	for (auto tcase = 1; tcase <= t; tcase++)
	{
		int n, k;
		in >> n >> k;

		vector<panc> pancackes(n);
		for (auto i = 0; i < n; i++)
			in >> pancackes[i].r >> pancackes[i].h;

		sort(pancackes.rbegin(), pancackes.rend(), [] (auto a, auto b)
		{
			return a.r < b.r;
		});
		
		auto maxArea = solve(0, n, k, pancackes, 0);

		out << "Case #" << tcase << ": " <<
			fixed << setprecision(8) << maxArea << endl;
	}
}