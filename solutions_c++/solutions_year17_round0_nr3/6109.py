#include<iostream>
#include<queue>
using namespace std;
int main()
{	
	int t;
	cin>>t;
	for(int j=0;j<t;j++)
	{
		queue<long long int> queue;
		long long int bath,pep;
		cin>>bath>>pep;
		long long int ans,ans1;
		queue.push(bath);
		long long int x=0,y=1,flag=0;
		for(long long int i=0;i<pep;i++)
		{
			long long int temp = queue.front();
			queue.pop();
			if(temp%2==0)
			{
				ans = temp/2;
				ans1 = ans-1;
				while(!queue.empty() && queue.front()==temp)
				{
					flag=1;
					y++;
					queue.pop();
				}
			}
			else
			{
				ans = temp/2;
				ans1 = ans;
			}
			if(flag==0)
			{
			
			if(ans!=0)
			{
				queue.push(ans);
			}
			if(ans1!=0)
			{
				queue.push(ans1);
			}
		}
		else
		{
			flag=0;
			for(long long int s = 0;s<y;s++)
			{
			if(ans!=0)
			{
				queue.push(ans);
			}
			
			}
				for(long long int s = 0;s<y;s++)
			{
			if(ans!=0)
			{
				queue.push(ans1);
			}
			
			}
			i=i+y-1;
			y=1;
		}
		}
		printf("Case #%d: %lld %lld\n",j+1,ans,ans1);
	}
	return 0;
}
