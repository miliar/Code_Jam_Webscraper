#include <iostream>
#include <fstream>
#include <algorithm>
#include <climits>
#include <vector>

using namespace std;

vector<long long> findMaxMin(long long* left, long long* right, long long n, bool* free)
{
	long long maxmin = -1;
	for (long long i = 0; i < n; i++)
	{
		if (free[i]) maxmin = max(maxmin, min(left[i], right[i]));
	}
	vector<long long> res;
	for (long long i = 0; i < n; i++)
	{
		if (free[i])
		{
			long long mn = min(left[i], right[i]);
			if (mn == maxmin) res.push_back(i);
		}
	}
	return res;
}

long long findMaxMax(long long* left, long long* right, vector<long long>& maxmin)
{
	long long pos = -1;
	long long maxmax = -1;
	for (const long long index : maxmin)
	{
		long long mx = max(left[index], right[index]);
		if (mx > maxmax)
		{
			maxmax = mx;
			pos = index;
		}
	}
	return pos;
}

int main(int argc, char** argv)
{
	string inFile(argv[1]);
	string outFile(inFile + ".out");
	ifstream in(inFile);
	ofstream out(outFile);

	int ts; in >> ts;
	for (int t = 1; t <= ts; ++t)
	{
		long long n, k; in >> n >> k;
		bool free[n];
		fill_n(free, n, true);
		long long left[n];
		fill_n(left, n, LLONG_MAX);
		long long right[n];
		fill_n(right, n, LLONG_MAX);
		long long resa = -1;
		long long resb = -1;
		while (k > 0)
		{
			long long l = 0;
			long long r = 0;
			for (long long i = 0; i < n; i++)
			{
				if (free[i])
				{
					left[i] = l;
					l++;
				}
				else
				{
					l = 0;
				}
				if (free[n - i - 1])
				{
					right[n - i - 1] = r;
					r++;
				}
				else
				{
					r = 0;
				}
			}
			long long pos = -1;
			vector<long long> maxmin = findMaxMin(left, right, n, free);
			if (maxmin.size() == 1) pos = maxmin.front();
			else pos = findMaxMax(left, right, maxmin);
			if (pos >= 0)
			{
				resa = max(left[pos], right[pos]);
				resb = min(left[pos], right[pos]);
				free[pos] = false;
			}
			k--;
		}
		out << "Case #" << t << ": " << resa << ' ' << resb << endl;
	}
	return 0;
}
