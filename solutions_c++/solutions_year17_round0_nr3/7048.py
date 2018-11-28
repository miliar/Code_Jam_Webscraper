#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

struct tart
{
	int a, f;
};

int main()
{
	fstream fs("a.in");
	int t;
	fs >> t;
	vector<long long> inputn;
	vector<long long> inputk;
	for (int i = 0; i < t; ++i)
	{
		long long n, k;
		fs >> n;
		fs >> k;
		inputn.push_back(n);
		inputk.push_back(k);
	}

	for (int i = 0; i < inputn.size(); ++i)
	{
		int n = inputn[i];
		int k = inputk[i];

		std::vector<tart> tarts;
		tarts.push_back(tart{ 1, n });
		tart last1, last2;
		for (int j = 0; j < k; ++j)
		{
			sort(tarts.begin(), tarts.end(), [](tart a, tart b)->bool {
				int asize = a.f - a.a;
				int bsize = b.f - b.a;
				if (asize == bsize)
					return a.a > b.a;
				return (bsize > asize);
			});
			tart a = tarts.back();
			tart new1 = last1 = tart{ a.a, a.a + (int)floor((a.f - a.a) / 2.0) - 1 };
			tart new2 = last2 = tart{a.a + (int)floor((a.f - a.a) / 2.0) + 1, a.f };
			tarts.pop_back();
			if (new1.a <= new1.f) tarts.push_back(new1);
			if (new2.a <= new2.f) tarts.push_back(new2);
		}
		int size1 =  last1.f - last1.a + 1;
		int size2 = last2.f - last2.a + 1;
		std::cout << "Case #" << i+1 << ": " <<  max(size1, size2) << " " << min(size1, size2) << endl;
	}
	int f;
	cin >> f;

	return 0;
}