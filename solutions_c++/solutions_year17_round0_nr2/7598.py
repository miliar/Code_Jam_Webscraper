#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	ifstream fin("input.in");
	ofstream fout("ouput.out");
	int t;
	fin >> t;
	for (int i = 0; i < t; ++i)
	{
		string n;
		fin >> n;
		int stop = n.size()-1;
		vector<char> v(n.size(), '0');

		for(int j = 0; j < n.size()-1; ++j)
			if(n[j] > n[j+1])
				{stop = j; break;}

		while (stop != n.size() - 1 && stop != 0 && n[stop - 1] == n[stop])
			--stop;

		for (int j = stop + 1; j < n.size(); ++j)
			v[j] = '9';

		bool rep = true;
		if(n.size() == 1)
			rep = false;
		for (int j = 0; j < stop; ++j)
			if (n[j] != n[j + 1] || stop == n.size() - 1)
				rep = false;

		if(stop != n.size()-1 && stop != 0)
			n[stop]--;

		for (int j = 0; j <= stop; ++j)
			v[j] = n[j];

		if (rep == true)
		{
			v[0]--;
			for (int j = 1; j <= stop; ++j)
				v[j] = '9';
		}

		if (v[0] == '0')
			v.erase(v.begin());

		fout << "Case #" << i + 1 << ": ";
		for (auto it : v)
			fout << it;
		fout << endl;
	}
}