#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream fin;
	string name;
	getline(cin,name);
	fin.open(name);
	ofstream fout;
	fout.open("small-output.txt");
	int tests = 0;
	fin >> tests;
	int number = 0;
	int j = 1;
	while (j<=tests)
	{
		fin >> number;
		int check = number;
		int mod = check % 10;
		int num = 10;
		int i = 0;
		while (check>0)
		{
			if (mod <= num && check >= 10)
			{
				check /= 10;
				num = mod;
				mod = check % 10;
			}
			else
			{
				if (check < 10 && check <= num) 
					check = 0;
				else
				{
					i++;
					check = number - i;
					mod = check % 10;
					num = 10;
				}
			}
		}
		fout << "Case #" << j << ": " << number - i << endl;
		j++;
	}
	fin.close();
	fout.close();
	return 0;
}