#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <iomanip>

const int NMAX = 1005;

using namespace std;

ifstream f("syrup.in");
ofstream g("syrup.out");

struct pancake
{
	double r;
	double h;

	bool operator < (const pancake &t) const
    {
        if (t.r < r)
            return true;
        return false;
    }
};

int T;
int N, K;
vector <pancake> v;
double dp[NMAX][NMAX];
double answer;

void init()
{
	v.clear();
	pancake aux;
	aux.r = 100000000;
	aux.h = 100000000;
	v.push_back(aux);

	for (int i = 0; i < 1001; ++i)
	{
		for (int j = 0; j < 1001; ++j)
		{
			dp[i][j] = 0;
		}
	}
}

void read()
{
	f >> N >> K;
	for (int i = 1; i <= N; ++i)
	{
		pancake newPancake;
		f >> newPancake.r;
		f >> newPancake.h;
		v.push_back(newPancake);
	}
}

void solve(int t)
{
	sort(v.begin(), v.end());
	for (int i = 1; i <= N; ++i)
	{
		for (int j = 1; j <= K; ++j)
		{
			if (j > i)
			{
				continue;
			}

			dp[i][j] = v[i].r * v[i].r + 2 * v[i].r * v[i].h;

			if (j == 1)
			{
				continue;
			}

			for (int p = j - 1; p < i; ++p)
			{
				dp[i][j] = max(dp[i][j], dp[p][j - 1] + 2 * v[i].r * v[i].h);
			}
		}
	}

	answer = 0;
	for (int i = 1; i <= N; ++i)
	{
		if (dp[i][K] > answer)
		{
			answer = dp[i][K];
		}
	}
	g << "Case #" << t << ": ";
	// Case #1: 
	g << answer * M_PI << '\n';
}

int main()
{
	f >> T;
	g << setprecision(9) << fixed;
	for(int t = 1; t <= T; ++t)
	{
		init();
		read();
		solve(t);
	}
}