#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main()
{
	ifstream in("C-small.in");
	ofstream out("C-small.out");
	int q;
	in >> q;
	for (int qq = 0; qq < q; ++qq)
	{
		out << "Case #" << qq + 1 << ": ";
		int n, c, m;
		in >> n >> c >> m;
		int cust[2] = { 0 };
		int first = 0;
		int seat[1001] = { 0 };
		for (int i = 0; i < m; ++i)
		{
			int a, b;
			in >> a >> b;
			if (a == 1)
				first++;
			cust[b - 1]++;
			seat[a]++;
		}
		if (first >= max(cust[0], cust[1]))
		{
			out << first << " 0 \n";
		}
		else
		{
			int sum = 0;
			int mx = max(cust[0], cust[1]);
			for (int i = 1; i <= 1000; ++i)
			{
				if (seat[i] > mx)
					sum += seat[i] - mx;
			}
			out << mx << ' ' << sum << '\n';
		}
	}
	in.close();
	out.close();
	return 0;
}