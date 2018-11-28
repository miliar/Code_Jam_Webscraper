#include"iostream"
#include"cstdio"
#include"vector"
#include"string"
#include"algorithm"
using namespace std;
int main()
{
	int InputSize;
	::cin >> InputSize;

	for (int seek_times = 0; seek_times < InputSize; seek_times = seek_times + 1)
	{
		unsigned int PSize = 0;

		char Buffer[1024];
		::cin >> Buffer >> PSize;

		string str = Buffer;

		int PCount = 0;

		for (auto c : str)
		{ 
			PCount = PCount + (c == '+' ? 1 : 0);
		}

		int Times = 0;


		for (int seek = 0; seek < str.size(); seek = seek + 1)
		{
			//::cout << str.c_str() << endl;

			if (PCount == str.size()) { break; }
			if ((seek + PSize) > str.size())
			{ 
				Times = -1;
				break; 
			}

			if (str[seek] == '+') { continue; }

			for (int seek_p = 0; seek_p < PSize; seek_p = seek_p + 1)
			{
				bool bPos = str[seek + seek_p] == '+';

				PCount = PCount + (bPos ? -1 : 1);
				str[seek + seek_p] = bPos ? '-' : '+';
			}

			Times = Times + 1;
		}

		::cout << "Case #" << seek_times + 1 << ": " << (Times == -1 ? "IMPOSSIBLE" : to_string(Times)) << endl;
	}

	return 0;
}