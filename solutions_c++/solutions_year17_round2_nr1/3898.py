#include <iostream>
#include <iomanip>

using namespace std;

#define MAX_HORSE 10000

int start[MAX_HORSE];
int speed[MAX_HORSE];

int main()
{
	int n_case;
	cin >> n_case;
	for (int z = 1; z <= n_case; ++z)
	{
		int dest, n_horse;
		cin >> dest >> n_horse;
		double max_time = 0;
		for (int i = 0; i < n_horse; ++i)
		{
			cin >> start[i] >> speed[i];
			double cur_time = (double)(dest - start[i]) / speed[i];
			max_time = cur_time > max_time ? cur_time : max_time;
		}

		cout << "Case #" << z << ": " << fixed << setprecision(6) << dest / max_time << endl;
	}
}