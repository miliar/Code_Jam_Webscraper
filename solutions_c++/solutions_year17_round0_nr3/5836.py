#include <iostream>
#include <fstream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
	ifstream in("input.txt");

	size_t T;

	in >> T;

	ofstream out("output.txt");

	for (int z = 1; z <= T; ++z)
	{
		size_t N, K;

		in >> N >> K;

		vector<char> taken(N + 2);
		taken[0] = 1;
		taken[N + 1] = 1;

		vector<size_t> Ls(N + 2);
		vector<size_t> Lr(N + 2);

		size_t l, r, mid;
		for (size_t i = 0; i < K; ++i)
		{
			l = 0;
			r = N + 1;

			mid = (r - l) / 2;
			while (taken[mid])
			{
				if (Ls[mid] >= Lr[mid])
				{
					--Ls[mid];
					r = mid;
				}
				else
				{
					--Lr[mid];
					l = mid;
				}

				mid = (r + l) / 2;
			}

			taken[mid] = 1;
			Ls[mid] = mid - l - 1;
			Lr[mid] = r - mid - 1;
		}

		out << "Case #" << z << ": " << max(Ls[mid], Lr[mid]) << " " << min(Ls[mid], Lr[mid])<< "\n";
	}
}