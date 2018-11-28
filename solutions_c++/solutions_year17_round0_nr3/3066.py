#include <bits/stdc++.h>
using namespace std;

#define pq priority_queue<long long int>
#define mp map<long long int, long long int>  
#define lli long long int

pq p;
mp m;

void makepairs(lli &a, lli &b, lli K , lli N)
{
	if(m[a]==0)
        p.push(a);
    m[a]++;
    if(m[b]==0)
        p.push(b);
    m[b]++;
    lli pairs = 1;
    while(pairs < K)
	{
        N = p.top();
	    p.pop();
	    pairs += m[N];
	    if(!(N&1))
		{
			a = (N/2)-1;
			b = N/2;
		}
		else {
			a = (N/2);
			b = a;
		}
    	if(m[a]==0)
            p.push(a);
        m[a] += m[N];
        if(m[b]==0)
            p.push(b);
        m[b] += m[N];
    }
}

int main()
{
	int t,Case=1;
	scanf("%d", &t);
	while(t--){
		lli N,K;
		scanf("%lld %lld",&N,&K);
		printf("Case #%d: ",Case);Case++;
		lli pairs,a,b;
		if(!(N&1))
		{
			a = (N/2)-1;
			b = N/2;
		}
		else {
			a = (N/2);
			b = a;
		}
		makepairs(a,b, K, N);
		printf("%lld %lld\n",b,a);
		while(!(p.empty()))
		p.pop();
		m.erase(m.begin(),m.end());
	}
	
	return 0;
}