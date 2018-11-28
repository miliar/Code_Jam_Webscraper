#include <iostream>
#include <cstdlib>
#include <cstring>

inline long long int getPow10(long long int n)
{
	long long int tmp;
	long long int pow10 = 1;
	for(; (tmp = pow10 * 10) <= n; pow10 = tmp);
	return pow10;
}

char * solve(char *buffer, size_t len)
{	
	size_t i, loopbound;
	char flag, finished;
	char *res;
	flag = 0;
	finished = 0;
	loopbound = len - 1;

	while(!finished)
	{
		finished = 1;
		for(i = 0; i < loopbound; ++i)
		{
			if(buffer[i] > buffer[i+1])
			{
				finished = 0;
				--buffer[i];
				++i;
				flag = 1;
				break;
			}
		}
		if(flag)
		{
			for(; i < len; ++i)
			{
				buffer[i] = '9';
			}
		}
	}

	res = buffer;
	while(*res == '0' && res[1] != '\0') {
		++res;
	}
	return res;
}

int main(int argc, char **argv)
{
	int t, i;
	char buffer[0x20];
	std::string n;

	std::cin >> t;
	for(i = 1; i <= t; ++i)
	{
		std::cin >> n;
		strcpy(buffer, n.c_str());
		std::cout << "Case #" << i << ": " << solve(buffer, n.length()) << std::endl;
	}

	return 0;
}
