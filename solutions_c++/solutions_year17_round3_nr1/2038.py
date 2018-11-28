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
#define _USE_MATH_DEFINES
#include <math.h>
using namespace std;

int R[1000], H[1000];

int T, K, N;

double ret;

void dp(int n, double maxR, double score,int next)
{
	if (n == K)
	{
		score += maxR * maxR * M_PI;
		if (score > ret)
		{
			ret = score;
		}
		return;
	}

	for (int i = next; i < N; i++)
	{
		double tmp = 2.0f * M_PI * R[i] * H[i];
		double inR = maxR;
		if (R[i] > maxR)
		{
			inR = R[i];
		}
		dp(n + 1, inR, score + tmp, i + 1);

	}

	return;
}


priority_queue<double> retheight;

int main()
{
	double maxtime = -1;

	cin >> T;
	double maxR = 0, maxH = 0;
	for (int i = 0; i < T; i++)
	{

		ret = 0;
		cin >> N >> K;

		for (int j = 0; j < N; j++)
		{
			cin >> R[j] >> H[j];
		}

		dp(0, 0, 0,0);

		cout << "Case #" << i + 1 << ": ";
		printf("%.6f\n",ret);
	}
	return 0;
}