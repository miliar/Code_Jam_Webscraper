#include <iostream>
#include <string>
#include <cassert>
#include <algorithm>

// https://code.google.com/codejam/contest/6254486/dashboard#s=p1

char Inverse(char c)
{
	if (c == '+')
		return '-';
	return '+';
}
// return -10000 if impossible
int GetFlips(char* str, int len, int K, char cDest)
{
	assert(len >= K);
	assert(K >= 2);
	if (len == K)
	{
		bool bSame = true;
		for (int i = 1; i < K; ++i)
		{
			if (str[i] != str[0])
			{
				bSame = false;
				break;
			}
		}
		if (bSame)
		{
			if (cDest == str[0])
				return 0;
			return 1;
		}
		else
			return -10000;
	}

	if (str[0] == cDest)
		return GetFlips(str + 1, len - 1, K, cDest);

	// else flip the first K
	for (int i = 0; i < K; ++i)
		str[i] = Inverse(str[i]);
	return 1+GetFlips(str + 1, len - 1, K, cDest);
}

int main()
{
	int nTests;
	std::cin >> nTests;
	for (int nCase =0 ; nCase < nTests; ++nCase)
	{				
		std::string t2b;
		std::cin >> t2b;

		int K;
		std::cin >> K;

		char* tempStr = new char[t2b.length() + 1];
		strcpy_s(tempStr, t2b.length()+1, t2b.c_str());
		int nLeftAttempts = GetFlips(tempStr, t2b.length(), K, '+');
		// revsere string
		for (size_t i = 0; i < t2b.length(); i++)
		{
			tempStr[t2b.length() - 1 - i] = t2b[i];
		}
		int nRightAttempts = GetFlips(tempStr, t2b.length(), K, '+');

		std::cout << "Case #" << nCase + 1 << ": ";
		if (nLeftAttempts < 0 && nRightAttempts < 0)
			std::cout<< "IMPOSSIBLE";
		else if (nLeftAttempts >= 0 && nRightAttempts < 0)
			std::cout << nLeftAttempts;
		else if (nLeftAttempts < 0 && nRightAttempts >= 0)
			std::cout << nRightAttempts;
		else
		{
			assert(nLeftAttempts >= 0);
			assert(nRightAttempts >= 0);
			std::cout << std::min(nRightAttempts, nLeftAttempts);
		}


		
		std::cout<<std::endl;
	}

	return 0;
}
