// ProblemC.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <map>
#include <set>

using namespace std;


int main()
{
	int t;
	cin >> t;

	for (int i = 0; i < t; ++i)
	{
		unsigned long long n, k;
		cin >> n >> k;

		map<unsigned long long, unsigned long long> m;
		set<unsigned long long> s;

		m[n] = 1;
		s.insert(n);

		unsigned long long min, max;

		while (k > 0)
		{
			unsigned long long l = *s.rbegin();
			if (k >= m[l])
			{
				k -= m[l];
			}
			else
			{
				k = 0;
			}

			min = (l - 1) / 2;
			max = ((l - 1) / 2) + ((l - 1) % 2);

			m[min] += m[l];
			m[max] += m[l];
			s.insert(min);
			s.insert(max);
			m[l] = 0;
			s.erase(l);
		}

		cout << "Case #" << (i + 1) << ": " << max << " " << min << endl;
	}
    return 0;
}

