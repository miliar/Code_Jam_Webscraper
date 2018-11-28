#include <iostream>
#include <string>
#include <sstream>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <fstream>

using namespace std;

string findPrevTidyNumber(string str)
{
	bool set_highbit = false;
	do
	{
		set_highbit = false;
		for (int i = 0; i!= str.length();++i)
		{
			if (set_highbit)
			{
				str[i] = '9';
				continue;
			}
			if (str[i] > str[i+1] && i != str.length() - 1)
			{
				str[i] -= 1;
				set_highbit = true;
			}
		}
	} while (set_highbit);
	str.erase(0, min(str.find_first_not_of('0'), str.size() - 1));
	return str;
}

int main()
{
	const string in = "B-large.in";
	const string out = "B-large.out";
	ofstream outputFile(out);
	ifstream inputFile(in);
	if (!inputFile.is_open())
	{
		cout << "Cannot open input file";
		outputFile.close();
		return 1;
	}
	string line;
	int case_num = 0;
	while (getline(inputFile, line))
	{
		if (case_num == 0)
		{
			++case_num;
			continue;
		}
		istringstream iss(line);
		string number;
		if (!(iss >> number)) { continue; }
		outputFile << "Case #" << case_num++ << ": " << findPrevTidyNumber(number) <<endl; 
	}
	inputFile.close();
	outputFile.close();
	return 0;
}
