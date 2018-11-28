#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <cassert>

const int minutes = 60 * 30;

int solve(std::vector<std::pair<int, int>> &C, std::vector<std::pair<int, int>> &J)
{
	int* E = new int[minutes * 4 * minutes];
	std::cout << "boo" << std::flush;
	std::sort(C.begin(), C.end());
	std::sort(J.begin(), J.end());
// a = total minutes
// b = minutes by C
// c = 0, last = C, first = C
//     1, last = J, first = C
//     2, last = C, first = J
//     3, last = J, first = J
#define EIJK(a, b, c) \
	E[(c) * (minutes * minutes) + (a) * (minutes) + (b)]
	
	for (int i = 0; i < minutes * 4 * minutes; ++i)
		E[i] = minutes;
	EIJK(0, 0, 0) = 0;
	EIJK(0, 0, 3) = 0;
	
	int closestC = 0, closestJ = 0;
	for (int i = 1; i <= 1440; ++i)
	{
		if (closestC < C.size() && C[closestC].second < i)
			++closestC;
		if (closestJ < J.size() && J[closestJ].second < i)
			++closestJ;
		bool cfree = closestC == C.size() || C[closestC].first >= i;
		bool jfree = closestJ == J.size() || J[closestJ].first >= i;

#if 0
		std::cout << "\t" << i  << " " << "{C: " <<(cfree ? "Y" : "N") << "[";
		if (closestC < C.size())
			std::cout << C[closestC].first << "; " << C[closestC].second;
		std::cout << ") " << " J: " <<(jfree ? "Y" : "N") << "[";
		if (closestJ < J.size())
			std::cout << J[closestJ].first << "; " << J[closestJ].second;
		std::cout << ")} "  << std::flush;
#endif
		assert(cfree || jfree);


		if (cfree)
		{
			for (int b = 0; b < i; ++b)
			{
				int min = minutes;
				min = std::min(min, EIJK(i - 1, b, 0));
				min = std::min(min, EIJK(i - 1, b, 1) + 1);
				if (b + 1 < minutes)
				{
					EIJK(i, b + 1, 0) = min;
				}
				min = minutes;
				min = std::min(min, EIJK(i - 1, b, 2));
				min = std::min(min, EIJK(i - 1, b, 3) + 1);
				if (b + 1 < minutes)
				{
					EIJK(i, b + 1, 2) = min;
				}
			}
		}

		if (jfree)
		{
			for (int b = 0; b < i; ++b)
			{
				int min = minutes;
				min = std::min(min, EIJK(i - 1, b, 1));
				min = std::min(min, EIJK(i - 1, b, 0) + 1);
				EIJK(i, b, 1) = min;
				min = minutes;
				min = std::min(min, EIJK(i - 1, b, 3));
				min = std::min(min, EIJK(i - 1, b, 2) + 1);
				EIJK(i, b, 3) = min;
			}
		}
	}
	auto res = std::min(std::min(std::min(EIJK(1440, 720, 1)+1, EIJK(1440, 720, 0)), EIJK(1440, 720, 2) + 1), EIJK(1440, 720, 3));
	delete[] E;
	return res;
}

int main()
{
	std::ios_base::sync_with_stdio(0);

	int T;
	std::cin >> T;
	std::vector<std::pair<int, int>> C, J;
	for (int i = 0; i < T; ++i)
	{
		int Ac, Aj;
		std::cin >> Ac >> Aj;
		C.resize(Ac); J.resize(Aj);
		for (int j = 0; j < Ac; ++j)
			std::cin >> C[j].first >> C[j].second;
		for (int j = 0; j < Aj; ++j)
			std::cin >> J[j].first >> J[j].second;
		auto res = solve(C, J);
		std::cout << "Case #" << i + 1 << ": " << std::setprecision(16) << res << std::endl;
	}
	return 0;
}
