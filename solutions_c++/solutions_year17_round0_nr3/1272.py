
#include <iostream>
#include <fstream>
#include<conio.h>
#include<stdio.h>
#include<iomanip>
#include<string>
#include<ctype.h>
#include<math.h>
using namespace std;
/*void main()
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
}*/
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
	long long t, n, c, to, co, temp, k, max;
	long long a[10000], b[10000], ra[10000], rb[10000], la[10000], lb[10000];
	ifstream fin("input.txt", ios::in);
	ofstream fout("output.txt", ios::out);
	fin >> t;
	for (int i = 1; i <= t; i++)
	{
		fin >> n >> k;
		co = 0;
		if (n % 2 == 0)
		{
			a[co] = 0;
			b[co] = 1;
			rb[co] = n / 2;
			lb[co] = n / 2 - 1;
			ra[co] = n / 2 - 1;
		}
		else
		{
			a[co] = 1;
			b[co] = 0;
			ra[co] = n / 2;
			rb[co] = n / 2;
			lb[co] = n / 2 - 1;
		}
		n /= 2;
		co += 1;
		to = 1;
		temp = 1;
		while (to < k){
			if (ra[co - 1] % 2 == 0)
			{
				a[co] = b[co - 1];
				b[co] = a[co - 1] * 2 + b[co - 1];
				if (lb[co - 1] == 0)
				{
					a[co] = 0;
				}
				if (ra[co - 1] == 0)
				{
					b[co] -= a[co - 1] * 2;
				}
				if (rb[co - 1] == 0)
				{
					b[co] -= b[co - 1];
				}
				rb[co] = rb[co - 1] / 2;
				lb[co] = rb[co - 1] / 2 - 1;
				ra[co] = lb[co - 1] / 2;
			}
			else
			{
				a[co] = a[co - 1] * 2 + b[co - 1];
				b[co] = b[co - 1];
				if (lb[co - 1] == 0)
				{
					a[co] -= b[co-1];
				}
				if (ra[co - 1] == 0)
				{
					a[co] -= a[co - 1] * 2;
				}
				if (rb[co - 1] == 0)
				{
					b[co] -= b[co - 1];
				}
				ra[co] = lb[co - 1] / 2;
				rb[co] = rb[co - 1] / 2;
				lb[co] = rb[co - 1] / 2 - 1;
			}
			if (lb[co] == -1)
				lb[co] = 0;
			temp = to;
			to += a[co] + b[co];
			co += 1;

		}

		if (ra[co - 1] >= rb[co - 1])
		{
			if (k <= (temp + a[co-1]))
				fout << "Case #" << i << ": " << ra[co - 1] << " " << ra[co - 1] << "\n";
			else
				fout << "Case #" << i << ": " << rb[co - 1] << " " << lb[co - 1] << "\n";
		}
		else
		{
			if (k <= (temp + b[co-1]))
				fout << "Case #" << i << ": " << rb[co - 1] << " " << lb[co - 1] << "\n";
			else
				fout << "Case #" << i << ": " << ra[co - 1] << " " << ra[co - 1] << "\n";
		}
	}
}