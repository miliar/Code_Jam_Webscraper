#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;

const double pi = acos(-1);

struct Pancake
{
	uint64_t R;
	uint64_t H;
};

static inline double SideSurfaceArea(const Pancake& Pancake)
{
	return 2.0 * pi * Pancake.R * Pancake.H;
}

void main()
{
	uint64_t T;
	cin >> T;
	for (uint64_t t = 0; t < T; ++t)
	{
		uint64_t N, K;
		cin >> N;
		cin >> K;
		vector<Pancake> Pancakes(N);
		for (uint64_t n = 0; n < N; ++n)
		{
			uint64_t R, H;
			cin >> R;
			cin >> H;
			Pancakes[n] = { R, H };
		}
		sort(Pancakes.begin(), Pancakes.end(), [](const Pancake& LHS, const Pancake& RHS) { return LHS.R == RHS.R ? LHS.H < RHS.H : LHS.R > RHS.R; });

		double LargestSurfaceArea = 0.0;
		for (size_t p = 0, size = Pancakes.size() - K; p <= size; ++p)
		{
			vector<Pancake> SmallerPancakes(Pancakes.begin() + p + 1, Pancakes.end());
			sort(SmallerPancakes.begin(), SmallerPancakes.end(), [](const Pancake& LHS, const Pancake& RHS) { return SideSurfaceArea(LHS) > SideSurfaceArea(RHS); });

			double SurfaceArea = Pancakes[p].R * Pancakes[p].R * pi + SideSurfaceArea(Pancakes[p]);
			for (size_t s = 0; s < K - 1; ++s)
				SurfaceArea += SideSurfaceArea(SmallerPancakes[s]);

			if (SurfaceArea > LargestSurfaceArea)
				LargestSurfaceArea = SurfaceArea;
		}
		cout << fixed << setprecision(9) << "Case #" << t + 1 << ": " << LargestSurfaceArea << endl;
	}
}
