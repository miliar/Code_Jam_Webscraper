#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>

#define LIMIT 1000

double compute_rel(int n, int k, std::vector<double> &v)
{
	double res = 1;
	if(n == k)
	{
		for(int i = 0; i < k; ++i) 
		{
			res *= std::min(v[i], 1.0);
		}
		return res;
	}
	return 0;
}

int main(int argc, char **argv)
{
	int t, ct;

	std::cin >> t;
	for(ct = 0; ct < t; ++ct)
	{
		std::vector<double> p;
		double u;
		int n, k;
		std::cin >> n >> k;
		std::cin >> u;
		for(int i = 0; i < n; ++i)
		{
			double pd;
			std::cin >> pd;
			p.push_back(pd);
		}

		std::sort(p.begin(), p.end());

		int b = n - k;
		while(u > 0)
		{
			int i;
			for(i = b; i < n - 1; ++i)
			{
				if(p[i] < p[i + 1]) 
				{
					int nums = 1 + i - b;
					double diff = std::min(u, (p[i + 1] - p[i]) * nums);
					u -= diff;
					diff /= nums;
					for(int j = b; j < i + 1; ++j)
					{
						p[j] += diff;
					}
					break;
				}
			}
			if(i == n - 1)
			{
				double inc = b == 0 ? u / n : u / b;
				u = 0;
				for(i = b; i < n; ++i)
				{
					p[i] += inc;
				}
			}
		}
/*
		for(int i = 0; i < n; ++i)
		{
			std::cout << p[i] << " ";
		}
		std::cout << "\n";
*/
		printf("Case #%d: %.8f\n", (ct+1), compute_rel(n, k, p)); 
	}

	return 0;
}
