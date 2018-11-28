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
		
		// True ocupada, False vazia
		bool stalls[n+2];
		for(int i = 1; i <= n; i++)
			stalls[i] = false;
		stalls[0] = stalls[n+1] = true;
		
		
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
				while(stalls[j] != true)
				{
					toLeft++;
					j++;
				}
				while(stalls[k] != true)
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
			
			stalls[igmax] = true;
		}
		
	}
	return 0;
}