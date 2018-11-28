#include <iostream>
#include <fstream>
#include <cmath>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <map>

using namespace std;

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T;
	in >> T;

	for (size_t i = 0; i < T; ++i)
	{
		size_t N, K;
		in >> N >> K;

		size_t a = 0;
		size_t b = 0;

		map<size_t, size_t> data;
		data.insert(make_pair(N, 1));
		for (; K > 0;)
		{
			map<size_t, size_t>::iterator it = data.end();
			--it;
			a = (it->first-1) / 2;
			b = it->first % 2 == 1 ? a : a + 1;
			if (K >= it->second)
			{
				K -= it->second;
				size_t temp = it->second;
				data.erase(it);
				it = data.find(a);
				if (it != data.end())
					it->second += temp;
				else
					data.insert(make_pair(a, temp));
				it = data.find(b);
				if (it != data.end())
					it->second += temp;
				else
					data.insert(make_pair(b, temp));
			}
			else
				break;
		}

	    if (i > 0)
			out << endl;
		out << "Case #" << i+1 << ": " << b << " " << a;
	}

	in.close();
	out.close();
	return 0;
}