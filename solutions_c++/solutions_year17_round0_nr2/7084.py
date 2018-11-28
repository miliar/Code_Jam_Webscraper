#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,y=1;
	char str[25],k,x; //game is on
	cin>>t;
	while(t--)
	{
		k=0;
		x=0;
		int i,len;
		cin>>str;
		len=strlen(str);
		if(len==1)
		{cout<<"Case #"<<y++<<": ";
			cout<<str<<endl;
		}
		else
		{
		for(i=0;i<len-1;i++)
		{
			if(str[i+1]<str[i] && str[i]!='1' && (str[i]-str[i-1])==0)
			{
				str[0]-=1;
				for(i=1;i<len;i++)
				    	str[i]='9';
				}
			else if(str[i+1]<str[i] && str[i]!='1' && abs(str[i+1]-str[i])>0)
			{
				x=i+1;
				str[i]-=1;
				for(i=x;i<len;i++)
					str[i]='9';
			}
				
			else if(str[i+1]<str[i] && str[i]=='1')
			{
				k=1;
				for(i=0;i<len;i++)
					str[i]='9';
			}
		}
		if(k==0) //lets print it
		{
			    cout<<"Case #"<<y++<<": ";
				for(i=0;i<len;i++)
					cout<<str[i];
				cout<<endl;
			}
			else if(k==1)
			{
			    cout<<"Case #"<<y++<<": ";
				for(i=1;i<len;i++)
					cout<<str[i];
				cout<<endl;
			}
		}

	}
	return 0;
}
