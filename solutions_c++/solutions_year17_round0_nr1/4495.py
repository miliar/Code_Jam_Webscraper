#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("h3.txt","w",stdout);
	int t,t1;
	cin>>t;
	t1=t;
	while(t--)
	{
		
		char s[10000];
		int i,l,k=0,j,z,mm=0;
		cin>>s>>z;
		l=strlen(s);
		cout<<"Case #"<<t1-t<<": ";
		for(i=0;i<l-z+1;i++)
		{
			if(s[i]=='+')
			continue;
			else
			{
				
				k++;
				for(j=i;j<i+z;j++)
				{
					if(s[j]=='-')
					s[j]='+';
					else
					s[j]='-';
				}
				
			}
		}
		for(i=0;i<l;i++)
		if(s[i]=='-')
		{
			cout<<"IMPOSSIBLE\n";
			mm=1;
			break;
		}
		
		
		if(mm==0)
		cout<<k<<endl;
	}
	
}
