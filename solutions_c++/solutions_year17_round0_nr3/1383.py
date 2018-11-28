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
		freopen("C-small-2-attempt0.in", "rt", stdin);
		freopen("C-small-2.out", "wt", stdout);
	#endif

	#ifdef LARGE
		freopen("C-large.in", "rt", stdin);
		freopen("C-large.out", "wt", stdout);
	#endif

	long long int t;
	cin >> t;
	
	for(long long int i = 1; i <= t; i++)
	{
		long long int ans = 0, n, k;
		cin >> n >> k;
		
		long long int k1 = 1, k2 = 1, part, rem, curr_part;
		while(k2 < k)
		{
			k2 = (k2 << 1) + 1;
		}
		k1 = k2 >> 1;
		
		part = (n - k1) / (k1 + 1);
		rem = (n - k1) % (k1 + 1);
		
		curr_part = part;
		if(k - k1 <= rem && rem != 0)
			curr_part = part + 1;
			
		ans = curr_part / 2;
		if(curr_part % 2 == 1)
			cout << "Case #" << i << ": " << ans << " " << ans << endl;
		else
			if(ans == 0)
				cout << "Case #" << i << ": " << ans << " " << ans << endl;
			else
				cout << "Case #" << i << ": " << ans << " " << ans - 1 << endl;
	}
	
	return 0;
}
