#include <array>
#include <cmath>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char** argv)
{
	if (argc < 2)
	{
		cout << "Not enough arguments" << endl;
		return EXIT_FAILURE;
	}
	ifstream file(argv[1]);
	if (!file.is_open())
	{
		cout << "Error: could not read file: " << argv[1] << endl;
		return EXIT_FAILURE;
	}

	int T;
	file >> T;

	string fileName = "output.txt";
	ofstream output(fileName, ios::out | ios::trunc);
	if (!output.is_open())
	{
		cout << "Error: could not write file: " << fileName.c_str() << endl;
		return EXIT_FAILURE;
	}
	for (int i = 0; i < T; i++)
	{
		string pancakesStr;
		file >> pancakesStr;
		vector<bool> pancakes(pancakesStr.length());
		vector<bool> goalFlip(pancakesStr.length());
		for (int i = 0; i < (int)pancakes.size(); i++)
			pancakes[i] = pancakesStr[i] == '+';
		int k;
		file >> k;
		bool goal = true;
		int nbFlips = 0;
		for (int i2 = 0; i2 < (int)pancakes.size() - k + 1; i2++)
		{
			if (pancakes[i2] != goal)
			{
				goal = !goal;
				goalFlip[i2 + k - 1] = !goalFlip[i2 + k - 1];
				nbFlips++;
			}
			goal = goal != goalFlip[i2];
		}
		bool gitGud = true;
		for (int i2 = (int)fmax(0, (int)pancakes.size() - k + 1); i2 < (int)pancakes.size() && gitGud; i2++)
		{
			gitGud &= pancakes[i2] == goal;
			goal = goal != goalFlip[i2];
		}
		output << "Case #" << i + 1 << ": ";
		if (gitGud)
			output << nbFlips;
		else
			output << "IMPOSSIBLE";
		output << endl;
	}
	output.close();
	file.close();
	cout << "Done\n";
	return EXIT_SUCCESS;
}