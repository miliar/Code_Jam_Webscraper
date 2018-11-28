#include <array>
#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char** argv)
{
	if (argc < 2)
	{
		cout << "Not enough arguments" << endl;
		return EXIT_FAILURE;
	}
	ifstream file(argv[1]);
	if(!file.is_open())
	{
		cout << "Error: could not read file: " << argv[1] << endl;
		return EXIT_FAILURE;
	}

	int T;
	file >> T;

	string fileName = "output.txt";
	ofstream output(fileName, ios::out | ios::trunc);
	if (!output.is_open())
	{
		cout << "Error: could not write file: " << fileName.c_str() << endl;
		return EXIT_FAILURE;
	}
	for (int i = 0; i < T; i++)
	{
		long long N;
		file >> N;
		array<int, 20> digits;
		int nbDigits = 0;
		while (N > 0)
		{
			digits[nbDigits] = N % 10;
			N /= 10;
			nbDigits++;
		}
		int droped = -1;
		int toBeDroped = -1;
		for (int k = nbDigits - 1; k >= 1 && droped == -1; k--)
		{
			if (digits[k] > digits[k - 1])
			{
				if (toBeDroped != -1)
					droped = toBeDroped;
				else
					droped = k;
			}
			else if (digits[k] < digits[k - 1])
				toBeDroped = -1;
			else if (toBeDroped == -1)
					toBeDroped = k;
		}
		if (droped != -1)
		{
			digits[droped] -= 1;
			for (int k = droped - 1; k >= 0; k--)
				digits[k] = 9;
		}
		output << "Case #" << i + 1 << ": ";
		for (int k = nbDigits - 1 - (int)(digits[nbDigits - 1] == 0); k >= 0; k--)
			output << digits[k];
		output << endl;
	}
	output.close();
	file.close();
	cout << "Done\n";
	return EXIT_SUCCESS;
}