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
		double u;
		cin >> u;
		vector<int> vc;

		int uI = static_cast<int>(floor(u*10000 + 0.5));

		for (int j = 0; j < n; j++)
		{
			double p;
			cin >> p;
			vc.push_back(static_cast<int>(floor(p * 10000 + 0.5)));
		}

		std::sort(vc.begin(), vc.end());

		auto lessCount = [&]()
		{
			int c = 0;
			for (int i = 0; i < n-1; i++)
			{
				if (vc[i] != vc[i + 1])
					return i;
			}
			return n - 1;
		};

		while (uI > 0)
		{
			int lastequalIndex = lessCount();
			if (lastequalIndex + 1 != vc.size())
			{
				int diff = vc[lastequalIndex + 1] - vc[lastequalIndex];
				if (diff*(lastequalIndex + 1) <= uI)
				{
					for (int i = 0; i <= lastequalIndex; i++)
					{
						vc[i] += diff;
					}
					uI -= diff*(lastequalIndex + 1);
				}
				else
				{
					int ceil = uI / (lastequalIndex + 1);
					int remainder = uI % (lastequalIndex + 1);
					for (int i = 0; i <= lastequalIndex; i++)
					{
						vc[i] += ceil;
					}
					for (int i = 0; i < remainder; i++)
					{
						vc[i] += 1;
					}
					uI = 0;
				}
			}
			else
			{
				int ceil = uI / (lastequalIndex + 1);
				int remainder = uI % (lastequalIndex + 1);
				for (int i = 0; i <= lastequalIndex; i++)
				{
					vc[i] += ceil;
				}
				for (int i = 0; i < remainder; i++)
				{
					vc[i] += 1;
				}
				uI = 0;
			}
		}

		double mult = 1;
		for (int i = 0; i < vc.size(); i++)
		{
			mult *= static_cast<double>(vc[i])/10000;
		}

		PrintCase(i,mult);
	}

	return 0;
}