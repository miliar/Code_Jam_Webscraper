#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t,k,i,j,ans,n,c=1;
	string s;
	cin>>t;
	while(t>0)
	{
		cout<<"Case #"<<c<<": ";
		++c;
		ans=0;
		cin>>s>>k;
		n=s.length();
		for(i=0;i<n-k+1;++i)
		{
			if(s[i]=='+')
			continue;
			else
			{
				++ans;
				for(j=i;j-i<k;++j)
				if(s[j]=='+')
				s[j]='-';
				else
				s[j]='+';
			}
		}
		
		int flag=0;
		for(i=0;i<n;++i)
		if(s[i]=='-')
		flag=1;
		if(flag==1)
		cout<<"IMPOSSIBLE"<<endl;
		else
		cout<<ans<<endl;
		--t;
	}
	return 0;
}

