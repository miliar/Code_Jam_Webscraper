
#include <iostream>
#include <fstream>
#include<conio.h>
#include<stdio.h>
#include<iomanip>
#include<string>
#include<ctype.h>
#include<math.h>
using namespace std;
void main()
{
	long long t, n, a, b, c, to, co, temp;
	ifstream fin("input.txt", ios::in);
	ofstream fout("output.txt", ios::out);
	fin >> t;
	for (int i = 1; i <= t; i++)
	{
		to = 0;
		co = 10;
		fin >> n;
		//fout << n;
		temp = n;
		c = n / 10;
		while (c != 0)
		{
			a = n % 10;
			b = c % 10;
			if (a < b)
			{
				n -= a + 1;
				c -= 1;
				//fout << n << " " << c;
				temp=c*co+co-1;

			}
			c /= 10;
			n /= 10;
			co *= 10;
		}

		fout << "Case #" << i << ": " << (temp) << "\n";
	}
}