#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <typeinfo>
#include <functional>
#include <iomanip>
using namespace std;

int main()
{
	double T,D,N;
	double maxtime = -1;

	cin >> T;
	for (int i = 0; i < T; i++)
	{
		maxtime = -1;
		cin >> D >> N;
		for (int j = 0; j < N; j++)
		{
			double K, S;
			cin >> S >> K;
			double time = (double)(D - S) / (double)(K);
			if (maxtime < time)
			{
				maxtime = time;
			}
		}
		double ret = D / maxtime;
		cout << "Case #" << i + 1 << ": ";
		printf("%.6lf\n", ret);
	}
	return 0;
}