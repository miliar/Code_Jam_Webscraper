#include <iostream>

#include <cstring>

#include <string>

using namespace std;

string comp1,comp2;

int main()
{
	int t,len,z=0;

	cin>>t;

	string comp1(1001,'+');

	string comp2(1001,'-');

	while(t)
	{
		z++;

		int k;

		string str,comp;

		cin>>str>>k;

		len=str.size();

		int ans=0;

		for(int i=0;i<len-k;i++)
		{
			if(str[i]=='-')
			{
				for(int j=i;j<k+i;j++)
				{
					if(str[j]=='-')str[j]='+';

					else if(str[j]=='+') str[j]='-';
				}
			
				ans++;
			}
		}

		comp=str.substr(len-k,k);
		
		string temp1=comp1.substr(0,k);

		string temp2=comp2.substr(0,k);

		if(comp==temp1)
		{	
			cout<<"Case #"<<z<<": "<<ans<<endl;
		}

		else if(comp==temp2)
		{
			ans++;

			cout<<"Case #"<<z<<": "<<ans<<endl;
		}

		else
		{
			cout<<"Case #"<<z<<": "<<"IMPOSSIBLE"<<endl;	
		}

		t--;
	}

	return 0;
}