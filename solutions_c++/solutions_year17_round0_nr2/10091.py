#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int T;

vector<long long int> v;

void beOlvas()
{
	ifstream inputFile("input.in");
	inputFile >> T;

	long long int data;

	for(int i = 0; i < T; i++)
	{
		inputFile >> data;
		v.push_back(data);
	}

}

inline bool tidyNumber(long long int num)
{
	int digit = num % 10;
	num /= 10;

	long long int aux;

	while(num != 0)
	{
		aux = num % 10;

		if(digit < aux)
		{
			return false;
		}

		digit = aux;
		num /= 10;
	}

	return true;
}

void kiIr()
{
	ofstream outputFile;
	outputFile.open("output.out");

	for(int i = 0; i < T; i++)
	{
		if(tidyNumber(v[i]))
		{
			outputFile << "Case #" << i + 1 << ": " << v[i] << endl;
		}
		else
		{
			for(long long int j = v[i] - 1; j > 9; j--)
			{
				if(tidyNumber(j))
				{
					outputFile << "Case #" << i + 1 << ": " << j << endl;
					break;
				}
			}
		}
	}

	outputFile.close();
}

int main(int argc, char const *argv[])
{
	beOlvas();
	kiIr();

	return 0;
}