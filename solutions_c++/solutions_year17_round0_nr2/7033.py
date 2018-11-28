#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T, t, i, SZ;
	string n;
	char bigger;
	
	cin>>T;
	
	for(t = 1; t <= T; t++)
	{
		cin>>n;
		//cout<<"n = "<<n<<endl;
		cout<<"Case #"<<t<<": ";
		
		SZ = n.size() - 1;
		
		for(i = 0; i < SZ; i++)
		{
			
			if(n[i] > n[i+1] && n[i] > bigger)
			{
				while(i > 0 && n[i] == n[i-1])
					i--;
				
				n[i++]--;
				for(; i <= SZ; i++)
					n[i] = '9';
			}
		}
		
		i = 0;
		if(n[i] == '0')
			i++;
		
		for(; i <= SZ; i++)
			cout<<n[i];
		
		cout<<endl;
	}
	
	return 0;
}
