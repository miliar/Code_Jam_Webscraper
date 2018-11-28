// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <cmath>
#include <unordered_set>
#include <algorithm>
#include <iomanip>
#include <string>



//2
//6 2 0 2 0 2 0
//3 1 0 2 0 0 0


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
		int n, R, O, Y, G, B, V;
		cin >> n >> R >> O >> Y >> G >> B >> V;

		struct unicorns
		{
			unicorns(int c, char col) : count(c), color(col) {}
			int count;
			char color;
			bool operator ==(unicorns const & other) const
			{
				return (color == other.color);
			}
		};

		vector<unicorns> uni;
		uni.emplace_back(R, 'R');
		uni.emplace_back(O, 'O');
		uni.emplace_back(Y, 'Y');
		uni.emplace_back(G, 'B');
		uni.emplace_back(B, 'B');
		uni.emplace_back(V, 'V');

		string out;

		unicorns& first = *std::max_element(uni.begin(), uni.end(), [&](unicorns const & l, unicorns const & r)
		{
			return l.count < r.count;
		});

		out += first.color;
		first.count--;

		for (int i = 0; i < n - 1; i++)
		{
			unicorns & curr = *std::max_element(uni.begin(), uni.end(), [&](unicorns const & l, unicorns const & r)
			{
				if (l.color == out.back())
					return true;
				if (r.color == out.back())
					return false;
				if (l.count == r.count)
				{
					if (l == first)
						return false;
					if (r == first)
						return true;
				}
				return l.count < r.count;
			});
			if (curr.count == 0)
				break;
			if (curr.color == out.back())
				break;
			out += curr.color;
			curr.count--;
		}

		if (out.length() != n || out.back() == out.front())
			PrintCase(i, "IMPOSSIBLE");
		else
			PrintCase(i, out);
	}

	return 0;
}

