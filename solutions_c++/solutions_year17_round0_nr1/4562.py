#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,cnt=1;
	cin>>t;
	while(t--)
	{
		int n,i,j,k;
		string str; 
		cin>>str>>k;
		n = str.length();
		int ans = 0;
		for(i=0 ; i<n-k+1 ; i++)
		{
			if(str[i]=='-')
			{
				for(j=i ; j<i+k ; j++)
				{
					if(str[j]=='-') 
						str[j]='+';
					else 
						str[j]='-';
				}
				ans++;
			}
		}
		int yes = 1;
		for(i=0 ; i<n ; i++)
		{
			if(str[i]=='-')
			{
				yes = 0; break;
			}
		}
		cout<<"Case #"<<cnt<<": ";
		if(!yes) 
			cout<<"IMPOSSIBLE\n";
		else 
			cout<<ans<<"\n";
		cnt++;
	}
	return 0;
} 