// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <cmath>
#include <unordered_set>
#include <algorithm>
#include <iomanip>

using namespace std;

template<typename T>
void Print(T obj)
{
	cout << fixed << setprecision(7) << obj;
}

template<typename... T>
void PrintCase(int i, T... Objs)
{
	using expand_type = int[];
	cout << "Case #" << i + 1 << ": ";

	expand_type{ 0, (Print(Objs), 0)... };

	cout << endl;
}

int main()
{
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		int n, d;
		cin >> d >> n;
		struct info
		{
			info(int s, int sp,int d) : start(s), speed(sp)
			{
				time = static_cast<double>(d - start) / static_cast<double>(speed);
			}
			int start;
			int speed;
			double time;
		};
		vector<info> vec;


		for (int j = 0; j < n; j++)
		{
			int start, speed;
			cin >> start >> speed;
			vec.emplace_back(start, speed,d);
		}

		double t = (*max_element(vec.begin(), vec.end(), [](info const & lhs, info const & rhs)
		{
			return lhs.time < rhs.time;
		})).time;

			PrintCase(i, static_cast<double>(d)/t);
	}

	return 0;
}

