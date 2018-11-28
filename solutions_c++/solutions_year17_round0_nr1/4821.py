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
	string line, pk_string;
	int T = 0, K;
	ll N, currentNumber, tempNumber, result;

	bool foundDigits[10];
	vector<int> numberofFlips;

	if (file.is_open())
	{
		getline(file, line);
		T = stoi(line);

		numberofFlips.resize(T);

		for (int i = 0; i < T; ++i)
		{
			file >> pk_string >> K;
			
			vector<bool> pk(pk_string.size(), false);

			for (size_t j = 0; j < pk_string.size(); j++)
			{
				if (pk_string[j] == '+')
				{
					pk[j] = true;
				}
			}

			for (size_t j = 0; j < pk_string.size(); j++)
			{
				if (pk[j])
					continue;

				if ((j + K) > pk_string.size())
				{
					numberofFlips[i] = -1;
					break;
				}
				else
				{
					for (size_t m = 0; m < K; m++)
					{
						pk[j + m] = !pk[j + m];
					}
					numberofFlips[i]++;
				}
			}
		}
	}

	file.close();

	ofstream outputfile;
	outputfile.open("Output.txt");

	for (int i = 0; i < T; ++i)
	{
		if (numberofFlips[i] >= 0)
			outputfile << "Case #" << i + 1 << ": " << numberofFlips[i];
		else
			outputfile << "Case #" << i + 1 << ": IMPOSSIBLE";

		if (i != (T-1))
			outputfile << endl;
	}

	outputfile.close();

	return 0;
}