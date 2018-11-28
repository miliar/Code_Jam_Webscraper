#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int start_change_at(string &number)
{
	for (int i = 0; i < number.size() - 1; i++)
	{
		if (number[i] > number[i + 1])
		{
			while (i > 0 && number[i] == number[i - 1])
			{
				i--;
			}
			return i; 
		}
	}

	return -1;
}

string max_tidy_number(string number)
{
	int start_indx = start_change_at(number);

	if (start_indx == 0 && number[0] == '1')
	{
		string nines = "";
		for (int i = 0; i < number.size() - 1; i++) 
		{
			nines += "9";
		}
		
		return nines;
	} 
	
	if (start_indx == -1)
	{
		return number;
	}

	number[start_indx]--;
		
	for (start_indx = start_indx + 1; start_indx < number.size(); start_indx++)
	{
		number[start_indx] = '9';
	}
		
	return number;
}

int main()
{
	
	ifstream fin;
	ofstream fout;

	fin.open("input.txt");
	fout.open("output.txt");

	int t;
	
	fin >> t;
	
	for (int i = 1; i <= t; i++)
	{
		string number;
	
		fin >> number;
		
		fout << "Case #" << i << ": " << max_tidy_number(number) << endl;
	}
		
	
	return 0;
}
