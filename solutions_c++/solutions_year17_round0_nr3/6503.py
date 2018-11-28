#include <fstream>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;
using ull = unsigned long long;

struct p {
	p(ull l, ull r, ull s)
		: left(l), right(r), size(s)
	{}

	ull left;
	ull right;
	ull size;
};

int main()
{
	ifstream input("data.txt");
	ofstream output("output.txt");

	unsigned cases;
	ull n, k;

	input >> cases;

	for (int t = 1; t <= cases; t++)
	{
		input >> n >> k;

		vector<p> ps;
		ps.emplace_back(1, n + 2, n);

		for (ull i = 0; i < k; i++)
		{
			ull mi = 0, mx = ps[0].size;
			for(ull i = 0; i < ps.size(); i++)
				if (ps[i].size > mx) {
					mi = i; 
					mx = ps[i].size;
				}

			ull m = ceil(ps[mi].size / 2.0);
			ull tmp = ps[mi].right;
			ps[mi].right = ps[mi].left + m;
			ps[mi].size = ps[mi].right - ps[mi].left - 1;

			ps.emplace(ps.begin() + mi + 1, ps[mi].right, tmp, tmp - ps[mi].right - 1);

			ull ls = ps[mi].size;
			ull rs = ps[mi + 1].size;

			if (i == k - 1) 
				output << "Case #" << t << ": " << max(ls, rs) << " " << min(ls, rs) << endl;
		}

	}

	input.close();
	output.close();

	return 0;
}