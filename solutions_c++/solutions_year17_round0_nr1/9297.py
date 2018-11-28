#include <iostream>
using namespace std;

int main()
{
	int t, n, ans=0;
	cin>>t;
	while(t--)
	{
		ans++;
		int c=0;
		char s[1100];
		cin>>s>>n;
		for(int i=0; s[i]!='\0'; i++)
		{
			if(s[i]=='-')
			{
				int k=i;
				for(int j=0; j<n; j++)
				{
					if(s[i]=='\0')
					{
						s[i-1]='-';
						break;
					}
					//cout<<i<<endl;
					if(s[i]=='+')
						s[i]='-';
					else
						s[i]='+';
					//cout<<s[i];
					i++;
				}
				c++;
				i=k;
			}
			//cout<<s<<" "<<i<<endl;
		}
		int check=0;
		for(int i=0; s[i]!='\0'; i++)
		{
			if(s[i]=='-')
			{
				check=1;
				break;
			}
		}
		if(check==0)
		{
			cout<<"Case #"<<ans<<": "<<c<<endl;
		}
		else
		{
			cout<<"Case #"<<ans<<": "<<"IMPOSSIBLE"<<endl;
		}
	}
}