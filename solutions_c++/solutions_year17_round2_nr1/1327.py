#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int t;
	in >> t;

	for (auto tcase = 1; tcase <= t; tcase++)
	{
		double d;
		int n;
		in >> d >> n;

		vector<double> horseTimes(n);

		for (auto i = 0; i < n; i++)
		{
			int k, s;
			in >> k >> s;

			horseTimes[i] = (d - k) / static_cast<double>(s);
		}

		auto min = *max_element(horseTimes.begin(), horseTimes.end());
		auto result = d / min;

		out << "Case #" << tcase << ": " <<
			fixed << setprecision(8) <<  result << endl;
	}
}