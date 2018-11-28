#include<algorithm>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include  <stdio.h>
#include   <math.h>
#include   <time.h>
#include   <vector>
#include   <bitset>
#include    <queue>
#include      <set>
#include      <map>
using namespace std;

typedef long long LL;

LL N,haha=100000000000000000ll;

void solve()
{
	cin>>N;
	while(true)
	{
		int flag=0;
		for(LL i=haha;i;i/=10)
			if(N/i%10<N/(i*10)%10)
			{
				N=N/i/10*i*10-1;
				flag=1;
				break;
			}
		if(!flag)
			break;
	}
	cout<<N<<endl;
}

int main()
{
//#ifndef ONLINE_JUDGE
//	freopen("B.in","r",stdin);
//	freopen("B.out","w",stdout);
//#endif
	int T;cin>>T;
	for(int i=1;i<=T;i++)
		printf("Case #%d: ",i),solve();
	return 0;
}

