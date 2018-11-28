#include <iostream>
#include <algorithm>
#include <iomanip>

#define MAXN 1024
using namespace std;

int N, D;
double max_time = 0;

inline double calc_time(double X, double U)
{
	double rval = X / U;

	return rval;
}

inline void init()
{
	int i;

	double speed, pos;

	cin >> D >> N;
	max_time = 0;
	for (i = 0; i < N; i++)
	{
		cin >> pos >> speed;
		max_time = max(max_time, calc_time(D - pos, speed));
	}
}

inline double solve()
{
	return D / max_time;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios::sync_with_stdio(0);

	int i, T;
	cin >> T;

	for (i = 1; i <= T; i++)
	{
		init();
		cout << "Case #" << i << ": " << setprecision(15) << solve() << "\n";
	}

	return 0;
}