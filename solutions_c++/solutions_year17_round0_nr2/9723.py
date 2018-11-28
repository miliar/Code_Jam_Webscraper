#include <bits/stdc++.h>
using namespace std;
int main ()
{
	ifstream fin;
	ofstream fout;
	fin.open("input.in");
	fout.open("output.txt");
	int t, i, dig, first, second, flag, x, third;
	long long int n, res, tmp;
	fin >> t;
	for (i=1; i<=t; i++)
	{
		fin >> n;
		res = 0;
		dig = flag = 0;
		tmp = n;
		while (tmp)
		{
			tmp /= 10;
			dig++;
		}
		for (x=dig-1; x>0; x--)
		{
			if (flag == 1)
			{
				res *= 10;
				res += 9;
				continue;
			}
			first = n/(pow(10,x));
			first %= 10;
			second = n/(pow(10,x-1));
			second %= 10;
			if (first==second && x!=1)
			{
				third = n/(pow(10,x-2));
				third %= 10;
				if (third<first)
				{
					flag = 1;
					res *= 10;
					res += first-1;
				}
				else
				{
					res *= 10;
					res += first;
				}
			}
			else if (first<=second)
			{
				res *= 10;
				res += first;
			}
			else
			{
				flag = 1;
				res *= 10;
				res += first-1;
			}
		}
		if (x==0)
		{
			if (flag==0)
			{
				res *= 10;
				res += n%10;
			}
			else
			{
				res *= 10;
				res += 9;
			}
		}
		fout << "Case #" << i << ": " << res << endl;
	}
	fin.close();
	fout.close();
	return 0;
}
