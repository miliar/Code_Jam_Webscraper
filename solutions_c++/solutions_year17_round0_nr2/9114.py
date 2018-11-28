#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);
	int t;
	scanf("%d",&t);
	int z=1;
	while(t--)
	{
		long long int n,temp;
		scanf("%lld",&n);
		temp=n;
		int len=0;
		stack<int>s;
		int prev=10;
		int check1=1;
		while(temp)
		{
			int temp1=temp%10;
			if(temp1<=prev)
			prev=temp1;
			else 
			check1=0;
			s.push(temp1);
			len++;
			temp/=10;
		}
		if(check1==1)
		printf("Case #%d: %lld\n",z++,n);
		else
		{
				long long int ans=s.top();
				temp=s.top();
				s.pop();
				int count0=0;
		    while(s.empty()==false)
		     {
		     	 if(s.top()>temp)
		     	 {
		     	 	ans=ans*10+s.top();
		     	 	temp=s.top();
		     	 	s.pop();
					 }  
					 else if(s.top()==temp)
					 {
					 	count0++;
					 	s.pop();
					 	while(s.top()==temp)
					 	{
					 		count0++;
					 		s.pop();
						}
						if(temp<s.top())
						{
							int i;
							for(i=0;i<count0;i++)
							ans=ans*10+temp;
						}
						else
						{
							ans=ans*pow(10,count0+s.size());
							break;
						}
						temp=s.top();
					 	
					 }
					 else
					 {
					 	ans=ans*pow(10,s.size());
					 	break;
					 }
		    }
		    	printf("Case #%d: %lld\n",z++,ans-1);
		}
	}
	return 0;
}
