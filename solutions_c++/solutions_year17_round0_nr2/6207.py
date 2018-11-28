/*
 * ./executable < input > output
 */
#include <iostream>
#include <string>

int main()
{
	int T;
	std::cin >> T;
	for(int t = 1; t <= T; t++)
	{
		std::string N;
		std::cin >> N;
		int j = 0;
		for(int i = 0; i < N.length(); i++)
		{
			if(N[i] > N[i-1])
				j = i;
			if(N[i] < N[i-1])
			{
				N[j]--;
				for(int k = j+1; k < N.length(); k++)
					N[k] = '9';
				if(N[j] == '0')
					N = N.substr(1);
				break;
			}
		}
		std::cout << "Case #" << t << ": ";
		std::cout << N << std::endl;
	}
}
