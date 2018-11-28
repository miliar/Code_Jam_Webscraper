#include<fstream>
#include<iostream>
#include<string>
#include<stdlib.h>
using namespace std;

bool tidy(string N)
{
	bool tidy = true;
	for (int i = 0; i < N.length()-1; i++)
	{
		if (N[i] > N[i + 1])
		{
			tidy = false;
			break;
		}
	}
	return tidy;
}


int main()
{
	ifstream input;
	int test_num;
	input.open("input.in");
	input >> test_num;
	for (int k = 0; k < test_num; k++)
	{
		string N;
		input >> N;
		while (!tidy(N))
		{
			int number = atoi(N.c_str());
			number--;
			char temp[20];
			itoa(number, temp, 10);
			N = temp;
		}
		ofstream output;
		output.open("output.txt", ofstream::app);
		output<<"Case #"<<k+1<<": " << N << endl;
		output.close();
	}
	system("notepad.exe output.txt");
}