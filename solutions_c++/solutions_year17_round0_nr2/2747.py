#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	std::ios_base::sync_with_stdio(0);
	int ttt;
	scanf("%d\n",&ttt);
	for (int tt = 1; tt <= ttt; tt++)
	{
		char ints[30] = { 0 };
		gets_s(ints, 30);
		int l = strlen(ints);
		int k = 0;
		bool f = 1;
		while (k + 1 < l && ints[k] <= ints[k + 1])
			k++;
		if (k == l - 1)
		{
			cout << "Case #" << tt << ": " << ints << endl;
			continue;
		}
		ints[k] = ints[k] - 1;
		while (k > 0 && ints[k] < ints[k - 1])
		{
			ints[k - 1] = ints[k - 1] - 1;
			k--;
		}
		if (k == 0 && ints[k]=='0')
		{
			cout << "Case #" << tt << ": ";
			for (int i = 1; i < l; i++)
				cout << 9;
			cout << endl;
		}
		else
		{
			for (int i = k + 1; i < l; i++)
				ints[i] = '9';
			cout << "Case #" << tt << ": " << ints << endl;
		}
	}
	return 0;
}