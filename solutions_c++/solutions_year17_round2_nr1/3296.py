#include <algorithm>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;

int main()
{
	int cases;
	cin >> cases;
	double d;
	int n;
	int i=0;
	cout << setprecision(numeric_limits<double>::digits10+1);
	while (cin >> d >> n)
	{
		++i;
		//std::vector<pair<double, double>> horses;
		double slowest_time = 0;
		std::vector<double> times;
		while (n--)
		{
			double pos,speed;
			cin >> pos >> speed;
			if (pos > d)
				continue;
			auto time = (d-pos)/speed;
			slowest_time = max(time, slowest_time);
			//times.push_back(time);
		}
		cout << "Case #" << i << ": ";
		//auto slowest_time = max_element(begin(times), end(times));
		//if (slowest_time != end(times))
		{
			cout << d/(slowest_time) << '\n';
		}
		/*
		for (auto h : horses)
		{
			auto time = (d-h.first)/h.second;
			cout << '\t' << time << '\n';
		}
		*/
	}
}
