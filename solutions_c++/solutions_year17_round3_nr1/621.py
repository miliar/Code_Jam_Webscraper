#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <cassert>

//using namespace std;

const double pi = 3.141592653589793238462643383279502884197169399375105820974944592307816406286;

double solve(int N, int K, std::vector<std::pair<double, double>> &RH)
{
	auto h = new double[(K + 1) * N]; // select K last = N
	std::sort(RH.begin(), RH.end(), [](const std::pair<double, double> &a, const std::pair<double, double> &b) { return a.first == b.first ? a.second > b.second : a.first < b.first; });
	// i = 0..K
	// j = 0..N-1
#define HIJ(a, b)\
	h[(a) * N + b]
	for (int i = 0; i < N; ++i)
		HIJ(0, i) = 0.0;
	for (int i = 0; i < N; ++i)
		HIJ(1, i) = pi * (RH[i].first * RH[i].first) + 2.0 * pi * RH[i].first * RH[i].second;
	for (int kk = 2; kk <= K; ++kk)
	{
		for (int id = 0; id < N; ++id)
		{
			double max = 0.0;
			double Rcurr = RH[id].first,
				   Hcurr = RH[id].second;
			for (int prev = 0; prev < id; ++prev)
			{
				double Rprev = RH[prev].first;
				assert(Rprev <= Rcurr);
				double s = pi * (Rcurr * Rcurr - Rprev * Rprev) + 2.0 * pi * Rcurr * Hcurr;
				double sstack = HIJ(kk - 1, prev);
//				std::cout << "s: " << s << " sstack: " << sstack << std::endl;
				max = std::max(max, s + sstack);
			}
			HIJ(kk, id) = max;
		}
	}
#if 0
	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j <= K; ++j)
			std::cout << HIJ(j, i) << "\t";
		std::cout << std::endl;
	}
#endif
	double res  = 0;
	for (int i = 0; i < N; ++i)
		res = std::max(res, HIJ(K, i));
	delete h;
	return res;
}

int main()
{
	std::ios_base::sync_with_stdio(0);

	int T;
	std::cin >> T;
	std::vector<std::pair<double, double>> RH;
	for (int i = 0; i < T; ++i)
	{
		int K, N;
		double R, H;
		std::cin >> N >> K;
		RH.resize(N);
		for (int j = 0; j < N; ++j)
			std::cin >> RH[j].first >> RH[j].second;
		auto res = solve(N, K, RH);
		std::cout << "Case #" << i + 1 << ": " << std::setprecision(16) << res << std::endl;
	}
	return 0;
}
