#include <iostream>
const double PI_F = 3.14159265358979f;

using namespace std;

void doWork()
{
	int N, K;
	cin >> N;
	cin >> K;

	double flatAreas[10000];
	double sideAreas[10000];
	double radii[10000];

	for (int n = 0; n < N; ++n)
	{
		int r, h;
		cin >> r;
		cin >> h;

		radii[n] = r;
		flatAreas[n] = PI_F * r * r;
		sideAreas[n] = 2 * PI_F * r * h;
	}

	double best = -1;

	for (int n = 0; n < N; ++n)
	{
		bool usedSides[10000] = { false };

		double flat = flatAreas[n];
		double side = sideAreas[n];

		usedSides[n] = true;
		bool bad = false;

		for (int k = 1; k < K; ++k)
		{
			double bestSide = -1;
			int bestSideIdx = -1;

			for (int w = 0; w < N; ++w)
			{
				if (!usedSides[w] && radii[w] <= radii[n])
				{
					if (sideAreas[w] > bestSide)
					{
						bestSide = sideAreas[w];
						bestSideIdx = w;
					}
				}
			}

			if (bestSideIdx >= 0)
			{
				usedSides[bestSideIdx] = true;
				side += bestSide;
			}
			else
			{
				bad = true;
			}
		}

		double total = flat + side;
		if (total > best)
		{
			best = total;
		}
	}

	cout << fixed << best << endl;
}

void main()
{
	int cases;
	cin >> cases;

	for (int k = 1; k <= cases; ++k)
	{
		cout << "Case #" << k << ": ";
		doWork();
	}
}