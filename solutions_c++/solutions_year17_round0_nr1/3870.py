#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <map>

using namespace std;

int currCase = 1;
int cases;
vector<string> solution;

void print(const string &solution)
{
	cout << "Case #" << currCase << ": " << solution << '\n';
	++currCase;
}

void swap(bool* &tab, int size, int from, int to)
{
	for (int i = from; i < to; ++i)
	{
		tab[i] = !tab[i];
	}
}

void pancakes()
{
	for (int i = 0; i < cases; ++i)
	{
		string pancakes;
		int fSize, size;
		cin >> pancakes >> fSize;

		size = pancakes.size();

		bool* sides = new bool[size];
		for (int j = 0; j < size; ++j)
		{
			if (pancakes[j] == '+')
			{
				sides[j] = true;
			}
			else
			{
				sides[j] = false;
			}
		}

		int swaps = 0;

		for (int j = 0; j < size; ++j)
		{
			if (!sides[j])
			{
				if ((j + fSize) <= size)
				{
					swap(sides, size, j, j + fSize);
					++swaps;
				}
				else
				{
					swaps = -1;
					break;
				}
			}
		}

		if (swaps == -1) print("IMPOSSIBLE");
		else print(to_string(swaps));
	}
}

int getDigit(long long  pow, long long  number)
{
	return (number / pow) % 10;
}

void numbers()
{
	for (int i = 0; i < cases; ++i)
	{
		long long n, tmp;
		long long pow = 1;
		long long basePow;
		int digits = 0;
		cin >> n;
		tmp = n;

		while (tmp != 0)
		{
			tmp /= 10;
			++digits;
		}

		for (int j = 1; j < digits; ++j) pow *= 10;
		basePow = pow;

		while (pow != 1)
		{
			if (getDigit(pow, n) > getDigit(pow / 10, n))
			{
				long long x = getDigit(pow, n) * pow - 1;
				n = n / pow / 10;
				n *= pow * 10;
				n += x;
				pow = basePow;
			}
			else
			{
				pow /= 10;
			}
		}

		print(to_string(n));
	}
}

void stalls()
{
	for (int i = 0; i < cases; ++i)
	{
		long long n, k;
		cin >> n >> k;

		map<long long, long long> m;
		m.insert(std::make_pair(n, 1));

		long long min = 0;
		long long max = 0;

		for (long long j = 0; j < k; )
		{
			long long stalls = m.rbegin()->first;
			long long copies = m.rbegin()->second;

			if (copies <= k - j)
			{
				m.erase(std::prev(m.end()));
			}

			min = (stalls - 1) / 2;
			max = stalls / 2;

			auto it = m.find(min);
			if (it != m.end())
			{
				it->second += copies;
			}
			else
			{
				m.insert(std::make_pair(min, copies));
			}

			it = m.find(max);
			if (it != m.end())
			{
				it->second += copies;
			}
			else
			{
				m.insert(std::make_pair(max, copies));
			}

			j += copies;
		}

		string str = to_string(max) + " " + to_string(min);
		print(str);
	}
}

int main()
{
	cin >> cases;

	pancakes();
}