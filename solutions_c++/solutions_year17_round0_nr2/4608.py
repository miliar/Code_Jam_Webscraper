#include"iostream"
#include"cstdio"
#include"vector"
#include"string"
#include"algorithm"
using namespace std;
bool IsTidy(unsigned long long Val)
{
	unsigned long long PrevDigit = 10;

	while (Val != 0)
	{
		unsigned long long Digit = Val % 10;
		Val = Val / 10;

		if (Digit > PrevDigit) { return false; }

		PrevDigit = Digit;
	}

	return true;
}
int main()
{
	int InputSize;
	::cin >> InputSize;

	for (int seek_times = 0; seek_times < InputSize; seek_times = seek_times + 1)
	{
		unsigned long long Boundary = 0;
		::cin >> Boundary;

		unsigned long long Val = Boundary;

		while (Val >= 0)
		{
			if (IsTidy(Val)) { break; }
			Val = Val - 1;
		}

		::cout << "Case #" << seek_times + 1 << ": " << Val << endl;
	}

	return 0;
}