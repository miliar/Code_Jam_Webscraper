#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	
	for(int c=1; c<=t; c++)
	{
		int n, r=0;
		cin>>n;
		
		for(int i=1; i<=n; i++)
		{
			int x=i;
			int at=x%10;
			bool ok=false;
			while(x>0)
			{
				int p=x%10;
				if(p>at)	ok=true;
				at=p;
				x/=10;
			}
			if(!ok)	r=max(r, i);
		}
		
		cout<<"Case #"<<c<<": "<<r<<endl;
	}
	
	return 0;
}