#include <fstream>
#include <string>
using namespace std;

int main()
{
	ifstream fin("input.in");
	ofstream fout("ouput.out");
	int t;
	fin >> t;
	for (int i = 0; i < t; ++i)
	{
		string p;
		int k, c = 0;
		fin >> p;
		fin >> k;
		for (int j = 0; j <= p.size() - k; ++j)
			if (p[j] == '-')
			{
				++c;
				for (int l = j; l < j + k; ++l)
				{
					if (p[l] == '-')
						p[l] = '+';
					else
						p[l] = '-';
				}
			}
		bool w = true;
		for (int j = p.size() - k; j < p.size(); ++j)
			if (p[j] == '-')
				w = false;
		fout << "Case #" << i + 1 << ": ";
		if (w == true)
			fout << c << endl;
		else
			fout << "IMPOSSIBLE" << endl;
	}
}