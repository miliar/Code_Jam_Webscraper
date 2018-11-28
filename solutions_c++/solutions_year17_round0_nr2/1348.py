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
		freopen("B-small-attempt0.in", "rt", stdin);
		freopen("B-small.out", "wt", stdout);
	#endif

	#ifdef LARGE
		freopen("B-large.in", "rt", stdin);
		freopen("B-large.out", "wt", stdout);
	#endif

	int t;
	cin >> t;
	
	for(int i = 1; i <= t; i++)
	{
		long long int ans = 0, n;
		cin >> n;
		
		for(long long int j = n; j > 0; j--)
		{
				long long int temp = j, sub = 0, place = 10;
				bool flag = true;
				while(temp > 0)
				{
					if((temp % 10) < ((temp % 100) / 10))
					{
						flag = false;
						sub = j % place;
					}
					temp = temp / 10;
					place *= 10;
				}
				if(flag == true)
				{
					ans = j;
					break;
				}
				else
				{
					j = j - sub;
				}
		}	
		
		cout << "Case #" << i << ": " << ans << endl;		
	}
	
	return 0;
}
