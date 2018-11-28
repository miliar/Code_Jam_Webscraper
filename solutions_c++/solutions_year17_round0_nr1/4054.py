// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <cmath>
#include <string>
#include <unordered_set>

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



int main()
{
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		string str;
		cin >> str;
		int k;
		cin >> k;
		int out = 0;
		vector<bool> inverse(str.length(), false);

		auto make_k_inverse = [&](int n)
		{
			for (int i = n; i < n + k; i++)
			{
				inverse[i] = !inverse[i];
			}
		};

		auto last_k_happy = [&]()
		{
			for (int i = str.length() - k; i < str.length(); i++)
				if ((str[i] == '-' && !inverse[i]) || (str[i] == '+' && inverse[i]))
					return false;
			return true;
		};

		for (int j = 0; j < str.length() - k; j++)
		{
			if ((str[j] == '-' && !inverse[j]) || (str[j] == '+' && inverse[j]))
			{
				out++;
				make_k_inverse(j);
			}
		}

		if (last_k_happy())
			PrintCase(i, out);
		else
		{
			make_k_inverse(str.length() - k);
			out++;
			if (last_k_happy())
				PrintCase(i, out);
			else
				PrintCase(i, "IMPOSSIBLE");
		}
	}

	return 0;
}

