#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ll;

ll large_limit = 1000000000000000000LL;

ll array[ 4686824 ];

void init()
{
	queue<ll> Queue;
	int cnt = 0;
	for(int i=1;i<10;++i)
	{
		Queue.push(i);
		array[cnt++] = i;
	}
	ll K;
	//int cnt = 9;

	while(!Queue.empty())
	{
		K = Queue.front();
		int last_index = K%10;
		Queue.pop();

		for(int i=last_index ; i<10; ++i)
		{
			ll tmp = K*10 + i;
			assert(tmp>0LL);
			if(tmp < large_limit)
			{
				//cout<<tmp<<endl;
				array[cnt++] = tmp;
				Queue.push(tmp);
			}
			
		}
	}

//	cout<<cnt<<"   "<<array[cnt-1]<<endl;
}
ll Solve(int start,int end,ll data)
{
	ll mid ;
	while(start <= end)
	{
		mid = (start + end)/2;
		if(array[mid] == data)
			return array[mid];

		if(array[mid] > data)
			end = mid - 1;
		else
			start = mid+1;
	}
	return array[end];
}
int main()
{
	int T;
	int start = 0;
	int end = 4686823 ;
	ll data;
	init();
	cin>>T;
	for(int i=1;i<=T;++i)
	{
		scanf("%llu",&data);
		ll K = Solve(start ,end ,data);
		printf("Case #%d: %llu\n",i,K);
	}
	return 0;
}