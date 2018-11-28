#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;

struct pc
{
	double r;
	double h;
	double g;
	double rg;

	double total;

	bool operator () (pc p, pc q)
	{
		if (p.g > q.g) return true;
		else return false;
	}
	
};

int N, K;
pc ary[1001];

#define PI 3.141592653589793238
double MAX(double a, double b)
{
	if (a > b) return a;
	return b;
}
void getMaxV(pc arr[], double& maxValue, int& maxIndex, int left, int right)
{
	for (int i = left; i < right; i++)
	{
		if (arr[i].total > maxValue)
		{
			maxValue = arr[i].total;
			maxIndex = i;
		}
	}
}
void process(int tc)
{
	cin >> N >> K;

	cout << fixed;
	cout.precision(9);

	for (int i = 0; i < N; i++) cin >> ary[i].r >> ary[i].h;
	for (int i = 0; i < N; i++)
	{
		ary[i].g = 2 * PI*ary[i].r * ary[i].h;
		ary[i].rg = PI * ary[i].r * ary[i].r;
		ary[i].total = ary[i].g + ary[i].rg;
	}
	
	sort(ary, ary + N,pc());

	double ans = 0.0;
	double bMRG = 0.0;
	for (int i = 0; i < K-1; i++)
	{
		ans += ary[i].g;
		if (bMRG < ary[i].rg) bMRG = ary[i].rg;
	}

	int lowestIndex = 0;
	double lowestTotalValue = 0;
	for (int i = K - 1; i < N; i++)
	{
		double tempTotal = MAX(0,ary[i].rg - bMRG) + ary[i].g;
		if (tempTotal > lowestTotalValue)
		{
			lowestTotalValue = tempTotal;
			lowestIndex = i;
		}
	}

	ans += ary[lowestIndex].g;
	if (bMRG > ary[lowestIndex].rg) ans += bMRG;
	else ans += ary[lowestIndex].rg;
	
	cout << "Case #" << tc << ": " << ans << endl;
}

int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) process( i+ 1);

	return 0;
}