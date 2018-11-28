#include <iostream>
#include <fstream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
	ifstream in("input.txt");

	size_t T;

	in >> T;

	ofstream out("output.txt");

	for (int z = 1; z <= T; ++z)
	{
		double D, N;
		in >> D >> N;

		cout << z << endl;

		vector<pair<double, double>> horses(N);
		for (auto& p : horses)
			in >> p.first >> p.second;

		sort(horses.begin(), horses.end());

		double l = .0, r = 1e20;

		for (int k = 0; k < 400; ++k)
		{
			double mid = (l + r) / 2.0;

			double t = D / mid;

			bool finished = true;

			for (int i = horses.size() - 1; i >= 0; --i)
				if (horses[i].first + t*horses[i].second < D)
				{
					finished = false;
					break;
				}

			if (finished)
				l = mid;
			else
				r = mid;
		}

		out << "Case #" << z << ": " << fixed << setprecision(9) << (l + r) / 2.0 << "\n";
	}
}