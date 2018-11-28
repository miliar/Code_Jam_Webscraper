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

	int t;
	long long int n;
	long long int k;
	long long int intervals[2];
	long long int num[2];
	long long int intervalstmp[2];
	long long int numtmp[2];

	cin >> t;
	for (int run = 1; run <= t; run++)
	{
		cin >> n >> k;
		output << "Case #" << run << ": ";

		intervals[0] = n;
		intervals[1] = n;
		num[0] = 1;
		num[1] = 0;

		while (k > 0)
		{
			for (int i = 0; i < 2; i++)
			{
				numtmp[i] = 0;
			}

			for (int i = 0; i < 2; i++)
			{
				k -= num[i];

				if (k > 0)
				{
					if (intervals[i] % 2 == 0)
					{
						intervalstmp[0] = intervals[i]/2;
						intervalstmp[1] = intervalstmp[0] - 1;
						numtmp[0] += num[i];
						numtmp[1] += num[i];
					}
					else
					{
						intervalstmp[i] = (intervals[i] - 1)/2;
						numtmp[i] += 2*num[i];
					}
				}
				else
				{
					//The last person goes to a toilet with intervals[i] empty toilets.
					output << intervals[i]/2 << ' ' << (intervals[i] - 1)/2;
					break;
				}
			}

			for (int i = 0; i < 2; i++)
			{
				intervals[i] = intervalstmp[i];
				num[i] = numtmp[i];
			}
		}



		output << "\n";
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
