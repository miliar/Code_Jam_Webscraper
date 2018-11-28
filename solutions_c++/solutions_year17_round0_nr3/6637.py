#include <iostream>
#include <vector>
#include <ctime>
#include <fstream>
#include <cstring>
#include <string>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

int main()
{
	fstream in("in.in"), out("out.txt");
	int T;
	in >> T;

	vector<pair<bool, pair<size_t, size_t>>> baths;

	for (int t = 1; t <= T; ++t)
	{
		size_t n, k;

		in >> n >> k;

		baths.clear();
		baths.resize(n + 2, make_pair(false, pair<size_t, size_t>()));
		baths[0].first = true;
		baths[n + 1].first = true;

		size_t rs, ls, mn, mx, y, z;
		long long maximin, maximax;

		for (size_t i = 0; i < k; ++i)
		{
			for (size_t j = 1; j < baths.size() - 1; ++j)
			{
				if (!baths[j].first)
				{
					for (ls = j - 1; ls >= 0; --ls)
					{
						if (baths[ls].first)
							break;
					}

					for (rs = j + 1; rs >= 0; ++rs)
					{
						if (baths[rs].first)
							break;
					}

					mn = min(j - ls - 1, rs - j - 1);
					mx = std::max(j - ls - 1, rs - j - 1);

					baths[j].second.first = mn;
					baths[j].second.second = mx;
				}
			}

			maximin = -1;
			maximax = -1;
			size_t smxmx, smnmx;

			for (size_t j = 1; j < baths.size() - 1; ++j)
			{
				if (!baths[j].first)
				{
					if (maximin < baths[j].second.first)
					{
						smnmx = j;
						maximin = baths[j].second.first;

						smxmx = j;
						maximax = baths[j].second.second;
						
					}
					else if (maximin == baths[j].second.first)
					{
						if (maximax < baths[j].second.second)
						{
							smxmx = j;
							maximax = baths[j].second.second;
						}
					}
				}
			}

			size_t mxmxcounter = 0, mxmncounter = 0;

			for (size_t j = 1; j < baths.size() - 1; ++j)
			{
				if (!baths[j].first)
				{
					if (maximin == baths[j].second.first)
						++mxmncounter;
					
					if (maximax == baths[j].second.second)
						++mxmxcounter;

					if (mxmxcounter > 1 && mxmncounter > 1)
						break;
				}
			}

			if (mxmncounter == 1)
			{
				baths[smnmx].first = true;
				y = baths[smnmx].second.second;
				z = baths[smnmx].second.first;
			}
			else
			{
				baths[smxmx].first = true;
				y = baths[smxmx].second.second;
				z = baths[smxmx].second.first;
			}
		}

		out << "Case #" << t << ": " << y << " " << z << '\n';
	}

	in.close();
	out.close();

	system("pause");
	return 0;
}