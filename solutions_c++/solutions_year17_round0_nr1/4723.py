#include <bits/stdc++.h>
using namespace std;

int n , t , can;
string z;

bool good()
{
	for(int i=0;i<n;i++) if(z[i] == '-') return false;
	return true;
}

void flip(int start , int end)
{
	for(int i=start;i < end && i < n;i++)
	{
		if(z[i] == '-') z[i] = '+';
		else z[i] = '-';
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> t;
	
	for(int q=1;q<=t;q++)
	{
		cin >> z >> can;
		
		n = z.size();
		
		int ans = 0;
		
		for(int i=0;i + can <= n;i++)
		{
			if(z[i] == '-')
			{
				flip(i,i+can);
				ans++;
			}
		}
		
		if(good()) printf("Case #%d: %d\n",q,ans);
		else printf("Case #%d: IMPOSSIBLE\n",q);
		
	}
}