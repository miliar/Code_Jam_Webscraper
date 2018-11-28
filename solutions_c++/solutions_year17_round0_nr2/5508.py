//Tatiana likes to keep things tidy.Her toys are sorted from smallest to largest, 
//her pencils are sorted from shortest to longest and her computers from oldest to newest.
//One day, when practicing her counting skills, she noticed that some integers, when written in base 10
//with no leading zeroes, have their digits sorted in non - decreasing order.Some examples of this are 8, 123, 555, and 
//224488. She decided to call these numbers tidy.Numbers that do not have this property, like 20, 321, 495 and 999990, 
//are not tidy.
//She just finished counting all positive integers in ascending order from 1 to N.
//What was the last tidy number she counted ?

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int T; // case
	long long N;// number
	int i = 1;//case number
	long long k = 1;
	long long value;
	int num1, num2;
	ifstream fin("B-large.in");
	ofstream fout("Output.out");

	fin >> T;
	while (i <= T)
	{
		fin >> N;
		value = N;
		while (value >= 10)
		{
			num1 = value % 10;
			value /= 10;
			num2 = value % 10;
			k *= 10;
			if (num1 < num2)
			{
				N=N-N%k-1;
				k = 1;
				value = N;
				continue;
			}
		}
		k = 1;
		fout << "Case #" << i << ": " << N << endl;

		i++;
	}
	fin.close();
	fout.close();
}