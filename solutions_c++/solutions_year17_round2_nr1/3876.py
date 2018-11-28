#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;

struct Pony
{
	double k;
	double s;
	bool operator<(const Pony& o) { return k > o.k; }
};

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t<=T; ++t)
	{
		double D;
		int N;
		cin >> D;
		cin >> N;

		std::vector<Pony> ponies;
		ponies.resize(N);
		for (int i = 0; i < N; ++i)
		{
			cin >> ponies[i].k;
			cin >> ponies[i].s;
		}
		std::sort(ponies.begin(), ponies.end());

		cout << "Case #" << t << ": ";

		double tmax = 0.f;
		for (int i = 0; i < N; ++i)
		{
			double t1 = (D - ponies[i].k) / ponies[i].s;  // celbaeresi ido
			if (t1 > tmax)
				tmax = t1;
		}

		double speed = D / tmax;
		cout << std::fixed << std::setprecision(6) << speed << endl;
	}

	return 0;
}