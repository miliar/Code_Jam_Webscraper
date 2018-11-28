#include <bits/stdc++.h>

using namespace std;
#define MAX 1010
const double eps = 0.00000001;

int d,n,t;
int v[MAX][2];
double tempo;


int main(void)
{
	ios :: sync_with_stdio(false);
	cin >> t;
	for (int cases = 1; cases <= t; ++cases)
	{
		cin >> d >> n;
		for (int i = 0; i < n; ++i)
		{
			cin >> v[i][0] >> v[i][1];
		}
		tempo = ((double)d - (double)v[n - 1][0])/(double)v[n - 1][1];
		for (int i = n - 2; i >= 0; --i)
		{
			double newtempo = ((double)d - v[i][0])/(double)v[i][1];
			tempo = max(tempo, newtempo);
		}
		cout << fixed << setprecision(8);
		cout << "Case #" << cases << ": " << (double)d/tempo << "\n";
	}
	return 0;
}
