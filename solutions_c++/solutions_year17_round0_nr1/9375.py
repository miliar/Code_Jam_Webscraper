// google_codejam_qual_1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>

int main()
{
	std::ofstream os;
	std::ifstream in;
	int in_num = 0;
	int attempt_num = 0;
	scanf("%d", &attempt_num);
	std::string input;
	std::string file_in_name = "A-large.in";
	os.open("output.txt");
	in.open(file_in_name);
	in >> in_num;
	int k = 0;
	int num_up = 0;
	int flips = 0;
	std::vector<int> flip_index;
	std::vector<int> double_flip_index;
	for (int n = 0; n < in_num; n++)
	{
		flips = 0;
		in >> input;
		in >> k;
		bool possible = false;
		bool impossible = false;
		bool all_up = false;
		int counter = 0;
		for (char pancake : input)
		{
			if (pancake == '+')
			{
				counter++;
			}
		}
		if (counter == input.size())
		{
			all_up = true;
		}
		else if (((counter == 0) && (input.size() % k) == 0) && (input.size() > k))
		{
			for (int j = 0; j < input.length(); j++)
			{
				input.at(j) = (input.at(j) == '+') ? '+' : '+';
			};
			flips = input.size() / k;
			all_up = true;
		}
		else
		{
			while (!(all_up || impossible))
			{
				for (int i = 0; i < input.size(); i++)
				{

					if ((input.at(i) == '-') && ((i + k - 1) < input.size()))
					{
						flips++;
						for (size_t j = i; j < i + k && j < input.size(); j++)
						{
							input.at(j) = (input.at(j) == '+') ? '-' : '+';
						}
					}
					
				}//for (int i = 0; i < input.size(); i++)
				counter = 0;
				for (char pancake : input)
				{
					if (pancake == '+')
					{
						counter++;
					}
				}
				if (counter == input.size())
				{
					all_up = true;
					continue;
				}
				else if ((input.size() - counter) < k)
				{
					impossible = true;
					break;
				}
			}
		}
		if (all_up && !impossible)
		{
			os << "Case #" << n + 1 << ": " << flips << std::endl;
		}
		else
		{
			os << "Case #" << n + 1 << ": " << "IMPOSSIBLE" << std::endl;
		}
	}//for (int i = 0; i < in_num; i++)
	in.close();
	os.close();
	return 0;
}