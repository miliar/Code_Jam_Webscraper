#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <string>
#include <time.h>

#define SQR(_x) ((_x)*(_x))
#define NL printf("\n")
#define LL long long
#define DB double
#define PB push_back
#define INF 1<<30
#define LB lower_bound
#define UB upper_bound
#define F front
#define PQ priority_queue

using namespace std;

struct data{
	long long mx,mn,l,r;
	data(long long a,long long b,long long c,long long d){
		mx=a;
		mn=b;
		l=c;
		r=d;
	}
	bool operator < (const data &T) const{
		if(mn == T.mn)
			return mx < T.mx;
        return mn < T.mn;
    }
};

priority_queue<data> q;

int main()
{
	int t,x=1;
	scanf("%d",&t);
	while(t--)
	{
		while(not q.empty())
			q.pop();
		long long n,k;
		long long l,r,mx,mn,m;
		long long mx_l,mn_l,mx_r,mn_r;
		scanf("%lld%lld",&n,&k);
		l=0;
		r=n+1;
		m=(l+r)/2;
		mx = r-m-1;
		mn = m-l-1;
		q.push(data(mx,mn,l,r));
		for(long long i=0;i<k-1;i++){
			l = q.top().l;
			r = q.top().r;
			// printf("%lld %lld\n",l,r);
			m = (l+r)/2;
			mx_l = m-(m+l)/2-1;
			mn_l = (m+l)/2-l-1;
			mx_r = r-(m+r)/2-1;
			mn_r = (m+r)/2-m-1;
			// printf("=== L %lld %lld === R %lld %lld \n",mx_l,mn_l,mx_r,mn_r);
			if(mx_l>=0 and mn_l>=0)
				q.push(data(mx_l,mn_l,l,m));
			if(mx_r>=0 and mn_r>=0)
				q.push(data(mx_r,mn_r,m,r));
			q.pop();
		}
		mx=q.top().mx;
		mn=q.top().mn;
		l=q.top().l;
		r=q.top().r;
		printf("Case #%d: %lld %lld\n",x,mx,mn);
		x++;
	}
	return 0;
}








