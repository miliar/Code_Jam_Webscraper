#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <queue>
#include <deque>
#include <algorithm>

using namespace std;

bool cmp(long long int a, long long int b)
{
	return a > b;
}
int main()
{
	int n;
	scanf("%d",&n);
	for (int x = 0; x < n; ++x)
	{	
		long long int num,people;
		scanf("%lld%lld",&num,&people);
		deque<long long int> data;
		data.push_back(num);
		long long int fir;
		while(people>0)
		{	
			fir = data.front();
			sort(data.begin(),data.end(),cmp);
			data.pop_front();
			if (fir%2==1)
			{
				data.push_back(fir/2);
				data.push_back(fir/2);
			}
			else{
				data.push_back(fir/2);
				data.push_back(fir/2-1);
			}
			people--;
		}
		long long int ans1=0,ans2=0;
		if (fir%2==1 )
		{
			ans1 = fir/2;
			ans2 = fir/2;
		}
		else{
			ans1 = fir/2;
			ans2 = fir/2-1;
		}
		printf("Case #%d: %lld %lld\n", x+1,ans1,ans2 );
	}
	return 0;
}