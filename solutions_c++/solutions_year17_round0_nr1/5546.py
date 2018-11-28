#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <cstring>
#include <cstdlib>

struct problem
{
	std::string input;
	int k;	
};
typedef struct problem problem_t;


void flip(char *p, int f)
{
	int i;
	for(i = 0; i < f; ++i, ++p)
	{
		char v = (*p == '+' ? '-' : '+');
		*p = v;
	}
}

int solve_problem(const char *input, int k)
{
	char buffer[0x400];
	size_t i, loopbound, len;	/* loop counter, loopbound, length */
	int c;						/* cound number of flips */
	len = strlen(input);
	strcpy(buffer, input);
	loopbound = len - k + 1;
	c = 0;

	for(i = 0; i < loopbound; ++i)
	{
		if(buffer[i] == '-')
		{
			flip(&buffer[i], k);
			++c;
		}
	}

	for(i = 0; i < len; ++i)
	{
		if(buffer[i] != '+')
			c = -1;
	}

	return c;
}

int main(int argc, char **argv)
{
	int t, k, r, i;
	std::string s;

	std::cin >> t;
	for(i = 1; i <= t; ++i)
	{
		std::cin >> s >> k;
		r = solve_problem(s.c_str(), k);
		if(r >= 0)
			std::cout << "Case #" << i << ": " << r << std::endl;
		else
			std::cout << "Case #" << i << ": IMPOSSIBLE" << std::endl;
	}

	return 0;
}
