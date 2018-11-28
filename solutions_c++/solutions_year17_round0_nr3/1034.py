#include <iostream>
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

unordered_map<ll, ll> m;

int main()
{
    int T;
    scanf("%d",&T);
    for(int test=1; test<=T; test++)
    {
        printf("Case #%d: ",test);
        m.clear();
        priority_queue<ll> q;
        ll n, k;
        scanf(" %lld %lld", &n, &k);
        q.push(n); m[n]++;
        ll t;
        while(k>0)
        {
        	t = q.top();
        	q.pop();
        	ll c = m[t];
        	k -= c;
        	if(t%2 == 0)
        	{
        		if(m[t/2] == 0)
        			q.push(t/2);
        		m[t/2] += c;
        		if(m[t/2-1] == 0)
        			q.push(t/2-1);
        		m[t/2-1] += c;
        	}
        	else
        	{
        		if(m[t/2] == 0)
        			q.push(t/2);
        		m[t/2] += 2*c;
        	}
        }
        if(t%2 == 0)
        	printf("%lld %lld\n", t/2, t/2-1 );
        else
        	printf("%lld %lld\n", t/2, t/2 );
    }
    return 0;
}
