#include <fstream>
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
		vector<long double> v;
		long double d, n;
		fin >> d >> n;
		for (int j = 0; j < n; ++j)
		{
			long double k, s, l;
			fin >> k >> s;
			l = (d - k) / s;
			v.push_back(l);
		}
		fout << "Case #" << i+1 << ": " << d / *max_element(v.begin(), v.end()) << endl;
	}
}