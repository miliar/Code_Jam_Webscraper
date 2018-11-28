#include <iostream>
#include <map>
#include <iomanip>

using namespace std;

float maxSpeed(double dist, map<double, double> hourses)
{
	double maxTime = 0, time = 0;
	for (auto elem : hourses)
	{
		time = (dist - elem.first) / elem.second;
		if (time > maxTime)
			maxTime = time;
	}

	return dist / maxTime;
}

void main()
{
	int T;
	cin >> T;

	for (int i = 0; i < T; ++i)
	{
		double dist = 0, countOther = 0;
		cin >> dist >> countOther;
		map<double, double> hourses;
		int point = 0;
		int speed = 0;

		for (int i = 0; i < countOther; i++)
		{
			cin >> point >> speed;
			hourses[point] = speed;
		}

		cout << "Case #" << i + 1 << ": ";
		cout << fixed << scientific << maxSpeed(dist, hourses) << "\n";
	}
}

