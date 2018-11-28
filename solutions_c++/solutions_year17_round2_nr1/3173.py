#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

const double eps = 0.000000001;


double time_of_destination(int x1, int v1, double t_old, int end)
{
	double tt = 1. * (end - x1) / v1;

	if (tt > t_old + eps) return tt;
	else
	{
		return t_old;
	}
}

int main()
{
	ifstream fin("input.in");
	ofstream fout("output.out");


	int t;

	fin >> t;

	for (int test = 0; test < t; test++)
	{
		int d, n;

		fin >> d >> n;

		int pos[1010];
		int v[1010];

		for (int i = 0; i < n; i++)
		{
			fin >> pos[i] >> v[i];
		}

		double t_kek = 1. * (d - pos[n - 1]) / v[n - 1];
		double t_ans;

		for (int i = n - 1; i >= 0; i--)
		{
			t_kek = time_of_destination(pos[i], v[i], t_kek, d);
		}

		t_ans = t_kek;

		double ansss = 1. * d / t_ans;

		fout << "Case #" << test + 1 << ": " << setprecision(12)  << ansss << endl;
	}

	fin.close();
	fout.close();

	return 0;
}