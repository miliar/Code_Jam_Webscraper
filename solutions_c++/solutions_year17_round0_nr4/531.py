#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
#include <map>

using namespace std;

int N;
char row[200];

struct rep
{
	char c;
	int x;
	int y;
	rep(char c, int x, int y) : c(c), x(x), y(y) {}
};

void solve()
{
	int bad = 0;
	vector<rep> r;
	for (int x=0; x<N; ++x)
		if (row[x] != '.' && row[x] != '+')
			bad=x;
	if (row[bad] != 'o')
	{
		row[bad] = 'o';
		r.push_back(rep('o', bad, 0));
	}
	for (int x=0; x<N; ++x)
		if (row[x] == '.')
		{
			row[x] = '+';
			r.push_back(rep('+', x, 0));
		}
	for (int x=0; x<N-1; ++x)
	{
		r.push_back(rep('x', x >= bad ? x+1 : x, x+1));
	}
	if (N > 2 && bad == N-1)
		r[r.size()-1].c = 'o';
	for (int x=1; x<N-1; ++x)
		r.push_back(rep('+', x, N-1));
	if (N > 2 && bad == N-1)
		r.pop_back();
	printf("%d %d\n", N==1 ? 2 : 2*N+N-2, r.size());
	for(int i=0; i<r.size(); ++i)
		printf("%c %d %d\n", r[i].c, r[i].y+1, r[i].x+1);
}

int main()
{
	int T;
	scanf("%d\n", &T);
	for (int t=0; t<T; ++t)
	{
		int M;
		scanf("%d %d\n", &N, &M);
		for(int i=0; i<N; ++i)
			row[i] = '.';
		for(int i=0; i<M; ++i)
		{
			char c;
			int x, y;
			scanf("%c%d%d\n", &c, &y, &x);
			row[x-1] = c;
		}
		printf("Case #%d: ", t+1);
		solve();
	}
	return 0;
}
