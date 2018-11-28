#include<iostream>
#include<string>
#include<cstdio>
#include<limits>
#include<cmath>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<iomanip>
using namespace std;

//#define SMALL
#define LARGE



int main()
{


	#ifdef SMALL
		freopen("A-small-attempt2.in","rt",stdin);
		freopen("A-small.out","wt",stdout);
	#endif

	#ifdef LARGE
		freopen("A-large.in","rt",stdin);
		freopen("A-large.out","wt",stdout);
	#endif

	int t, T;
	cin >> T;
	
	for(t = 1; t <= T; t++)
	{
		int n, k;
		double ans = 0;
		cin >> n >> k;	
		
		double r[n], h[n], a[n];
		
		for(int i = 0; i < n; i++)
		{
			cin >> r[i] >> h[i];
			a[i] = 2 * M_PI * r[i] * h[i] + M_PI * r[i] * r[i];
		}
		
		for(int i = 1; i < n; i++)
		{
			for (int j = 0; j < n - i; j++)
			{
				if(a[j] < a[j + 1])
				{
					swap(r[j], r[j + 1]);
					swap(h[j], h[j + 1]);
					swap(a[j], a[j + 1]);
				}
			}
		}
		
		for(int i = 1; i < n; i++)
		{
			a[i] = 2 * M_PI * r[i] * h[i];
		}
		
		for(int i = 1; i < n; i++)
		{
			for (int j = 0; j < n - i; j++)
			{
				if(a[j] < a[j + 1])
				{
					swap(r[j], r[j + 1]);
					swap(h[j], h[j + 1]);
					swap(a[j], a[j + 1]);
				}
			}
		}
		
		double R = 0;
		for(int i = 0; i < k; i++)
		{
			ans += 2 * M_PI * r[i] * h[i];
			if(R < r[i])
				R = r[i];
		}
		
		ans += M_PI * R * R;	
		
		cout << "Case #" << t << ": " << fixed << setprecision(10) << ans << endl;	
	}
	
	fclose(stdin);
	fclose(stdout);
	return 0;
}
