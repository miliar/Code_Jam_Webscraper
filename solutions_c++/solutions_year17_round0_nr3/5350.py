//  Created by Chlerry in 2017.
//  Copyright (c) 2017 Chlerry. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <climits>
#include <string>
#include <vector>
#include <cmath>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;
#define Size 1000010
#define ll long long
#define mk make_pair
#define pb push_back
#define mem(array, x) memset(array,x,sizeof(array))
typedef pair<int,int> P;

int main()
{
    // freopen("in.txt","r",stdin);

    int T;cin>>T;
for(int ca=0;ca<T;ca++)
{
	// cout<<"-----------------"<<endl;
	long long n,k;cin>>n>>k;
	priority_queue<ll> q; 
	q.push(n);
	for(int i=0;i<k-1;i++)
	{
		if(q.empty())
			break;
		ll t=q.top();
		q.pop();
		ll a=(t+1)/2;
		ll b=t-a;
		a--;
		if(a>1) q.push(a);
		if(b>1) q.push(b);
	}
	ll a,b;
	if(!q.empty())
	{
		ll t=q.top();
		q.pop();
		a=(t+1)/2;
		b=t-a;
		a--;
		printf("Case #%d: %lld %lld\n",ca+1,max(a,b),min(a,b));
	}
	else 
		printf("Case #%d: 0 0\n",ca+1);
}
    return 0;
}
