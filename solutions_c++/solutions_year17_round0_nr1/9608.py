#include<bits/stdc++.h>
using namespace std;

long long int k; string s;
string flip(long long int index)
{
	long long int i;
	for(i=index;i<=index+k-1;i++)
	{
		if(s[i]=='-')
			s[i]='+';
		else if(s[i]=='+')
			s[i]='-';
	}
	return s;
}
int main()
{
	long long int t,i,test,l,cnt=0,plus,minus; bool flag;
	cin>>t;
	test=t;
	while(t--)
	{
		cnt=0;	
		flag=true;
		plus=0;
		minus=0;
		cin>>s>>k;
		l=s.length();
		for(i=0;i<l;i++)
		{
			if(s[i]=='+')
				plus++;
			else 
				minus++;
		}
		if(k==1)
			cout<<minus<<endl;
		else
		{
			for(i=0;i<l;i++)
			{
				if(s[i]=='-')
				{
					if(i+k-1<l)
					{
						flip(i);
						//cout<<s<<endl;
						cnt++;
					}
					else 
					flag=false;
				}
			}
			if(flag==true)
				cout<<"Case #"<<(test-t)<<": "<<cnt<<endl;
			else
				cout<<"Case #"<<(test-t)<<": IMPOSSIBLE"<<endl;
		}

	}
	return 0;
}