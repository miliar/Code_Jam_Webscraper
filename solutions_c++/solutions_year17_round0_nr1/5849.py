#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t,q=1;
	cin>>t;
	while(t--)
	{
		char s[1005];
		cin>>s;
		int k,l=strlen(s),count=0;
		cin>>k;
		for(int i=0;i<l;i++)
		{
			if(s[i]=='-')
			{
				count++;
				int run=k,j=i;
				if(j+run<=l)
				{
					//cout<<j+run<<endl;
				while(run--)
				{
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
					j++;
				}
			}
			}
		}
		int x=0;
		for(int i=0;i<l;i++)
		{
			if(s[i]=='-')
			{
				x=1;
				break;
			}
		}
		if(x==1)
			printf("Case #%d: IMPOSSIBLE\n",q);
		else
			printf("Case #%d: %d\n",q,count);
		q++;
	}	
	return 0;
} 