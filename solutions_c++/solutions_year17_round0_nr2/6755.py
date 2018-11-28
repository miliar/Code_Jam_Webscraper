#include <iostream>
#include <string> 
#include <cmath>
using namespace std;

int main(int argc, char const *argv[])
{
	int num = 0;
	int count = 0;
	cin >> num;
	for (int i = 0; i < num; ++i)
	{
		long long int input;
		cin >> input;
		int digit = log10(input) + 1;
		long long int n = 1;
		for (int i = 1; i < digit; ++i)
		{
			n *= 10;
			if (input % n < ((input % (n * 10)) / 10))
			{
				input = input - n;
				input = input - input % n;
				long long int times = 9;
				for (int j = 0; j < i; ++j)
				{
					input = input + times;
					times *= 10;
				}
			}
		}


		count++;
		cout << "Case #" << count << ": " << input << "\n";
	}
	return 0;
}