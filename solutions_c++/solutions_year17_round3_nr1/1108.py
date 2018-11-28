#include <stdio.h>
#include <queue>
#define pi 3.1415926535897932384626433832795
using namespace std;

typedef struct Set {
	long long int r, w, index;
	long long int circle, side;
}Set;

typedef struct cmp {
	bool operator()(Set a, Set b) {
		return (a.r < b.r) || (a.r == b.r && a.w < b.w);
	}
}cmp;

int main()
{
	FILE *in, *out;
	long long int test, tt, n, k, i, j, check[1000];
	long long int ans, totalside, tmp, sidesave[1000][2], a;
	priority_queue<Set, vector<Set>, cmp> pq;

	in = fopen("A-large.in", "r");
	out = fopen("outputAL.txt", "w");

	fscanf(in, "%lld", &test);
	for (tt = 1;tt <= test;tt++)
	{
		fscanf(in, "%lld %lld", &n, &k);
		totalside = ans = 0.0;
		for (i = 0;i < n;i++)
			check[i] = 0;
		for (i = 0;i < n;i++)
		{
			Set s;
			fscanf(in, "%lld %lld", &s.r, &s.w);
			s.circle = (s.r*s.r);
			s.side = 2 * (s.r*s.w);
			s.index = i;
			sidesave[i][0] = i;
			sidesave[i][1] = s.side;
			totalside += s.side;
			pq.push(s);
		}

		for (i = 0;i < n - 1;i++)
		{
			a = i;
			for (j = i + 1;j < n;j++)
				if (sidesave[j][1] > sidesave[a][1])
					a = j;
			tmp = sidesave[i][0];
			sidesave[i][0] = sidesave[a][0];
			sidesave[a][0] = tmp;
			tmp = sidesave[i][1];
			sidesave[i][1] = sidesave[a][1];
			sidesave[a][1] = tmp;
		}
		ans = 0;
		while (!pq.empty())
		{
			check[pq.top().index] = 1;
			for (tmp = 0, i = 0, j = k - 1;i < n && j>0;i++, j--)
			{
				if (check[(int)sidesave[i][0]] == 0)
					tmp += sidesave[i][1];
				else
					j++;
			}
			a = tmp + pq.top().circle + pq.top().side;
			if (a > ans)
				ans = a;
			pq.pop();
		}
		fprintf(out, "Case #%lld: %.9lf\n", tt, (double)ans*pi);
	}

	fclose(in);
	fclose(out);
	return 0;
}