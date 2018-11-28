/*
ID: paradoxes
PROG: Cruise Control
LANG: C++
*/

#include<iostream>
#include <iomanip>
#include<fstream>
#include<algorithm>

using namespace std;

int T;

double D, N;

double max_time_num, max_time_dem;

int main()
{
	ifstream Input("cruise.in");
	ofstream Output("cruise.out");

	Input >> T;

	double a, b;

	double answer;

	for (int j = 1; j <= T; j++)
	{
		Input >> D >> N;

		max_time_num = D;
		max_time_dem = 1;

		for (int i = 0; i < N; i++)
		{
			Input >> a >> b;

			if((D - a) / (double) b > (D - max_time_num) / (double) max_time_dem)
			{
				max_time_num = a;
				max_time_dem = b;
			}
		}

		answer = (D*max_time_dem) / (double)(D - max_time_num);

		if(answer > 0)
			Output << "Case #" << j << ": " << setprecision(8) << fixed << answer << endl;
		else
			Output << "Case #" << j << ": " << setprecision(8) << fixed << 0 << endl;
	}

	return 0;
}