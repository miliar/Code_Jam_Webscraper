#include <iostream>
#include <cmath>
#include <string>
#include <fstream>
using namespace std;
int main()
{
	int c = 0;
	ofstream fout;
	ifstream fin;
	fin.open("B-large.in");
	fout.open("out.txt");
	string a;
	fin >> c;
	c = 1;
	while (fin >> a)
	{
		unsigned long long b = 0;
		int siz = 0;
		siz = a.size();
		for (int i = 0; i < siz; ++i)
		{
			a[i] -= 48;
 		}
		for (int i = 0; i < siz - 1; ++i)
		{
			if (a[i] > a[i + 1])
			{
				fuck:
				if (i)
				{
					if (a[i] != a[i - 1])
					{
						--a[i];
						for (int j = i + 1; j < siz; ++j)
						{
							a[j] = 9;
						}
					}
					else
					{
						--i;
						goto fuck;
					}
				}
				else
				{
					--a[i];
					for (int j = i + 1; j < siz; ++j)
					{
						a[j] = 9;
					}
				}
			}
		}
		for (int i = 0; i < siz; ++i)
		{
			b += a[i] * long long (pow(10, siz - i - 1));
		}
		fout << "Case #"<<c<<": "<<b << endl;
		++c;
	}
	return 0;
}