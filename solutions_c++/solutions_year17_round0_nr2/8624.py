#include <set>
#include <numeric>
#include <memory>
#include <vector>
#include <deque>
#include <list>
#include <forward_list>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <functional>
#include <map>
#include <iterator>
#include <string>
#include <iostream>
#include <math.h>

#include <fstream>
#include "inf_int.h"
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	ifstream in{ "input.txt" , ios::in };
	ofstream out{ "output.txt", ios::out };

	int testCase;
	in >> testCase;

	for (int i = 0; i < testCase; i++)
	{
		string limit, sortedLimit;
		in >> limit;
		
		sortedLimit = limit;
		sort(sortedLimit.begin(), sortedLimit.end());
		


		if (sortedLimit == limit)
		{
			out << "Case #" << (i + 1) << ": " << limit << endl;
			continue;
		}
		else
		{
			inf_int inf{ limit.c_str() };
			int off = 1;
			inf_int multiplier = 1;
			inf_int ten = 10;
			while (true)
			{
				string infInt = inf.to_string();
				reverse(infInt.begin(), infInt.end());
				inf_int n{ ((infInt[infInt.size() - off] - '0' + 1) * multiplier) };
				inf = inf - n;

				string reversedInf = inf.to_string();
				string sortedInf = inf.to_string();
				sort(sortedInf.begin(), sortedInf.end());
				reverse(reversedInf.begin(), reversedInf.end());
				if (sortedInf == reversedInf)
				{
					break;
				}

				++off;
				multiplier = multiplier * ten;
			}


			out << "Case #" << (i + 1) << ": " << inf << endl;
			continue;
		}
	}

	return 0;
}
