
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
int main() {
	int t;
	cin >> t;
	for(int u = 0; u < t; u++)
	{
		int n, k;
		cin >> n >> k;
		bool stalls1[n+2];
		for(int i = 1; i <= n; i++)
			stalls1[i] = false;
		stalls1[0] = stalls1[n+1] = true;

		for(int g = 0; g < k; g++)
		{
			int gmax = 0;
			int igmax = 0;
			int lastdifmax = 0;
			for(int i = 1; i <= n; i++)
			{
				int j = i;
				int k = i;
				int toLeft = 0;
				int toRight = 0;
				while(stalls1[j] != true)
				{
					toLeft++;
					j++;
				}
				while(stalls1[k] != true)
				{
					toRight++;
					k--;
				}
				toLeft--;
				toRight--;
 
				int a = min(toLeft, toRight);
				if (a > gmax)
				{
					gmax = a;
					igmax = i;
					lastdifmax = max(toLeft, toRight);
				}
 
				if(a == gmax)
				{
					int b  = max(toLeft, toRight);
					if(b > lastdifmax)
					{
						lastdifmax = b;
						gmax = a;
						igmax = i;
					}
 
				}
			}
 
 
			if(g == k-1)
			{
				cout << "Case #" << u+1 << ": " << lastdifmax << " " << gmax << endl;
			}
 
			stalls1[igmax] = true;
		}
 
	}
	return 0;
}