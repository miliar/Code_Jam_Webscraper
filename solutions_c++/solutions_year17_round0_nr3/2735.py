#include <iostream>
#include <vector>
#include <queue>
#include <deque>
#include <utility>
#include <cmath>
#include <list>
#include <string>
#include <fstream>
#define mp make_pair
#define pb push_back

using namespace std;

int main()
{
	ifstream in;
	in.open("C-large.in");
	ofstream out;
	out.open("C-large.out");
	int q;
	in >> q;
	long long dou[61];
	long long pow = 2;
	dou[0] = 1;
	for (int i = 1; i < 61; i++)
	{
		dou[i] = pow;
		pow *= 2;
	}
	for (int w = 0; w < q; w++)
	{
		out << "Case #" << w + 1 << ": ";
		long long a, b, k = 1;
		in >> a >> b;
		int al = 0, bl = 0;
		while (dou[al+1]-1 < a)
			al++;
		//al--;
		while (dou[bl+1]-1 < b)
			bl++;
		//bl--;
		if (b > dou[al]-1)
		{
			out << 0 << ' ' << 0 << endl;
			continue;
		}
		long long lastl = a - dou[al]+1;
		//out << dou[al - bl]-1 << ' ' << lastl / dou[bl] << ' ' << (lastl % dou[bl] >= (b - dou[bl]+1)) << endl;
		long long res = dou[al - bl] - 1 + lastl / dou[bl] + (lastl % dou[bl] >= (b - dou[bl] + 1));
		out << res / 2 << ' ' << res / 2 + (res % 2) - 1 << endl;
	}
	return 0;
}