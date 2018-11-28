#include<iostream>
using namespace std;

int main()
{
	int cases;
	cin>>cases;
	for(int z=1; z<=cases; z++)
	{
		cout<<"Case #"<<z<<": ";
		string s;
		cin>>s;
		int k;
		cin>>k;
		int ans=0;
		for(int i=0; i<s.length()+1-k; i++)
		{
			if(s[i]=='-')
			{
				for(int j=i; j<i+k; j++)
				{
					if(s[j]=='-') s[j]='+';
					else s[j]='-';
				}
				ans++;
			}
		}
		bool check=1;
		for(int i=0; i<s.length(); i++)
		{
			if(s[i]=='-')
			{
				check=0;
				break;
			}
		}
		if(check) cout<<ans<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
}