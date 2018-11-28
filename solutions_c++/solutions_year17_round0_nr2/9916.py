// ConsoleApplication1.cpp : Defines the entry point for the console application.
//
#define _CRT_SECURE_NO_WARNINGS
//#include "stdafx.h"
/*#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
//#include <graphic.h>

using namespace std;

/*const int MAXLEN = 10000;

struct num
{
	int len;
	int d[MAXLEN];

	num()
	{
		len = 1;
		memset(d, 0, MAXLEN * sizeof(MAXLEN));
	}
};

int numsum(vector<int> vi)
{
	int a = 0;
	for (int i = 0; i < vi.size(); i++)
	{
		a += vi[i];
	}
	return a;
}

int main()
{
	vector <int >

	/*long long n;
	cin >> n;
	if (n < 10) { cout << n; return 0; }
	vector<int> vi, vres;
	int sum = 0;
	while (n != 0)
	{
		vi.push_back(n % 10);
		sum += n % 10;
		n /= 10;
	}

	vres = vi;

	for (int i = 0; i < vi.size() - 1; i++)
	{
		if (vi[i] < 9)
		{
			vi[i + 1]--;
			vi[i] = 9;
			int sum2 = numsum(vi);
			if (sum2 > sum)
			{
				vres = vi;
				sum = sum2;
			}
		}
	}

	for (int i = 0; i < vres.size(); i++)
	{
		if (vres[vres.size() - i - 1] == 0) continue;
		else cout << vres[vres.size() - i - 1];
	}*/



	///ÄÎÐÅØÀÒÜ!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	/*int n;
	cin >> n;
	string s;
	cin >> s;
	long long res = 0;
	int vbef = 0, vaft = 0;
	for (int i = 0; i < n; i++)
	{
		if (s[i] == 'K')
		{
			for (int j = i - 1; j > -1; j--)
			{
				if (s[j] == 'V') vbef++;
				else break;
			}
			for (int j = i + 1; j < n; j++)
			{
				if (j == n - 1 && s[j] == 'V') vaft = 150;
				if (s[j] == 'V') vaft++;
				else break;
			}


			if (vbef <= vaft)
			{
				string str1 = s.substr(0, i+1), str2 = s.substr(i+1,s.length() - i);
				int j = i;
				while (j > 0 && s[j - 1] == 'V')
				{
					
				}
			}
		}
		
		vbef = vaft = 0;
	}
	cout << s;
	cout << res;
	



    return 0;
}*/

#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

/*int numsum(vector<int> vi)
{
	int a = 0;
	for (int i = 0; i < vi.size(); i++)
	{
		a += vi[i];
	}
	return a;
}*/

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	cin >> t;
	int p = 0;
	long long n;
	while (t-- > 0)
	{
		cin >> n;
		if (n < 10) { p++; cout << "Case #" << p << ": " << n << endl; continue; }
		vector <int> vi;
		while (n > 0)
		{
			vi.push_back(n % 10);
			n /= 10;
		}
		for (int i = 0; i < vi.size() - 1; i++)
		{
			/*if (vi[i] == vi[i + 1] == 0)
			{
				vi[i + 1]--;
				vi[i] = 9;
				for (int j = 0; j < i; j++)
					vi[j] = 9;
			}*/
			if (vi[i] <= vi[i + 1])
			{
				if (vi[i] == vi[i + 1] != 0) continue;
				vi[i + 1]--;
				vi[i] = 9;
				for (int j = 0; j < i; j++)
					vi[j] = 9;
			}
			
		}
		vector<int> vres;
		if (vi[vi.size() - 1] > 0)
			vres.push_back(vi[vi.size() - 1]);
		for (int i = 1; i < vi.size(); i++)
			vres.push_back(vi[vi.size() - i - 1]);
		p++;
		cout << "Case #" << p << ": ";
		for (int i = 0; i < vres.size(); i++)
			cout << vres[i];
		cout << endl;
		/*for (int i = 0; i < vi.size(); i++)
			cout << vi[i];*/

	}
	return 0;
}