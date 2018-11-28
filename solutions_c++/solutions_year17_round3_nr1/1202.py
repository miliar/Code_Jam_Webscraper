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
#include <iomanip>

using namespace std;

template<typename T>
void Print(T obj)
{
	cout << std::setprecision(33) << obj;
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
		int n, k;
		cin >> n >> k;
		struct cake
		{
			cake(double rad, double hi) : R(rad), H(hi) 
			{
				expose = 2 * R * 3.14159265359*H;
				topExpose = R*R*3.14159265359;
			}
			double R;
			double H;
			double expose;
			double topExpose;
		};
		vector<cake> vc;
		vc.reserve(n);
		for (int i = 0; i < n; i++)
		{
			int r, h;
			cin >> r >> h;
			vc.emplace_back(r, h);
		}
		std::sort(vc.begin(), vc.end(), [](cake const & lhs, cake const & rhs)
		{
			return lhs.R > rhs.R;
		});

		auto find_min = [&]()
		{
			auto it = std::min_element(vc.begin(), vc.end(), [](cake const & lhs, cake const& rhs)
			{
				return lhs.expose < rhs.expose;
			});

			if (it == vc.begin())
			{
				auto itNextMin = std::min_element(vc.begin() + 1, vc.end(), [](cake const & lhs, cake const& rhs)
				{
					return lhs.expose < rhs.expose;
				});
				if ((itNextMin->expose - (*it).expose) < it->topExpose - (vc.begin() + 1)->topExpose)
				{
					return itNextMin;
				}
			}
			return it;
		};

		while (vc.size() > k)
		{
			vc.erase(find_min());
		}
		double sum = vc.begin()->topExpose;
		for (int i = 0; i < k; i++)
		{
			sum += vc[i].expose;
		}
		PrintCase(i, sum);
	}

	return 0;
}