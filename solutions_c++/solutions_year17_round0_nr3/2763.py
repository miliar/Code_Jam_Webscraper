#include <iostream>
#include <fstream>


using namespace std;


struct row
{
	long long kol1;
	long long tree1;
	long long kol2;
	long long tree2;
};

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

		long long kol_del = 0;

		row x = { 1, n, 0, n + 1 };

		while (kol_del < k)
		{
			row x1;

			long long sum = x.kol1 * x.tree1 + x.kol2 * x.tree2 - (x.kol1 + x.kol2);
			long long mod = sum % ((x.kol1 + x.kol2) * 2);

			x1.tree1 = sum / ((x.kol1 + x.kol2) * 2);
			x1.tree2 = (sum / ((x.kol1 + x.kol2) * 2)) + 1;
			x1.kol2 = sum % ((x.kol1 + x.kol2) * 2);
			x1.kol1 = (x.kol1 + x.kol2) * 2 - (sum % ((x.kol1 + x.kol2) * 2));

			x = x1;
			kol_del = kol_del * 2 + 1;

		}
		long long tmp = kol_del / 2;

		long long sum = x.kol1 * x.tree1 + x.kol2 * x.tree2;

		if ((x.tree1 > x.tree2 && x.kol1 > x.kol2) || (x.tree1 < x.tree2 && x.kol1 < x.kol2))
		{
			if (x.kol1 > x.kol2) tmp += (x.kol1 - x.kol2) / 2; else tmp += (x.kol2 - x.kol1) / 2;
			if (k <= tmp)
			{
				if (x.tree1 > x.tree2 && x.kol1 != 0) fout << "Case #" << test + 1 << ": " << x.tree1 << " " << x.tree1 << endl;
				else if (x.tree1 < x.tree2 && x.kol2 != 0) fout << "Case #" << test + 1 << ": " << x.tree2 << " " << x.tree2 << endl;

				if (x.tree1 > x.tree2 && x.kol1 == 0) fout << "Case #" << test + 1 << ": " << x.tree2 << " " << x.tree2 << endl;
				if (x.tree1 < x.tree2 && x.kol2 == 0) fout << "Case #" << test + 1 << ": " << x.tree1 << " " << x.tree1 << endl;
			}
			else
			{
				if (x.tree1 > x.tree2) fout << "Case #" << test + 1 << ": " << x.tree1 << " " << x.tree2 << endl;
				else fout << "Case #" << test + 1 << ": " << x.tree2 << " " << x.tree1 << endl;
			}
		}
		else
		{
			if (x.tree1 > x.tree2) tmp += x.kol1; else tmp += x.kol2;
			if (k <= tmp)
			{
				if (x.tree1 > x.tree2) fout << "Case #" << test + 1 << ": " << x.tree1 << " " << x.tree2 << endl;
				else fout << "Case #" << test + 1 << ": " << x.tree2 << " " << x.tree1 << endl;
			}
			else
			{
				if (x.tree1 > x.tree2) fout << "Case #" << test + 1 << ": " << x.tree2 << " " << x.tree2 << endl;
				else fout << "Case #" << test + 1 << ": " << x.tree1 << " " << x.tree1 << endl;
			}
		}

	}

	fin.close();
	fout.close();

	return 0;
}