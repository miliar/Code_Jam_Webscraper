#include <iostream>
#include <fstream>
#include <algorithm>
#include <iomanip>

using namespace std;

struct my_pair
{
	long long r;
	long long h;
};

bool comp(my_pair a, my_pair b)
{
	return (a.h * a.r > b.h * b.r);
}

const double pi = acos(-1);
const double eps = 0.0000000001;

int main()
{

	ifstream fin("input.in");
	ofstream fout("output.out");

	int t;

	fin >> t;


	for (int test = 0; test < t; test++)
	{
		long long n, k;

		fin >> n >> k;

		my_pair p[1000];

		for (int i = 0; i < n; i++)
		{
			fin >> p[i].r >> p[i].h;
		}

		sort(p, p + n, comp);


		double max_ans = -100.0;

		for (int i = 0; i < n; i++)
		{
			double ans = 0.0;

			int id = 0;
			ans += pi * p[i].r * p[i].r + 2 * pi * p[i].r * p[i].h;

			for (int j = 0; j < n; j++)
			{
				if (id < k - 1 && i != j && p[j].r <= p[i].r)
				{
					ans += 2 * pi * p[j].h * p[j].r;
					id++;
				}
			}

			if (ans > max_ans + eps) max_ans = ans;
		}

		fout << "Case #" << test + 1 << ": " << setprecision(13) << max_ans << endl;

	}


	fin.close();
	fout.close();


	return 0;
}