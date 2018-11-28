#ifndef ALPER
#include <bits/stdc++.h>
#endif

#ifdef ALPER
#include <Windows.h>
#endif

#include <string>
#include <iostream>
#include <queue>
#include <sstream>
#include <fstream>
using namespace std;

int unequiv(char c)
{
	if (c == '+')
		return 0;

	return 1;
}
int ss;
int sum_till_exc(int *co, int i)
{
	if (i > ss) i = ss;
	int sum = 0;
	for (int j = 0; j < i; ++j)
	{
		sum += co[j];
	}

	return sum;
}

int summ(int *co, int i, int k)
{
	return sum_till_exc(co, i)- sum_till_exc(co, i - k + 1);
}

int summ_range(int *co, int i, int j)
{
	return sum_till_exc(co, j + 1) - sum_till_exc(co, i);
}

int last_x(int *co, int x, int size)
{
	return sum_till_exc(co, size) - sum_till_exc(co, size- x);
}

int answer(string s, int k)
{
	int *counts = new int[s.length() - k + 1];
	ss = s.length() - k + 1;
	for (int i = 0; i < s.length() - k + 1; ++i)
	{
		counts[i] = (unequiv(s[i]) + 100000 - summ(counts, i, k)) % 2;
	}


	for (int i = 0; i < s.length(); ++i)
	{
		if (unequiv(s[i]) != summ_range(counts, i - k +1, i) % 2)
		{
			return -1;
		}
	}

int sum = 0;
	for (int i = 0; i < s.length() - k + 1; ++i)
	{
		sum += counts[i];
	}

	delete[] counts;

	
	return sum;
}

int main(int argc, char *argv[])
{
	int T;
	stringstream kk;


	cin >> T;
	int i = 1;
	while (T--)
	{
		kk << "Case #" << i++ << ": ";
		string s;
		int k;
		cin >> s >> k;

		int x = answer(s, k);
		if (x == -1)
		{
			kk << "IMPOSSIBLE";
		}
		else
		{
			kk << x;
		}
		kk << endl;
	}

	
#ifdef ALPER
	ofstream file("C:\\sonuc.txt");
	file << kk.str();
#endif // ALPER

#ifndef ALPER
	cout << kk.str();
#endif

	return 0;
}