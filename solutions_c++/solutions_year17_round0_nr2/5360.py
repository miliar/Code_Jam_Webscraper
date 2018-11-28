#include <iostream>
#include <fstream>
#include <string>
#include <limits>

using namespace std;
int main()
{
	ifstream istream("B-large.in");
	ofstream ostream("B-large.out");

	int T;
	istream >> T;

	string input;
	for (int i = 0; i < T; ++i)
	{
		istream >> input;
		int j = 0;

		while (j != input.length() - 1)
		{
			for (j = 0; j < input.length() - 1; ++j)
			{
				if (input[j] > input[j + 1])
				{
					input[j] -= 1;

					for (int k = j + 1; k < input.length(); ++k)
						input[k] = '9';
					break;
				}
			}
		}
		
		ostream << "Case #" << i + 1 << ": " << atoll(input.c_str()) << endl;

	}

	//long long input;
	//for (int i = 0; i < T; ++i)
	//{
	//	istream >> input;
	//	cout << "input : " << input << endl;	

	//	// number of digit
	//	long long temp = input, numDigit = 0;
	//	while (temp)
	//	{
	//		temp /= 10;
	//		++numDigit;
	//	}
	//	cout << numDigit;



	//	long long sub = 0;
	//	int j = 0;

	//	for (int j = numDigit - 1; j > 0; --j)
	//	{
	//		pow(10, numDigit)
	//	}
	//	//while (j != input.length() - 1)
	////	{

	//		for (j = input; j > 0; j/=10)
	//		{
	//			if (input[j] > input[j + 1])
	//			{
	//				sub = atoll(&(input[j + 1])) + 1;
	//				cout << "sub : " << sub << endl;

	//				atoll(input.c_str()) - sub;
	//				break;
	//			}
	//		}
	//	}

	//	cout << "Case #" << i + 1 << ": " << atoll(input.c_str()) - sub << endl;

	//}

	istream.close();
	ostream.close();
	return 0;
}