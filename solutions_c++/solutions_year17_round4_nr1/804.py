#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int q;
	in >> q;
	for (int qq = 0; qq < q; ++qq)
	{
		out << "Case #" << qq + 1 << ": ";
		int n, p;
		in >> n >> p;
		vector<int> a;
		for (int i = 0; i < p; ++i)
			a.push_back(0);
		int b;
		for (int i = 0; i < n; ++i)
		{
			in >> b;
			a[b%p]++;
		}
		int sum = a[0];
		if (p == 4)
		{
			sum += a[2] / 2;
			while (a[1] > 0 && a[3] > 0)
			{
				sum++;
				a[1]--;
				a[3]--;
			}
			sum += (a[1]+3) / 4;
			sum += (a[3]+3) / 4;
			if (a[1] % 4 == 0 && a[3] % 4 == 0 && a[2] % 2 == 1)
				sum++;
		}
		if (p == 2)
		{
			sum += (a[1]+1) / 2;
		}
		if (p == 3)
		{
			while (a[1] > 0 && a[2] > 0)
			{
				sum++;
				a[1]--;
				a[2]--;
			}
			sum += (a[1] + 2) / 3;
			sum += (a[2] + 2) / 3;
		}
		out << sum << '\n';
	}
	in.close();
	out.close();
	return 0;
}