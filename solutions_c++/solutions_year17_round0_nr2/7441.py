#include<bits/stdc++.h>
using namespace std;
long long tidy(long long n)
{
	stack<long long> s;
	long long tmp=1;
	if(n%10==0)return tmp;
	s.push(n%10);
	n/=10;
	while(n)
	{
		if(n%10>s.top())return tmp;
		s.push(n%10);
		n/=10;
		tmp*=10;
	}
	return 0;
}
int main()
{
	int T,c=1;
	bool found;
	long long N;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%lld",&N);
		found=false;
		while(!found)
		{
			found=!tidy(N);
			N--;
		}
		printf("Case #%d: %lld\n",c,N+1);
		c++;
	}
	return 0;
}