#include<iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		string s;
		cin>>s;
		int k;
		cin>>k;
		
		int i,cnt=0,len=s.length(),tmp_i;
				
		for(i=0;s[i]!='\0';i++)
		{
			if(s[i]=='-')
			{
				tmp_i=i;
				if((i+k-1) > (len-1))
				{
					i-=(i+k-1) - (len-1);
				}
				for(int j=0;j<k;j++)
				{
					if(s[i+j]!='\0')
					{
						if(s[i+j]=='-')
							s[i+j]='+';
						else
							s[i+j]='-';
					}	
				}
				//cout<<s<<endl;
				cnt++;
				i=tmp_i;
			}
		}
		for(i=0;s[i]!='\0';i++)
		{
			if(s[i]=='-')
				break;
		}
		cout<<"Case #"<<z<<": ";
		if(s[i]!='\0')
			cout<<"IMPOSSIBLE"<<endl;
		else	
			cout<<cnt<<endl;
	}
	return 0;
}
