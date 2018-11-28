#include<iostream>
#include<string.h>
using namespace std;
main()
{
	int t,k,len,count=0,x=1;
	char s[1000];
	cin>>t;
	while(t>0)
	{	
		cin>>s;
		cin>>k;
		len = strlen(s);
		for(int i=0;i<len;i++)
		{
			if(s[i] == '-')
			{
				if (i+k > len)
				{
					count = -1;
					break;
				}
				for(int j=i;j<i+k;j++)	
				{
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
				//cout<<s<<endl;
				count++;
			}
			
		}
		if(count>-1)
			cout<<"Case #"<<x<<": "<<count<<endl;
		else
			cout<<"Case #"<<x<<": IMPOSSIBLE"<<endl;
		t--;
		x++;
		count = 0;
	}
}
