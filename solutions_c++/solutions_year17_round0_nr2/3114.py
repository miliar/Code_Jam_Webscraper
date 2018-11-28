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
	vector<vector<int>> numbers_digits;

	string sFileName = "B-large";

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

			char temp[22];
			fscanf_s(stream, "%s", temp, _countof(temp));
			vector<int> vectemp;
			for (int i = 0; temp[i] != '\0'; ++i)
			{
				vectemp.push_back((temp[i] - '0'));
			}
			numbers_digits.push_back(vectemp);
		}

		// closing file
		fclose(stream);
	}
	//--------------------- end - reading from file -----------------------


	//--------------------- begin - algorithm ---------------------
	for (int i = 0; i < T; ++i)
	{
		bool found = false;
		while (!found)
		{
			if(!is_sorted(numbers_digits[i].begin(), numbers_digits[i].end()))
			{
				vector<int>::iterator it = is_sorted_until(numbers_digits[i].begin(), numbers_digits[i].end());
				int index = it - numbers_digits[i].begin();
				if (index != 0)
				{
					--index;
				}
				fill(it, numbers_digits[i].end(), 9);
				--numbers_digits[i][index];

				if (numbers_digits[i][0] == 0)
				{
					numbers_digits[i].erase(numbers_digits[i].begin());
				}
			}
			else
			{

				found = true;
			}
		}
	}
	//--------------------- end - algorithm -----------------------


	//--------------------- begin - printing to file ---------------------
	ofstream out;
	out.open(sFileName + ".txt");

	for (int idx = 0; idx < T; ++idx)
	{
		string num("");
		for (int j = 0; j < numbers_digits[idx].size(); ++j)
		{
			num += to_string(numbers_digits[idx][j]);
		}
		out << "Case #" << idx + 1 << ": " << num << endl;
	}

	out.close();
	//--------------------- end - printing to file -----------------------

	//
	return 0;
}
