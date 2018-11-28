#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,c=1;
	cin>>t;
	while(t--)
	{
		string n;
		string ans;
		cin>>n;
		bool less = 0;
		for(int i=0;i<n.size();i++){ if(n[i]=='0') less=1; if(n[i]!='1') break; }
		if(less)
		{
			ans = "";
			for(int i=1;i<n.size();i++) ans+='9';

		}
		else
		{
			bool found=0;
			for(int i=1;i<n.size();i++)
			{
				if(found) 
				{
					n[i]='9';
					continue;
				}
				if(n[i]<n[i-1])
				{
					for(int j=i;;j--)
					{
						if(n[j]<n[j-1]) n[j-1]--;
						else { i=j; break; }
					}
					found=1;
				}
			}
			ans=n;
		}
		cout<<"Case #"<<c++<<": "<<ans<<endl;
	}
	return 0;
}

