#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int t;
	cin >> t;

	for(int i = 0; i < t; i++)
	{
		long long unsigned int destination;
		int others_count;
		cin >> destination;
		cin >> others_count;

		long long unsigned int *distance = new long long unsigned int[others_count];
		long long unsigned int *speed = new long long unsigned int[others_count];

		for(int j = 0; j < others_count; j++)
		{
			cin >> distance[j];
			cin >> speed[j];
		}

		double maximum_time = 0;
		for(int j = 0; j < others_count; j++)
		{
			double time = double(destination - distance[j]) / double(speed[j]);
			if(time > maximum_time)
			{
				maximum_time = time;
			//	cout << "maximum_time = " << maximum_time << endl;
			}
		}

		double speed_annie = double(destination) / maximum_time;
		cout << "Case #" << (i + 1) << ": " << fixed << setprecision(6) << speed_annie << endl;

		delete[] speed;
		delete[] distance;
	}
	return 0;

}
