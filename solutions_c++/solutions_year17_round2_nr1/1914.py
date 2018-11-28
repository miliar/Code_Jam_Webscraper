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
using namespace std;

//#define SMALL
#define LARGE

int main()
{


	#ifdef SMALL
		freopen("A-small-attempt1.in","rt",stdin);
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
		double d;
		int n, ans = 0;
		cin >> d >> n;
		
		double k[n], s[n], time[n], max = -1;
		
		for(int i = 0; i < n; i++)
		{
			cin >> k[i] >> s[i];
			time[i] = (d - k[i]) / s[i];
			if(time[i] > max)
			{
				max = time[i];
			}
		}
				
		cout << fixed << "Case #" << t << ": " << d / max << endl;	
	}
	
	return 0;
}
