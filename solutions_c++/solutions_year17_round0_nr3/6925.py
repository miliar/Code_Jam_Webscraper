#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;
long long int *que,end,now;
int all_zero;

bool compare(long long int a,long long int b)
{
	return a>b;
}

void run(long long int n)
{
	long long int temp,temp2;
	while(n<=end)
	{
		temp=(que[n]-1)/2,temp2=que[n++];
		if(!temp2)
		{
			all_zero=1;
			return;
		}
		else if(!temp)
			continue;
		else if(temp2%2)
		{
			que[now++]=temp;
			que[now++]=temp;
			sort(que+n,que+now,compare);
		}
		else 
		{
			que[now++]=temp+1;
			que[now++]=temp;
			sort(que+n,que+now,compare);
		}
	}
	return;
}

int main()
{
	long long int t,k,n,i,temp;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>n>>end;
		que=new long long int[n+10]();
		now=1;
		que[now++]=n;
		all_zero=0;
		run(1);
		cout<<"Case #"<<i<<": ";
		temp=que[end];
		if(all_zero||!temp)
			cout<<0<<" "<<0<<endl;
		else if(!(temp%2))
			cout<<(temp-1)/2+1<<" "<<(temp-1)/2<<endl;
		else
			cout<<(temp-1)/2<<" "<<(temp-1)/2<<endl;
		delete []que;
	}
	return 0;
}