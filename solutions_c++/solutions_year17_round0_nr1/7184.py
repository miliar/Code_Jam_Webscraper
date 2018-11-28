#include <iostream>
#include <cstring>
using namespace std;
int main()
{
	int t,x,k,i,j,ans;
	char s[2005];
	cin>>t;
	for(x=1;x<=t;x++)
	{
		ans=0;
		int flag=0;
		cin>>s;
		cin>>k;
		int len=strlen(s);
		for(i=0;i<len-k+1;i++)
		{
			if(s[i]=='-')
			{
				for(j=0;j<k;j++)
				{
					if(s[i+j]=='-')
						s[i+j]='+';
					else
						s[i+j]='-';
				}
				ans++;
			}
		}
		for(i=0;i<len;i++)
		{
			if(s[i]=='-')
			{
				flag=1;
				break;
			}
		}
		if(flag==1)
			cout<<"Case #"<<x<<": IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<x<<": "<<ans<<endl;
	}
	return 0;
}
