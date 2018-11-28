#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


const bool OUTPUT_TO_FILE = true;


int main()
{
	cout.sync_with_stdio(false);
	stringstream output;

	double ans;
	int t;
	int d;
	int n;
	int k;
	double s;
	double time;
	double max_time;
	bool first_time;

	cin >> t;
	for (int run = 1; run <= t; run++)
	{
		cin >> d >> n;
		ans = 0;
		max_time = 0;
		first_time = true;

		for (int i = 0; i < n; i++)
		{
			cin >> k >> s;
			time = (d - k)/s;
			if (first_time || time > max_time)
			{
				max_time = time;
			}

			first_time = false;
		}

		ans = d/max_time;

		output.precision(30);
		output << "Case #" << run << ": " << ans << "\n";
//		cout << run << "\n";
	}

	if (OUTPUT_TO_FILE)
	{
		ofstream output_file;
		output_file.open("out.txt");
		output_file << output.rdbuf();
		output_file.close();
	}
	else
	{
		cout << output.rdbuf();
	}
}
