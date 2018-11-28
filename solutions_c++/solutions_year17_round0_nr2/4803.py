#include <fstream>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <queue>
#include <cstdint>
#include <unordered_map>
#include <map>
#include <unordered_set>
#include <functional>

using namespace std;
typedef long long ll;

int main()
{
	string fileName = "input.txt";
	ifstream file(fileName.c_str());
	string line, N;
	int T = 0;

	bool foundDigits[10];
	vector<vector<int> > lastTidyNumber;

	if (file.is_open())
	{
		getline(file, line);
		T = stoi(line);

		for (size_t i = 0; i < T; i++)
		{
			vector<int> dec(18, 0);
			lastTidyNumber.push_back(dec);
		}

		for (int i = 0; i < T; ++i)
		{
			file >> N;
			
			reverse(N.begin(), N.end());

			lastTidyNumber[i].resize(N.size());
			for (size_t j = 0; j < N.size(); j++)
			{
				lastTidyNumber[i][j] = N[j] - '0';
			}

			for (size_t j = 0; j < N.size()-1; j++)
			{
				if (lastTidyNumber[i][j] < lastTidyNumber[i][j + 1])
				{
					for (size_t k = 0; k <= j; k++)
					{
						lastTidyNumber[i][k] = 9;
					}
					lastTidyNumber[i][j + 1]--;
				}
			}
		}
	}

	file.close();

	ofstream outputfile;
	outputfile.open("Output.txt");

	for (int i = 0; i < T; ++i)
	{
		outputfile << "Case #" << i + 1 << ": ";

		reverse(lastTidyNumber[i].begin(), lastTidyNumber[i].end());

		for (size_t j = 0; j < lastTidyNumber[i].size(); j++)
		{
			if (lastTidyNumber[i][j] != 0)
			{
				outputfile << lastTidyNumber[i][j];
			}
		}

		if (i != (T-1))
			outputfile << endl;
	}

	outputfile.close();

	return 0;
}