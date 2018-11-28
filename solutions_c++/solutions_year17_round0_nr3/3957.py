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

void pancakes()
{
	for (int i = 0; i < cases; ++i)
	{
		string pancakes;
		int fSize;
		cin >> pancakes >> fSize;
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
			max = stalls	   / 2;

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

	stalls();
}