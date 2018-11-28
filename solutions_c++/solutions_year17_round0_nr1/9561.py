#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t,p=1;
	cin>>t;
	cin.ignore();
	while(t--)
	{
		int count=0,temp=1;
		string s;
		int k,i,j;

		cin>>s;
		cin>>k;
		//cout<<s<<k;
		for(i=0;i<=(s.length()-k);i++)
		{
			if(s[i]=='-')
				{
					count++;
			for(j=i;j<i+k;j++)
			{
				if(s[j]=='-')s[j]='+';
				else s[j]='-';


			}
		}
		}
		for(i=s.length()-k;i<s.length();i++)
        {if(s[i]=='-')
				{temp=0;}
        }
        if(temp==0)
        {cout<<"Case #"<<p<<": IMPOSSIBLE"<<"\n";
        }
        else
		cout<<"Case #"<<p<<": "<<count<<"\n";

		p++;
	}
	return 0;
}

