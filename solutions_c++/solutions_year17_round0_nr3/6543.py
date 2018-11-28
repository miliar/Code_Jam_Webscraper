/*
 * main.cpp
 *
 *  Created on: Apr 8, 2017
 *      Author: trevor
 */

#include <iostream>
#include <string>
#include <vector>

int main()
{
	int t;
	int * stalls;
	int * people;
	int * left_stalls;
	int * right_stalls;
	bool * bathroom;
	int selected_stall;
	int temp;
	int temp2;
	std::vector<int> min;
	std::vector<int> max;


	std::cin >> t;

	stalls = new int [t];
	people = new int [t];

	for(int i = 0; i < t; i++)
	{
		std::cin >> stalls[i];
		std::cin >> people[i];
	}

	for(int i = 0; i < t; i++)
	{
		bathroom = new bool [stalls[i] + 2];
		bathroom[0] = true;
		bathroom[stalls[i] + 1] = true;
		left_stalls = new int [stalls[i] + 2];
		right_stalls = new int [stalls[i] + 2];
		std::cout << "Case #" << i + 1 << ": ";
		//empty stalls
		for(int i2 = 1; i2 < stalls[i] + 1; i2++)
		{
			bathroom[i2] = false;
		}

		//simulation each individual walking in
		for(int i2 = 0; i2 < people[i]; i2++)
		{
			max.clear();
			min.clear();
			//calculate the number of empty stalls to left and right for each stall
			for(int i3 = 1; i3 < stalls[i] + 2; i3++)
			{
				//calculate number of left empty stalls
				for(int i4 = i3 - 1; i4 >= 0; i4--)
				{
					if(bathroom[i4] == true)
					{
						left_stalls[i3] = (i3 -1) - i4;
						break;
					}
				}

				//calculate number of right empty stalls
				for(int i4 = i3 + 1; i4 < stalls[i] + 2; i4++)
				{
					if(bathroom[i4] == true)
					{
						right_stalls[i3] = i4 - (i3 + 1);
						break;
					}
				}
			}


			temp = 0;

			//calculate the stall with the max min(l,r)
			for(int i3 = 0; i3 < stalls[i] + 1; i3++)
			{
				if(bathroom[i3] != true)
				{
					if(left_stalls[i3] <= right_stalls[i3])
					{
						if(left_stalls[i3] > temp)
						{
							temp = left_stalls[i3];
							min.clear();
							min.push_back(i3);
						}
						else if(left_stalls[i3] == temp)
						{
							min.push_back(i3);
						}
					}
					else
					{
						if(right_stalls[i3] > temp)
						{
							temp = right_stalls[i3];
							min.clear();
							min.push_back(i3);
						}
						else if(right_stalls[i3] == temp)
						{
							min.push_back(i3);
						}
					}
				}
			}

			if(min.size() > 1)
			{
				temp2 = 0;
				max.clear();
				for(int i3 = 0; i3 < min.size(); i3++)
				{
					if(left_stalls[min[i3]] >= right_stalls[min[i3]])
					{
						if(left_stalls[min[i3]] > temp2)
						{
							temp2 = left_stalls[min[i3]];
							max.clear();
							max.push_back(min[i3]);
						}
						else if(left_stalls[min[i3]] == temp2)
						{
							max.push_back(min[i3]);
						}
					}
					else
					{
						if(right_stalls[min[i3]] > temp2)
						{
							temp2 = right_stalls[min[i3]];
							max.clear();
							max.push_back(min[i3]);
						}
						else if(right_stalls[min[i3]] == temp2)
						{
							max.push_back(min[i3]);
						}
					}
				}

				bathroom[max[0]] = true;
				selected_stall = max[0];
			}
			else
			{
				bathroom[min[0]] = true;
				selected_stall = min[0];
			}

		}

		//calculate number of left empty stalls
		for(int i3 = selected_stall - 1; i3 >= 0; i3--)
		{
			if(bathroom[i3] == true)
			{
				left_stalls[selected_stall] = (selected_stall -1) - i3;
				break;
			}
		}

		//calculate number of right empty stalls
		for(int i3 = selected_stall + 1; i3 < stalls[i] + 2; i3++)
		{
			if(bathroom[i3] == true)
			{
				right_stalls[selected_stall] = i3 - (selected_stall + 1);
				break;
			}
		}

		if(right_stalls[selected_stall] >= left_stalls[selected_stall])
		{
			std::cout << right_stalls[selected_stall] << " " << left_stalls[selected_stall] << std::endl;
		}
		else
		{
			std::cout << left_stalls[selected_stall] << " " << left_stalls[selected_stall] << std::endl;
		}
	}
}


