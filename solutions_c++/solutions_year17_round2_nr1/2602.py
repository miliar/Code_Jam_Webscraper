#include <iostream>
using namespace std;

double D;
int N;
#define INIT	0
#define MS		1

double MAX(double a, double b)
{
	if (a > b) return a;
	return b;
}
void process(int tc)
{
	int ary[1001][2] = { 0 };
	double maxElapse = 0;
	
	cin >> D >> N;
	for (int i = 0; i < N; i++) cin >> ary[i][INIT] >> ary[i][MS];
	
	for (int i = 0; i < N; i++)
	{
		maxElapse = MAX(maxElapse, (double)(D - ary[i][INIT]) / ary[i][MS]);
	}
	cout << fixed;
	cout.precision(6);
	double ans = 0;

	if (maxElapse <= 0) ans = 0;
	else ans = D / maxElapse;
	cout << "Case #" << tc << ": " << ans  << endl;
}

int main()
{
	int C;
	cin >> C;

	for (int i = 0; i < C; i++) process(i + 1);
	return 0;
}