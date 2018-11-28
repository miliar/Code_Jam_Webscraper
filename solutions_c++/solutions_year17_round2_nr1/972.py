#include <bits/stdc++.h>

using namespace std;

int main()
{
	//freopen("testA1.inp","r",stdin);
	//freopen("testA1.out","w",stdout);
	int T;
	cin >> T;
	int test=0;
	while (T--)
	{
		test++;
		double S,d,v,ti=0;
		int n;
		cin >> S >> n;
		for (int i=1; i<=n; ++i)
		{
			cin >> d >> v;
			ti=max(ti,(S-d)/v);
		}
		printf("Case #%d: %.6f\n",test,S/ti);
	}
}
