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

map<LL,LL> S;

LL n,k;

void solve()
{
	cin>>n>>k;S.clear();S[n]=1;
	while(k)
	{
		map<LL,LL>::iterator it=--S.end();
		LL len=it->first,Num=it->second;
		S.erase(it);
		LL ls=len/2-!(len%2),rs=len-ls-1;
		if(Num>=k)
		{
			printf("%lld %lld\n",rs,ls);return;
		}
		k-=Num;
		S[ls]+=Num;S[rs]+=Num;
	}
}

int main()
{
//#ifndef ONLINE_JUDGE
//	freopen("C.in","r",stdin);
//	freopen("C.out","w",stdout);
//#endif
	int T;cin>>T;
	for(int i=1;i<=T;i++)
		printf("Case #%d: ",i),solve();
	return 0;
}

