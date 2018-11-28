#include<bits/stdc++.h>
using namespace std;
int main()
{
	
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	cin>>n;
	for(int k=1;k<=n;k++)
	{
		string s;
		int i,j,p,x,cnt=0,f=0;
		cin>>s>>p;
		int l=s.length();
		for(i=0;i<=l-p;i++)	
		{
			
			if(s[i]=='-')
			{
				for(x=i;x<i+p;x++)
					if(s[x]=='-')
						s[x]='+';
					else
						s[x]='-';
				cnt++;
			}
		}
		while(i<l)
		{
			if(s[i]=='-')
			{
				f=1;
				break;			
			}
			i++;		
		}
		if(f==0)
			
			cout<<"Case #"<<k<<": "<<cnt<<endl;
		else
			cout<<"Case #"<<k<<": "<<"IMPOSSIBLE"<<endl;
	}
return 0;
}
