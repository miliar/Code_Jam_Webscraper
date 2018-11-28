#include <iostream>
#include <cstring>

#define LIMIT 25

int main(int argc, char **argv)
{
	char cake[LIMIT][LIMIT];
	int t, r, c;


	memset(cake, 0, sizeof(cake));
	std::cin >> t;
	for(int i = 1; i <= t; ++i)
	{
		std::cin >> r >> c;
		for(int j = 0; j < r; ++j)
		{
			for(int k = 0; k < c; ++k)
			{
				std::cin >> cake[j][k];
			}
		}

		/* solve the problem */
		for(int j = 0; j < r; ++j)
		{
			for(int k = 0; k < c; ++k)
			{
				if(cake[j][k] == '?')
				{
					int x = k;
					while(++x < c && cake[j][x] == '?');
					if(x < c)
						cake[j][k] = cake[j][x];
					x = k;
					while(--x >= 0 && cake[j][x] == '?');
					if(x >= 0)
						cake[j][k] = cake[j][x];
				}
			}
		}

		/* solve the problem */
		for(int j = 0; j < r; ++j)
		{
			for(int k = 0; k < c; ++k)
			{
				if(cake[j][k] == '?')
				{
					int x = j;
					while(++x < r && cake[x][k] == '?');
					if(x < r)
						cake[j][k] = cake[x][k];
					x = j;
					while(--x >= 0 && cake[x][k] == '?');
					if(x >= 0)
						cake[j][k] = cake[x][k];
				}
			}
		}

		std::cout << "Case #" << i << ":" << std::endl;
		for(int j = 0; j < r; ++j)
		{
			for(int k = 0; k < c; ++k)
			{
				std::cout << cake[j][k] << "";
			}
			std::cout << std::endl;
		}
	}


	return 0;
}
