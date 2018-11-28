#include <iostream>
#include <fstream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <string>
using namespace std;

struct pancake
{
	string pattern;
	size_t flipper;
};

void PancakeFlipper(int argc, char** argv)
{
	ifstream in(argv[1]);
	ofstream out(argv[2]);

	size_t c;
	in >> c;

	vector<pancake> cases;
	for (size_t i = 0; i < c; i++)
	{
		cases.push_back(pancake());
		in >> cases[i].pattern;
		in >> cases[i].flipper;
	}


	in.close();

	for (size_t i = 0; i < c; ++i)
	{
		string pan = cases[i].pattern;
		size_t k = cases[i].flipper;

		bool found = false;
		int count = 0;


		for (size_t j = 0; j < pan.size(); j++)
		{
			//find first -
			size_t pos = pan.find('-');

			if (pos == string::npos)
			{
				break;
			}

			count++;

			if (pos < pan.size() - k + 1)
				// swap k elements
				for (size_t l = 0; l < k; l++)
					pan[pos + l] = pan[pos + l] == '-' ? '+' : '-';
		}

		if(pan.find('-') == string::npos)
			out << "Case #" << i + 1 << ": " << count << endl;
		else
			out << "Case #" << i + 1 << ": IMPOSSIBLE" << endl;
			
	}

	out.close();
}