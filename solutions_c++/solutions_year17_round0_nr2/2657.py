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
	in.open("B-large.in");
	ofstream out;
	out.open("B-large.out");
	long long dec[18];
	long long pow = 1;
	for (int i = 0; i < 18; i++)
	{
		dec[i] = pow;
		pow *= 10;
	}
	int q;
	in >> q;
	for (int w = 0; w < q; w++)
	{
		out << "Case #" << w + 1 << ": ";
		long long n;
		in >> n;
		if (n/10 == 0)
		{
			out << n << endl;
		}
		else
		{
			if (n == 1000000000000000000)
			{
				out << 999999999999999999 << endl;
			}
			else
			{
				int s = 0;
				while (n / dec[s] != 0)
					s++;
				int * num = new int[s];
				int k = s;
				s--;
				long long res = n;
				while (s >= 0)
				{
					num[s] = n / dec[s];
					n = n%dec[s];
					s--;
				}
				int bad = -1;
				for (int i = k - 1; i > 0; i--)
				{
					if (num[i] <= num[i-1])
						continue;
					else
					{
						bad = i;
						num[i]--;
						break;
					}
				}
				if (bad != -1)
				{
					while (bad < k-1 && num[bad] < num[bad + 1])
					{
						bad++;
						num[bad]--;
					}
					res = res - res%dec[bad] - 1;
					out << res << endl;
				}
				else
					out << res << endl;
			}
		}
	}

	return 0;
}