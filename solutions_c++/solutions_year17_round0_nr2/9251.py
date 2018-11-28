#include<iostream>
#include<conio.h>
#include<fstream>
#include<string>
using namespace std;
bool istidy(unsigned long long number)
{
	int prev = number % 10;
	if (prev == 0)
		return false;
	number = number / 10;
	while (number)
	{
		int next = number % 10;
		number = number / 10;
		if (prev < next)
			return false;
		prev = next;
	}
	return true;
}
unsigned long long convert(string number)
{
	for (int i = number.length() - 1; i > 0; i--)
	{
		if (number[i] < number[i - 1])
		{
			int k = number[i - 1];
			number[i - 1] = k - 1;
			number[i] = '9';
			for (int j = i; j < number.length(); j++)
			{
				number[j] = '9';
			}
		}
	}
	return stoll(number);
}
int main()
{
	int cases;
	ifstream fin;
	fin.open("B-large.in");
	ofstream fout;
	fout.open("output.txt");
	fin >> cases;
	fin.ignore();
	int i = 1;
	int j = 1;
	if (fin.is_open())
	{
		string number;
		while (!fin.eof())
		{
			getline(fin, number, '\n');
			if (number != "")
			{
				unsigned long long k = convert(number);
				while (!istidy(k))
					k--;
				cout << "Case #" << i++ << ": " << k << endl;// << "  -> Input: " << number << endl;
				fout << "Case #" << j++ << ": " << k << endl;
			}
		}
	}
	//_getch();
	return 0;
}