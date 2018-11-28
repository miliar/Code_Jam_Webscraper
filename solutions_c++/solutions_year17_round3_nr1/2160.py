#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio> 
#include <iostream> 
#include <cmath> 
#include <string> 
#include <list> 
#include <vector> 
#include <algorithm> 
#include <functional> 
#include <utility> 
#include <set> 
#include <map> 
#include <complex> 
#include <queue> 
#include <stack> 
#include <cstdlib> 
#include <ctime> 
#include <cstring> 
#include <string.h> 

using namespace std;
typedef long long ll;
#define OO 2000;
#define md 1000000007
# define M_PI           3.14159265358979323846
using namespace std;
bool mySort( pair<double, int> &a,  pair<double, int> &b)
{
	return a.first>b.first;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, n, k, r, h;

	vector<double> circle, cyl;
	vector<pair<double, int>> cylinder;
	int taken[1005];

	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		circle.clear();
		cylinder.clear();
		cyl.clear();
		memset(taken, 0, sizeof taken);

		cin >> n >> k;
		for (int i = 0; i<n; i++)
		{
			cin >> r >> h;
			circle.push_back(M_PI * r * r);
			cyl.push_back(2 * M_PI * r * h);

			cylinder.push_back(make_pair((2 * M_PI * r * h), i));
		}

		sort(cylinder.begin(), cylinder.end(), mySort);
		for (int i = 0; i<k; i++)
			taken[cylinder[i].second] = 1;

		int largestCircleIndx = -1;
		double largestCircle = -1.0;
		for (int i = 0; i<n; i++)
		{
			if (circle[i] > largestCircle)
			{
				largestCircle = circle[i];
				largestCircleIndx = i;
			}
		}

		int maxi_indx = -1, tmpLargestCircleIndx = -1;
		double maxi = -1, tmpLargestCircle = -1;
		if (taken[largestCircleIndx] == 0)
		{
			//get tmpLargestCircle
			for (int i = 0; i<n; i++)
			{
				if (taken[i] && circle[i]> tmpLargestCircle)
				{
					tmpLargestCircle = circle[i];
					tmpLargestCircleIndx = i;
				}
			}

			//get diff in circles i will make
			double diffCicle = largestCircle - tmpLargestCircle;

			//get minimum diffInCylinder
			double diffCylinder = DBL_MAX, tmpDiffCylinder = -1;
			int tmpDiffCylinderIndx = -1;
			for (int i = 0; i<n; i++)
			{
				if (i != largestCircleIndx)
				{
					tmpDiffCylinder = cyl[i] - cyl[largestCircleIndx];
					if (taken[i] && diffCylinder>tmpDiffCylinder)
					{
						diffCylinder = tmpDiffCylinder;
							tmpDiffCylinderIndx = i;
					}
				}
			}

			if (tmpDiffCylinderIndx != -1 && diffCicle > diffCylinder)
			{
				taken[tmpDiffCylinderIndx] = 0;
				taken[largestCircleIndx] = 1;
			}
			else
			{
				largestCircle = tmpLargestCircle;
			}
		}

		double ans = largestCircle;
		for (int i = 0; i<n; i++)
		{
			if (taken[i])
			{
				ans += cyl[i];
			}
		}

		cout.precision(17);
		cout << "Case #" << tt << ": " << ans << endl;
	}

	return 0;
}