#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int p=1;p<=t;p++)
	{
		int N,i,flag=1;
		cin>>N;
		
		for(i=N;i>=1;i--)
		{
			flag=1;
			int num=i;
			if(num/10==0)
				break;
			
			int x=num/10;
			while(x)
			{
				int a=num%10;
				int b=x%10;
				if(b>a)
				{
					flag=0;		
					break;
				}
					x=x/10;
					num=num/10;
			}
			if(flag)
				break;	
		}
		cout<<"Case #"<<p<<": "<<i<<endl;
	}
	
}
