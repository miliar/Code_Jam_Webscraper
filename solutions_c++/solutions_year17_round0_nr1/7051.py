#include <bits/stdc++.h>
using namespace std;

int T, t, k, i, SZ;
string pan;

inline void flip()
{
	int j;
	for(j = i; j < i+k; j++)
	{
		if(pan[j] == '-')
			pan[j] = '+';
		else
			pan[j] = '-';
	}
}

int main()
{
	//freopen("A.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	
	cin>>T;
	
	for(t = 1; t <= T; t++)
	{
		cin>>pan>>k;
		cout<<"Case #"<<t<<": ";
		
		bool imp = false;
		int ans = 0;
		SZ = pan.size();
		
		
		for(i = 0; i < SZ; i++)
		{
			if(pan[i] == '-')
			{
				if(i + k <= SZ)
				{
					flip();
					ans++;
				}
				else
				{
					imp = true;
				}
			}
		}
		
		if(imp)
			cout<<"IMPOSSIBLE"<<endl;
		else
		{
			cout<<ans<<endl;
		}
	}
	
	return 0;
}
