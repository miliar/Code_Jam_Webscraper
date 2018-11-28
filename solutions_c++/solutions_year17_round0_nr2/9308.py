#include <iostream>
#include <string>

int main()
{
	int T, K;
	std::string S;
	std::cin >> T;

	for(int k = 0; k < T; ++k)
	{
		std::cin >> S;
		for(int i = (S.length()-1); i > 0; --i)
		{
			if ( S[i] < S[i-1] )
			{
				if ( S[i-1] == '0' )
				{
					for(int j = 1; j < (i-1); j++)
					{
						S[j] = '9';
					}
					S[0] = '0';
				}
				else
				{
					int a = S[i-1]-1;
					S[i-1] = a;
					for(int j = i; j < S.length(); j++)
					{
						S[j] = '9';
					}
				}
			}
		}
		long num = std::stol(S);
		std::cout << "Case #" << k+1 << ": " << num << std::endl;
	}
	return 0;
}