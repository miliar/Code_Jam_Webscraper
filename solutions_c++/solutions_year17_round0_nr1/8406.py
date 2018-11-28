/*
 * main.cpp
 *
 *  Created on: Apr 7, 2017
 *      Author: Trevor
 */

#include <iostream>
#include <cmath>
#include <string>


int main()
{
	int t;
	int * flipper_length;
	int cur_row;
	int cur_flipper;
	bool impossible = false;
	int num_flips = 0;
	std::string * pancake_rows;
	std::cin >> t;
	pancake_rows = new std::string [t];
	flipper_length = new int [t];

	for(int i = 0; i < t; i++)
	{
		std::cin >> pancake_rows[i];
		std::cin >> flipper_length[i];
	}

	for(int i = 0; i < t; i++)
	{
		num_flips = 0;
		impossible = false;
		std::cout << "Case #" << i + 1 << ": ";

		for(int i2 = 0; i2 < pancake_rows[i].length(); i2++)
		{
			if(pancake_rows[i][i2] == '-')
			{
				if(i2 + flipper_length[i] <= pancake_rows[i].length())
				{
					//flip next k pancakes
					for(int i3 = i2; i3 < i2 + flipper_length[i]; i3++)
					{
						if(pancake_rows[i][i3] == '-' )
						{
							pancake_rows[i][i3] = '+';
						}
						else
						{
							pancake_rows[i][i3] = '-';
						}

					}
					num_flips++;
				}
				else
				{
					std::cout << "IMPOSSIBLE" << std::endl;
					impossible = true;
					break;
				}
			}
		}

		if(!impossible)
		{
			std::cout << num_flips << std::endl;
		}
	}
	return 0;
}
