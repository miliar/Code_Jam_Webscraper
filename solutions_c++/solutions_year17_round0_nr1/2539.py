#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int c=1;c<=t;c++)
	{
		int ans=0,k;
		string x;
		cin>>x>>k;
		queue<int>things;
		for(int i=0;i<x.size();i++)
		{
			if(!things.empty() && things.front() < i ) things.pop();
			
			if((x[i]=='-')^(things.size()%2))
			{
				ans++; 
				things.push(i+k-1);
				if(i+k-1 >= x.size() ) 
				{
					ans=-1;
					break;
				}
			}
		}

		cout<<"Case #"<<c<<": ";
		if(ans==-1) cout<<"IMPOSSIBLE\n";
		else cout<<ans<<endl;
	}
	return 0;
}
