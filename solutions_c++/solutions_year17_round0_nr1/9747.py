#include <iostream>
#include <fstream>
#include <stdio.h>
#include <cstdio>
#include <string>
using namespace std;
char s[10];
void flip(int k, int i)
{
	int x, c;
	for (x = i; x < i + k; x++)
		if (s[x] == '+')
			s[x] = '-';
		else
			s[x] = '+';
	
}
int nouses(int l, int k)
{
	int usecount = 0, isplus = 0, i, j;
	for (i = 0; i < l; i++)
		if (s[i] == '+')
			isplus = 1;
		else
		{
			isplus = 0; break;
		}
	if (isplus == 1)
		return usecount;
	for (i = 0, j = l - 1; i <= l - k, j >= k - 1; i++, j--)
	{
		if (s[i] == '-')
		{
			flip(k, i); usecount++;
		}
		if (s[j] == '-')
		{
			flip(k, j - k + 1); usecount++;
		}
	}
	for (i = 0; i < l; i++)
		if (s[i] == '+')
			isplus = 1;
		else
		{
			isplus = 0; break;
		}
	if (isplus == 1)
		return usecount;
	else
	{
		usecount = -1;
		return usecount;
	}
}
void main()
{
	int x, t, l, k, count;
	cin >> t;
	for (x = 1; x <= t; x++)
	{
		cin >> s;
		l = strlen(s);
		cin >> k;
		count = nouses(l, k);
		if (count == -1)
			cout << "Case #" << x << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << x << ": " << count << endl;
	}
	cin.get();
}