#include <iostream>
#include <algorithm>
#include <iomanip>
#include <string>
#include <vector>
#define _USE_MATH_DEFINES
#include <math.h>

using namespace std;

class pancake
{
public:
	pancake(double r, double h)
	{
		R = r;
		H = h;
		Top = M_PI * r * r;
		Side = 2 * M_PI * r * h;
	}
	double R;
	double H;
	double Top;
	double Side;

	static bool sorterTop(pancake A, pancake B)
	{
		return (A.R > B.R);
	}

	static bool sorterSide(pancake A, pancake B)
	{
		return (A.Side > B.Side);
	}
};

int main()
{
	cout << fixed;
	cout << setprecision(9);

	int T, t;
	cin >> T;

	for (t = 1; t <= T; t++)
	{
		int N, K;
		double r, h;
		vector<pancake> cakes;
		
		cin >> N >> K;

		for (int i = 0; i < N;i++)
		{
			cin >> r >> h;
			cakes.push_back(pancake(r, h));
		}

		sort(cakes.begin(), cakes.end(), pancake::sorterTop);

		double answer = 0;

		for (int i = 0; i < N + 1 - K; i++)
		{
			double cur = cakes[i].Top + cakes[i].Side;

			vector<pancake> curCakes(cakes.begin() + i + 1, cakes.end());
			sort(curCakes.begin(), curCakes.end(), pancake::sorterSide);

			for (int j = 0; j < K - 1; j++)
			{
				cur += curCakes[j].Side;
			}

			if (cur > answer)
			{
				answer = cur;
			}
		}

		cout << "Case #" << t << ": " << answer << endl;
	}

	return 0;
}