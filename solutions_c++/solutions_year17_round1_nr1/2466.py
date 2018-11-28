#include <fstream>
#include <vector>
using namespace std;

int main()
{
	ifstream fin("input.in");
	ofstream fout("ouput.out");

	int t;
	fin >> t;
	for (int i = 0; i < t; ++i)
	{
		int r, c;
		fin >> r >> c;
		vector<char> v;
		for (int j = 0; j < r*c; ++j)
		{
			char l;
			fin >> l;
			v.push_back(l);
		}

		for (int k = 0; k < c; ++k)
		{
			for (int j = 0; j < r; ++j)
				if (v[j * c + k] != '?')
				{
					for (int m = j; m < r; ++m)
					{
						if (v[m * c + k] == v[j * c + k] || v[m * c + k] == '?')
							v[m * c + k] = v[j * c + k];
						else
							break;
					}
					for (int m = j; m >= 0; --m)
					{
						if (v[m * c + k] == v[j * c + k] || v[m * c + k] == '?')
							v[m * c + k] = v[j * c + k];
						else
							break;
					}
				}
			for (int j = r-1; j >= 0; --j)
				if (v[j * c + k] != '?')
				{
					for (int m = j; m >= 0; --m)
					{
						if (v[m * c + k] == v[j * c + k] || v[m * c + k] == '?')
							v[m * c + k] = v[j * c + k];
						else
							break;
					}
					for (int m = j; m < r; ++m)
					{
						if (v[m * c + k] == v[j * c + k] || v[m * c + k] == '?')
							v[m * c + k] = v[j * c + k];
						else
							break;
					}
				}
		}

		for (int k = 0; k < r; ++k)
		{
			for (int j = 0; j < c; ++j)
				if (v[k * c + j] != '?')
				{
					for (int m = j; m < c; ++m)
					{
						if (v[k * c + m] == v[k * c + j] || v[k * c + m] == '?')
							v[k * c + m] = v[k * c + j];
						else
							break;
					}
					for (int m = j; m >= 0; --m)
					{
						if (v[k * c + m] == v[k * c + j] || v[k * c + m] == '?')
							v[k * c + m] = v[k * c + j];
						else
							break;
					}
				}
			for (int j = c - 1; j >= 0; --j)
				if (v[k * c + j] != '?')
				{
					for (int m = j; m >= 0; --m)
					{
						if (v[k * c + m] == v[k * c + j] || v[k * c + m] == '?')
							v[k * c + m] = v[k * c + j];
						else
							break;
					}
					for (int m = j; m < c; ++m)
					{
						if (v[k * c + m] == v[k * c + j] || v[k * c + m] == '?')
							v[k * c + m] = v[k * c + j];
						else
							break;
					}
				}
		}

		fout << "Case #" << i+1 << ": " << endl;
		for (int j = 0; j < r; ++j)
		{
			for (int k = 0; k < c; ++k)
				fout << v[j * c + k];
			fout << endl;
		}
	}
}