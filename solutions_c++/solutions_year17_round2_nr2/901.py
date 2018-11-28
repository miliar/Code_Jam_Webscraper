#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


stringstream output;

int ans;
int t;
int n;
bool answered;
int colors[3];
int colors2[3];
vector<string> colorsN = {"R", "Y", "B"};
vector<string> colorsN2 = {"G", "V", "O"};
int biggest[3];
bool first[3];


void printPart(int k)
{
	if (first[k])
	{
		for (int i = 0; i < colors2[k]; i++)
		{
			output << colorsN[k] + colorsN2[k];
		}

		output << colorsN[k];

		first[k] = false;
	}
	else
	{
		output << colorsN[k];
	}
}



const bool OUTPUT_TO_FILE = true;


int main()
{
	cout.sync_with_stdio(false);


	cin >> t;
	for (int run = 1; run <= t; run++)
	{
		cin >> n >> colors[0] >> colors2[2] >> colors[1] >> colors2[0] >> colors[2] >> colors2[1];

		output << "Case #" << run << ": ";

		first[0] = true;
		first[1] = true;
		first[2] = true;

		answered = false;
		for (int i = 0; i < 3; i++)
		{
			if (colors[(i + 1) % 3] == 0 && colors[(i + 2) % 3] == 0 && colors2[(i + 1) % 3] == 0 && colors2[(i + 2) % 3] == 0)
			{
				if (colors[i] == colors2[i])
				{
					for (int j = 0; j < colors[i]; j++)
					{
						output << colorsN[i] + colorsN2[i];
					}
				}
				else
				{
					output << "IMPOSSIBLE";
				}

				output << "\n";

				answered = true;
				break;
			}
			else if (colors[i] <= colors2[i] && colors2[i] > 0)
			{
				output << "IMPOSSIBLE";

				output << "\n";

				answered = true;
				break;
			}
		}

		if (answered)
		{
			continue;
		}

		for (int i = 0; i < 3; i++)
		{
			colors[i] -= colors2[i];
		}

		if (colors[0] >= colors[1] && colors[1] >= colors[2])
		{
			biggest[0] = 0;
			biggest[1] = 1;
			biggest[2] = 2;
		}

		if (colors[0] >= colors[2] && colors[2] >= colors[1])
		{
			biggest[0] = 0;
			biggest[1] = 2;
			biggest[2] = 1;
		}

		if (colors[1] >= colors[0] && colors[0] >= colors[2])
		{
			biggest[0] = 1;
			biggest[1] = 0;
			biggest[2] = 2;
		}

		if (colors[1] >= colors[2] && colors[2] >= colors[0])
		{
			biggest[0] = 1;
			biggest[1] = 2;
			biggest[2] = 0;
		}

		if (colors[2] >= colors[0] && colors[0] >= colors[1])
		{
			biggest[0] = 2;
			biggest[1] = 0;
			biggest[2] = 1;
		}

		if (colors[2] >= colors[1] && colors[1] >= colors[0])
		{
			biggest[0] = 2;
			biggest[1] = 1;
			biggest[2] = 0;
		}


		if (colors[biggest[0]] > colors[biggest[1]] + colors[biggest[2]])
		{
			output << "IMPOSSIBLE";

			output << "\n";
			continue;
		}


		while (colors[0] + colors[1] + colors[2] > 0)
		{
			if (colors[0] == colors[1] && colors[1] == colors[2])
			{
				printPart(biggest[0]);
				printPart(biggest[1]);
				printPart(biggest[2]);
				colors[0]--;
				colors[1]--;
				colors[2]--;
			}
			else
			{
				printPart(biggest[0]);
				printPart(biggest[1]);
				colors[biggest[0]]--;
				colors[biggest[1]]--;

				if (colors[biggest[0]] != colors[biggest[1]])
				{
					printPart(biggest[0]);
					printPart(biggest[2]);
					colors[biggest[0]]--;
					colors[biggest[2]]--;
				}
			}
		}

		output << "\n";


//		output << "Case #" << run << ": " << ans << "\n";
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
