// CPP file
// Created in Microsoft VS2017 Community  

#include <algorithm>
#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>


using namespace std;

int main()
{
	int T = 0; // test cases
	vector<vector<bool>> pancakes;
	vector<int> consecutive_K;
	vector<int> results;

	string sFileName = "A-large";

	//--------------------- begin - reading from file ---------------------
	FILE *stream;

	if (fopen_s(&stream, (sFileName + ".in").c_str(), "r"))
	{
		cout << "File does not exist" << endl;
	}
	else
	{
		fscanf_s(stream, "%d", &T); // "%ld"   "%f"   "%c"

		for (int idx = 0; idx < T; ++idx)
		{
			// reading data for each test case

			char sKeys[1005];
			fscanf_s(stream, "%s", sKeys, _countof(sKeys));
			string s1 = string(sKeys);
			vector<bool> vecTemp;
			for (unsigned int uii = 0; uii < s1.size(); ++uii)
			{
				if (s1[uii] == '+')
				{
					vecTemp.push_back(true);
				}
				else
				{
					vecTemp.push_back(false);
				}
			}
			pancakes.push_back(vecTemp);

			int K = 0;
			fscanf_s(stream, "%d", &K);
			consecutive_K.push_back(K);
		}

		// closing file
		fclose(stream);
	}
	//--------------------- end - reading from file -----------------------


	//--------------------- begin - algorithm ---------------------
	for (int idx = 0; idx < T; ++idx)
	{
		int flips = 0;
		bool finished = false;

		while (!finished)
		{
			vector<bool>::iterator it = find(pancakes[idx].begin(), pancakes[idx].end(), false);
			if (it != pancakes[idx].end())
			{
				// found so flip if possible
				int index = it - pancakes[idx].begin();
				if (pancakes[idx].size() - index < consecutive_K[idx])
				{
					// impossible
					results.push_back(-1);
					finished = true;
				}
				else
				{
					for (int j = index; j < index + consecutive_K[idx]; ++j)
					{
						// flip
						pancakes[idx][j] = !pancakes[idx][j];
					}
					++flips;
				}
			}
			else
			{
				results.push_back(flips);
				finished = true;
			}
		}
	}
	//--------------------- end - algorithm -----------------------


	//--------------------- begin - printing to file ---------------------
	ofstream out;
	out.open(sFileName + ".txt");

	for (int idx = 0; idx < T; ++idx)
	{
		if (results[idx] == -1)
		{
			out << "Case #" << idx + 1 << ": " << "IMPOSSIBLE" << endl;
		}
		else
		{
			out << "Case #" << idx + 1 << ": " << results[idx] << endl;
		}
	}

	out.close();
	//--------------------- end - printing to file -----------------------

	//
	return 0;
}
