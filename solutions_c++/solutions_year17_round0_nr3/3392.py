
#include <string>
#include <fstream>
//#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	ifstream in("C-small-2-attempt0.in");
	ofstream out("a.out");
	int t;
	in >> t;
	for (int i = 0; i < t; ++i)
	{
		int n, k;
		in >> n >> k;

		multimap<int, int> m = { // size to begin index
			{-n, 0}
		};

		for (int j = 0; j < k - 1; ++j)
		{
			int size = -m.begin()->first;
			int begin = m.begin()->second;
			m.erase(m.begin());
			int mid = (size - 1) / 2 + begin;
			m.insert({-mid + begin, begin});
			m.insert({-begin - size + mid + 1, mid + 1});
		}
		{
			int size = -m.begin()->first;
			int begin = m.begin()->second;
			int mid = (size - 1) / 2 + begin;
			int a = mid - begin;
			int b = begin + size - mid - 1;

			out << "Case #" << (i + 1) << ": " << b << ' ' << a << "" << endl;
		}
	}

	return 0;
}

