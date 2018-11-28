#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Interval
{
	int minval;
	int maxval;
	bool operator<(const Interval &other) const
	{
		if (maxval < other.maxval)
			return true;
		if (maxval > other.maxval)
			return false;
		return minval < other.minval;
	}
};

bool intersect(Interval &a, Interval &b, Interval &c)
{
	if (a.maxval < b.minval || b.maxval < a.minval)
		return false;
	int newmin = max(a.minval, b.minval);
	int newmax = min(a.maxval, b.maxval);
	c.minval = newmin;
	c.maxval = newmax;
	return true;
}

void doCase()
{
	int N,P;
	cin >> N;
	cin >> P;
	int *needed = new int[N];
	int *packages = new int[N*P];

	for (int i = 0; i < N; i++)
		cin >> needed[i];
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < P; j++)
		{
			cin >> packages[i*P + j];
		}
	}

	vector<vector<Interval> > sorted;
	for (int i = 0; i < N; i++)
	{
		vector<Interval> ingredients;
		for (int j = 0; j < P; j++)
		{
			int amount = packages[i*P + j];
			Interval interval;
			interval.maxval = 10 * amount / (9 * needed[i]);
			int remainder = (10 * amount) % (11 * needed[i]) == 0 ? 0 : 1;
			interval.minval = remainder + (10 * amount) / (11 * needed[i]);
			if (interval.maxval < interval.minval)
			{
				interval.maxval = 0;
				interval.minval = 0;
			}
			//cout << "creating " << interval.minval << " " << interval.maxval << endl;
			ingredients.push_back(interval);
		}
		sort(ingredients.begin(), ingredients.end());
		sorted.push_back(ingredients);
	}

	int npackages = 0;
	vector<int> idx;
	for (int i = 0; i < N; i++)
		idx.push_back(P - 1);
	while (true)
	{
		bool done = false;
		for (int i = 0; i < N; i++)
		{
			if (idx[i] < 0)
				done = true;
		}
		if (done)
			break;

		Interval isect = sorted[0][idx[0]];
		bool ok = true;
		for (int i = 1; i < N; i++)
		{
			//cout << "intersecting " << isect.minval << " " << isect.maxval << " " << sorted[i][idx[i]].minval << " " << sorted[i][idx[i]].maxval << endl;
			ok &= intersect(isect, sorted[i][idx[i]], isect);
		}

		if (ok)
		{
			if(isect.maxval != 0)
				npackages++;
			for (int i = 0; i < N; i++)
			{
				idx[i]--;
			}
		}
		else
		{
			int minidx = -1;
			int minval = 0;
			for (int i = 0; i < N; i++)
			{
				if (sorted[i][idx[i]].minval > minval)
				{
					minval = sorted[i][idx[i]].minval;
					minidx = i;
				}
			}
			idx[minidx]--;
		}
	}

	delete[] packages;
	delete[] needed;
	cout << npackages << endl;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cout << "Case #" << i + 1 << ": ";
		doCase();
	}
}