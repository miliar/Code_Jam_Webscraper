#include <bits/stdc++.h>
using namespace std;

int main()
{

	int t,n,cnt,i,j,cases,flag;

	cin>>t;
	string s;
	cases=1;

	while(t--)
	{	
		cnt=0;
		cin>>s>>n;
		cout<<"Case #"<<cases<<": ";
		
		
		cases+=1;

		for(i=0;s[i]!='\0';i+=1)
		{
			if(s[i]=='+')
			{}
			else
			{
				cnt+=1;
				if(i+n<=s.length())
				{
					for(j=i;j<i+n;j+=1)
					{
						if(s[j]=='+')
							s[j]='-';
						else
							s[j]='+';
					}
				}
			}
		}
		
		flag=0;
		for(i=0;s[i]!='\0';i+=1)
		{
			if(s[i]=='-')
				{flag=1;break;}
		}
		if(flag==1)
			cout<<"IMPOSSIBLE";
		else
			cout<<cnt;
		cout<<endl;


	}


	return 0;
}