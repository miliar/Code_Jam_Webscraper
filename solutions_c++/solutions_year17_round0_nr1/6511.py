#include <iostream>
#include <cmath>
#include <string>
#include <fstream>
using namespace std;
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("a_large.txt");
	int a, siz = 0, time = 0, count = 0;
	fin >> a;
	string b;
	while (fin >> b >> a)
	{
		++time;
		siz = b.size();
		for (int i = 0; i < siz - a + 1; ++i)
		{
			if (b[i] == '-')
			{
				for (int j = i; j < i + a; ++j)
				{
					if (b[j] == '+')
						b[j] = '-';
					else
						b[j] = '+';
				}
				++count;
			}
		}
		for (int i = siz - a + 1; i < siz; ++i)
		{
			if (b[i] == '-')
			{
				fout << "Case #" << time << ": IMPOSSIBLE" << endl;
				goto fuck;
			}
		}
		fout << "Case #" << time << ": " << count << endl;
	fuck:
		count = 0;
	}
	return 0;
}