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

#define SMALL
//#define LARGE

int main()
{


	#ifdef SMALL
		freopen("B-small-attempt3.in","rt",stdin);
		freopen("B-small.out","wt",stdout);
	#endif

	#ifdef LARGE
		freopen("B-large.in","rt",stdin);
		freopen("B-large.out","wt",stdout);
	#endif

	int t, T;
	cin >> T;
	
	for(t = 1; t <= T; t++)
	{
		int  N, R, O, Y, G, B, V;
		cin >>  N >> R >> O >> Y >> G >> B >> V;
		
		char ans[N + 1];
		ans[N] = '\0';
		
		if(R > N / 2 || B > N / 2 || G > N / 2 || O > N / 2 || V > N / 2 || Y > N / 2)
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
		else
		{
			char prev = 'X';
			int i = 1, r = R, b = B, y = Y;
			
			if(R >= B && R >= Y)
			{
				ans[0] = 'R';
				prev = 'R';
				R--;
			}
			else if(B >= R && B >= Y)
			{
				ans[0] = 'B';
				prev = 'B';
				B--;
			}
			else if(Y >= R && Y >= B)
			{
				ans[0] = 'Y';
				prev = 'Y';
				Y--;
			}
			
			while(R > 0 || B > 0 || Y > 0)
			{
				if(prev == 'R')
				{
					if(B > Y)
					{
						ans[i] = 'B';
						prev = 'B';
						B--;	
					}
					else if(Y > B)
					{
						ans[i] = 'Y';
						prev = 'Y';
						Y--;
					}
					else
					{
						if(b >= y)
						{
							ans[i] = 'B';
							prev = 'B';
							B--;	
						}
						else
						{
							ans[i] = 'Y';
							prev = 'Y';
							Y--;
						}
					}
				}
				else if(prev == 'B')
				{
					if(R > Y)
					{
						ans[i] = 'R';
						prev = 'R';
						R--;
					}
					else if(Y > R)
					{
						ans[i] = 'Y';
						prev = 'Y';
						Y--;
					}
					else
					{
						if(r >= y)
						{
							ans[i] = 'R';
							prev = 'R';
							R--;
						}
						else
						{
							ans[i] = 'Y';
							prev = 'Y';
							Y--;
						}
					}
				}
				else if(prev == 'Y')
				{
					if(R > B)
					{
						ans[i] = 'R';
						prev = 'R';
						R--;
					}
					else if(B > R)
					{
						ans[i] = 'B';
						prev = 'B';
						B--;
					}
					else
					{
						if(r >= b)
						{
							ans[i] = 'R';
							prev = 'R';
							R--;
						}
						else
						{
							ans[i] = 'B';
							prev = 'B';
							B--;
						}
					}
				}
				i++;
			}
			cout << "Case #" << t << ": " << ans << endl;
		}
		
	}
	
	return 0;
}
