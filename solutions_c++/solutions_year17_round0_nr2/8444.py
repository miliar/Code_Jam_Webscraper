/*
 * main.cpp
 *
 *  Created on: Apr 7, 2017
 *      Author: trevor
 */

#include <iostream>
#include <string>


int main()
{
	int t;
	int c;
	std::string * nums_s;
	std::cin >> t;
	nums_s = new std::string[t];

	//get all the numbers
	for(int i = 0; i < t; i++)
	{
		std::cin >> nums_s[i];
	}

	//find tidy numbers for each number
	for(int i = 0; i < t; i++)
	{
		c = 0;
		std::cout << "Case #" << i + 1 << ": ";
		for(int i2 = 0; i2 < nums_s[i].length() - 1; i2++)
		{
			if(nums_s[i][i2] > nums_s[i][i2 + 1])
			{
				//everything to right is going to be nine now
				for(int i3 = i2 + 1; i3 < nums_s[i].length(); i3++)
				{
					nums_s[i][i3] = '9';
				}



				//everything to left except leading digit will be nine if new digit is less then left side digit
				if(i2 != 0)
				{
					if(nums_s[i][i2] - 1 < nums_s[i][i2 - 1])
					{
						for(int i3 = i2; i3 > 0; i3--)
						{
							nums_s[i][i3] = '9';
						}
						nums_s[i][0] = nums_s[i][0] - 1;
					}
					else
					{
						nums_s[i][i2] = nums_s[i][i2] - 1;
					}
				}
				else
				{
					nums_s[i][i2] = nums_s[i][i2] - 1;
				}

				break;
			}
		}

		//output number
		if(nums_s[i][0] == '0')
		{
			//wait till we see not zero value to start outputing
			for(c = 0; c < nums_s[i].length(); c++)
			{
				if(nums_s[i][c] != '0')
				{
					break;
				}
			}

			for(c; c < nums_s[i].length(); c++)
			{
				std::cout << nums_s[i][c];
			}

			std::cout << std::endl;

		}
		else
		{
			std::cout << nums_s[i] << std::endl;
		}

	}

	return 0;
}



