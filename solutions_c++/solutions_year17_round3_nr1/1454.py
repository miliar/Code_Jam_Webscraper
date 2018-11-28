
#define _CRT_SECURE_NO_WARNINGS
#include<vector>
#include<iostream>
#include<algorithm>
#include<iomanip>
#include<string>

#define M_PI 3.14159265358979323846

using namespace std;

vector<pair<long long int, int> > precalc(vector<pair<long long int, long long int> > &v)
{
	vector<pair<long long int, int> > res(v.size(), make_pair(0, -1));
	for (int i = 0; i < res.size(); ++i)
	{
		res[i].second = i;
		res[i].first = 2 * v[i].first * v[i].second;
	}
	sort(res.begin(), res.end());
	reverse(res.begin(), res.end());
	return res;
}

long long int f(vector<pair<long long int, long long int> > &v, int start, vector<pair<long long int, int> > &opt, int goal)
{
	long long int width = v[start].first * v[start].first;
	long long int height = v[start].second * v[start].first * 2;

	int cur = 1;
	for (int i = 0; i < opt.size(); ++i)
	{
		if (cur == goal)
			break;
		if (opt[i].second == start)
			continue;		
		if (opt[i].second < start)
		{
			++cur;
			height += opt[i].first;
		}
	}

	if (cur == goal)
	{
		return width + height;
	}
	return -1;
}

int main()
{
	freopen("a.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for (int testNum = 0; testNum < test; ++testNum)
	{
		int n, k;
		cin >> n >> k;
		vector<pair<long long int, long long int> > arr(n, make_pair(0,0));
		for (int i = 0; i < n; ++i)
		{
			cin >> arr[i].first >> arr[i].second;
		}
		sort(arr.begin(), arr.end());

		vector<pair<long long int, int> > heights = precalc(arr);
		long long int max = -1;
		for (int i = 0; i < arr.size(); ++i)
		{
			long long int tmp = f(arr, i, heights, k);
			if (tmp > max)
				max = tmp;
		}

		cout << "Case #" << testNum + 1 << ": " << setprecision(7) << fixed << max * M_PI << endl;
	}
	return 0;
}