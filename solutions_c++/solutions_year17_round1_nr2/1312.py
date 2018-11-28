#include <stdio.h>
#include <math.h>
#include <vector>
#include <queue>
using namespace std;

typedef struct Set {
	int min, max;
}Set;

typedef struct cmp {
	bool operator()(Set a, Set b) {
		return ((a.min > b.min) || (a.min == b.min && a.max > b.max));
	}
}cmp;

vector<priority_queue<Set, vector<Set>, cmp>> vec;
int n, p, stop;

int find2(int min2, int max2, int index)
{
	int left, right;
	priority_queue<Set, vector<Set>, cmp> pq;
	if (index == n - 1)
	{
		pq = vec.at(index);
		while (!pq.empty() && pq.top().max < min2)
			pq.pop();
		if (pq.empty())
		{
			stop = 1;
			return 0;
		}
		else
			stop = 0;
		if (pq.top().min <= max2)
		{
			pq.pop();
			return 1;
		}
		else
			return 0;
	}
	
	pq = vec.at(index);
	while (!pq.empty() && pq.top().max < min2)
		pq.pop();
	if (pq.empty())
	{
		stop = 1;
		return 0;
	}
	else
		stop = 0;
	if (pq.top().min <= max2 && pq.top().max>=min2)
	{
		left = (pq.top().min > min2) ? pq.top().min : min2;
		right = (pq.top().max < max2) ? pq.top().max : max2;
		if (find2(left,right, index + 1) == 1)
		{
			pq.pop();
			return 1;
		}
		else
			return 0;
	}
	else
		return 0;
}

int main()
{
	FILE *in, *out;
	int test, tt, i, j, ans, cost[50], tmp,mini,maxi;
	double d;

	in = fopen("B-small-attempt1.in", "r");
	out = fopen("outputBS.txt", "w");

	fscanf(in, "%d", &test);
	for (tt = 1;tt <= test;tt++)
	{
		ans = 0;
		vec.clear();
		fscanf(in, "%d %d", &n, &p);
		for (i = 0;i < n;i++)
			fscanf(in, "%d", &cost[i]);
		for (i = 0;i < n;i++)
		{
			priority_queue<Set, vector<Set>, cmp> pq;
			for (j = 0;j < p;j++)
			{
				Set s;
				fscanf(in, "%d", &tmp);
				d = (double)tmp / (1.1*(double)cost[i]);
				mini = ceil(d);
				maxi = (double)tmp / (0.9*(double)cost[i]);
				s.max = maxi;
				s.min = mini;
				if (s.max >= s.min)
					pq.push(s);
			}
			vec.push_back(pq);
		}
		
		if (n == 1)
		{
			ans = vec.at(0).size();
		}
		else
		{
			while (!vec.at(0).empty())
			{
				if (find2(vec.at(0).top().min, vec.at(0).top().max, 1) == 1)
					ans++;
				if (stop == 1)
					break;
				vec.at(0).pop();
			}
		}

		fprintf(out, "Case #%d: %d\n", tt, ans);
	}

	fclose(in);
	fclose(out);
	return 0;
}