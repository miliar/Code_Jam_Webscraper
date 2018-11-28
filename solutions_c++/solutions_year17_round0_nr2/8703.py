// 2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

typedef unsigned long long ull;

bool ok(ull &u)
{
	vector<int> jegyek;
	while (u != 0)
	{
		jegyek.push_back(u % 10);
		u /= 10;
	}
	reverse(jegyek.begin(), jegyek.end());
	bool l = true;
	for (int i = 1; i < jegyek.size(); ++i)
	{
		if (jegyek[i] < jegyek[i - 1])
		{
			jegyek[i - 1]--;
			for (int j = i; j < jegyek.size();++j) jegyek[j] = 9;
			l = false;
			break;
		}
	}
	u = 0;
	ull t = 1;
	for (int i = jegyek.size() - 1;i >= 0; i--)
	{
		u += t*jegyek[i];
		t *= 10;
	}
	return l;
}


int main()
{

	ifstream f("2-large.in");
	ofstream g("2-large.out");
	int T;
	f >> T;
	//cin >> T;
	vector<ull> a(T);
	for (int i = 0; i < T; ++i)
		//cin >> a[i];
		f >> a[i];
	for (int i = 0; i < T; ++i)
	{
		while (!ok(a[i]));
		g << "Case #" << i + 1 << ": " << a[i] << endl;

	}
	g.close();
    return 0;
}

