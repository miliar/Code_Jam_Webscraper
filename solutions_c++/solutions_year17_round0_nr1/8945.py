#include <iostream>
#include <fstream>
#include <string>


int main()
{
	long long T;
	std::cin >> T;
	std::string pancakes;
	std::string size;
	for (int i=0; i<T; i++)
	{
		int flips = 0;
		std::getline(std::cin, pancakes,' ');
		std::getline(std::cin, size);
		int pansize = std::stoi(size);
		if (i == 0)
		{
			pancakes.erase(1,1);
			pancakes.erase(0,1);
		}
		for (int j=0; j<pancakes.length()-pansize+1; j++)
		{
			if (pancakes[j] == '-')
			{
				flips++;
				for (int w=j; w<j+pansize; w++)
				{
					if (pancakes[w] == '-') pancakes[w] = '+';
					else pancakes[w] = '-';

				}
			}
		}
		bool possible = true;
		for (int j=0; j<pancakes.length(); j++)
		{
			if (pancakes[j] == '-')
			{
				possible = false;
			} 
		}
		if (possible) std::cout << "Case #" << i+1 << ": " << flips << std::endl; 
		else std::cout << "Case #" << i+1 << ": IMPOSSIBLE" << std::endl; 
	}
}