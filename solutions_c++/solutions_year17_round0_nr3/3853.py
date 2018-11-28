#include <bits/stdc++.h>
using namespace std;
int main()	
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<t+1;i++)
	{
		long long c=0;
		long long n,k;
		scanf("%lld %lld",&n,&k);
		printf("Case #%d: ",i);
		priority_queue<long long,vector<long long>,greater<long long> > pq;

		if(n%2==0){
			pq.push(-(n/2));
			pq.push(-(n-(n/2)-1));
			if(k==1){
				printf("%lld %lld\n",n/2,(n-(n/2)-1));
				continue;}
		}		
		else{
			pq.push(-(n/2));
			pq.push(-(n/2));
			if(k==1){
				printf("%lld %lld\n",n/2,n/2);
				continue;}
		}
		for(long long j=0;j<k-2;j++){
			c=-(pq.top());
			pq.pop();
			if(c%2==0)
				pq.push(-(c-(c/2)-1));
			else
				pq.push(-(c/2));
			pq.push(-(c/2));
		}
		c=-(pq.top());
		pq.pop();
		if(c%2!=0){
			printf("%lld %lld\n",c/2,c/2);
		}
		else{
			printf("%lld %lld\n",c/2,(c-(c/2)-1));
		}
	}
	return 0;
}
