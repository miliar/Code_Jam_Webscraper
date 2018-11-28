#include <cstdio>
#include <vector>

struct horse
{
    int pos, vel;
} ;

const double INF = 1e20;

int main()
{
    int tests;
    scanf("%d", &tests);

    for(int test = 1; test <= tests; test++)
    {
	int dest, n;
	scanf("%d %d", &dest, &n);

	std::vector<horse> horses;
	for(int i = 0; i < n; i++)
	{
	    horse h;
	    scanf("%d %d", &h.pos, &h.vel);
	    horses.push_back(h);
	}

	double res = INF;
	for(horse h : horses)
	{
	    double t = (double)(dest - h.pos) / (double)h.vel;
	    res = std::min(res, (double)dest / t);
	}

	printf("Case #%d: %.7f\n", test, res);
    }

    return 0;
}
