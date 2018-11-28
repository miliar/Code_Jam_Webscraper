#include<bits/stdc++.h>

#define dbg printf("%s\n",str);
using namespace std;

int main()
{
int t;
cin>>t;
int x=1;
	while(x<=t)
	{
		char str[1001];
		int k,ctr=0,flag=0;
		scanf("%s %d",str,&k);
		int l = strlen(str);
		for(int i=0;i<l;++i)
		{	
			if(str[i]=='+')
				continue;
			if(i+k>l)
			{
				cout<<"Case #"<<x<<": IMPOSSIBLE"<<endl;
				flag = 1;
				break;
			}
			ctr++;
			for(int j=0;j<k;++j)
			{
				
				if(str[i+j]=='+') str[i+j]='-';
				else str[i+j]='+';

			}
		}
		if(flag==0)
		cout<<"Case #"<<x<<": "<<ctr<<endl;
		x++;
	}
return 0;
}
