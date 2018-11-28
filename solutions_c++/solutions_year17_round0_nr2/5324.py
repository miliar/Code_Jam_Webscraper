#include <bits/stdc++.h>
using namespace std;

long long int t, n, pos;
long long int d[20];

long long int powe(long long int base, long long int power)
{
	long long int x = 1;
	for (int i = 0; i < power; i++)
	{
		x = x*base;
	}
	return x;
}

void print()
{
	for (int i = 0; i < 20; i++)
	{
		cout << d[i] << " ";
	}
	cout << endl;
}

long long int printrl()
{
	long long int num = 0;
	for (int i = 19; i >=0; i--)
	{
		num = num*10+d[i];
	}
	return num;
}

int main()
{
	cin >> t;
	for (int i = 0 ; i < t; i++)
	{
		for (int j = 0; j < 20; j++)
		{
			d[j] = 0;
		}
		pos = -2;
		cin >> n;
		for (int j = 0; j < 18; j++)
		{
			d[j] = (((n%(powe(10,j+1))))-(n%(int(powe(10,j)))))/(powe(10,j));
		}
		for (int j = 0; j < 19; j++)
		{
			if (d[j] < d[j+1])
			{
				pos = j;
			}
			if (pos == j-1)
			{
				if (d[j] <= d[j+1])
				{
					pos++;
				}
			}
		}
		d[pos+1]-=1;
		for (int j = 0; j < pos+1; j++)
		{
			d[j] = 9;
		}
		cout << "Case #" << i+1 << ": "<< printrl() << endl;
		
	}
}