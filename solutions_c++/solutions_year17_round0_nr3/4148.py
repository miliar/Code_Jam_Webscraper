// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <cmath>
#include <string>
#include <unordered_set>
#include <set>
#include <map>
#include <algorithm>
#include <functional>

using namespace std;

template<typename T>
void Print(T obj)
{
	cout << obj;
}

template<typename... T>
void PrintCase(int i, T... Objs)
{
	using expand_type = int[];
	cout << "Case #" << i + 1 << ": ";

	expand_type{ 0, (Print(Objs), 0)... };

	cout << endl;
}

int LowestTwoDeegree(long long n)
{
	int out = 0;
	while (n /= 2)
		out++;
	return out;
}

std::map<long long,int, std::greater<long long>> ClalculateSet(std::map<long long,int, std::greater<long long>> map)
{
	std::map<long long,int, std::greater<long long>> out;
	for (auto n : map)
	{
		if (n.first % 2)
		{
			out[n.first / 2] += 2 * n.second;
		}
		else
		{
			out[n.first / 2] += n.second;
			out[n.first / 2 - 1] += n.second;
		}
	}
	return out;
}

int main()
{
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		long long n, k;
		cin >> n >> k;
		std::map<long long,int, std::greater<long long>> map;
		map[n] =1;
		for (int i = 0; i < LowestTwoDeegree(k); i++)
			map = ClalculateSet(map);
		long long remainder_people = k - std::pow<long long>(2, LowestTwoDeegree(k))+1;
		for (auto const & number : map)
		{
			remainder_people -= number.second;
			if (remainder_people <= 0)
			{
				if (number.first % 2)
					PrintCase(i, number.first / 2," ", number.first / 2);
				else
					PrintCase(i, number.first / 2," ", number.first / 2 - 1);
				break;
			}
		}
	}

	return 0;
}