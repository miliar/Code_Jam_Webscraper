#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <string>
#include <ctime>

// #include <cstdio>
//#include <sstream>

using namespace std;

#define TASK "task3"

void printvec(vector<int> v)
{
	if (v[0] != 0)
		cout << v[0];
	for (int j = 1; j < v.size(); j++)
	{
		cout << v[j];
	}
	cout << endl;
}

int main()
{
//	clock_t begin = clock();

	freopen(TASK ".in", "r", stdin);
	freopen(TASK ".out", "w", stdout);
	ios_base::sync_with_stdio(false);

	int t; // kolvo_testovih_zadac;
	int n;
	int k;
	int intA, intB;
	int Ls, Rs;
	double doubleA, doubleB;
	vector<int> vec;

	cin >> t;

	for (int i = 0; i < t; i++)
	{
		cin >> n;
		cin >> k;
		vec.clear();
		vec.push_back(n);
//		printvec(vec);
		for (int j = 0; j < k-1; j++)
		{
			sort(vec.begin(), vec.end());
			intA = vec[vec.size() - 1];
			vec.pop_back();
			if (intA & 1)
			{
				// нечетное
				intB = (intA - 1) / 2;
				if (intB !=0)
					vec.push_back(intB);
				if (intB != 0)
					vec.push_back(intB);
			}
			else
			{
				// четное
				intB = (intA) / 2 - 1;
				if (intB != 0)
					vec.push_back(intB);
				intB = (intA) / 2;
				if (intB != 0)
					vec.push_back(intB);
			}
//			printvec(vec);
		}
		sort(vec.begin(), vec.end());
		intA = vec[vec.size() - 1];
		vec.pop_back();
		if (intA & 1)
		{
			// нечетное
			Ls = (intA - 1) / 2;
			Rs = (intA - 1) / 2;
		}
		else
		{
			// четное
			Ls = (intA) / 2 - 1;
			Rs = (intA) / 2;
		}
		cout << "Case #" << i + 1 << ": " << max(Ls,Rs) << " " << min (Ls,Rs) << endl;

	}
//	clock_t end = clock();
//	long elapsed_secs = end - begin;
//	cout << "time" << elapsed_secs; 
}