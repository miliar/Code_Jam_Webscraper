#include <iostream>
#include <fstream>
#include <string>

using namespace std;


bool sorted(char  number[10])
{
	int length = strlen(number);

	//If the number is already sorted
	bool isSorted = true;

	for (int j = 0; j < length - 1 && isSorted; j++)
	{
		if (number[j] > number[j + 1])
			isSorted = false;
	}

	return isSorted;
}




int main()
{
	ifstream fin("B-small-attempt0.in");
	ofstream fout("a.out");


	long long int n = 0;

	string n1 = "";

	getline(fin, n1);

	n = atoi(n1.c_str());

	string number1;

	
	for (long long int i = 0; i < n; i++)
	{
		getline(fin, number1);

		char number[10];

		strcpy_s(number, number1.c_str());

		bool stop = false;

		if (atoi(number) < 10)
		{
			fout << "Case #" << i+1 << ": " << number << endl;
			stop = true;
		}

		if (!stop)
		{
			//If the number is such that only first digit is non-zero and rest of the digits are zero
			int zero = atoi(number + 1);

			if (zero == 0)
			{
				fout << "Case #" << i + 1 << ": " << atoi (number) - 1 << endl;
				stop = true;
			}

			if (!stop)
			{
				//Regular Processing

				int temp = atoi(number);
				char R[16];

				while (!stop)
				{
					sprintf_s(R, "%d", temp);

					strcpy_s(number, R);

					if (sorted(number))
					{
						fout << "Case #" << i + 1 << ": " << number << endl;
						stop = true;
					}

					temp = temp - 1;
				}
			}
		}
	}


	return 0;
}