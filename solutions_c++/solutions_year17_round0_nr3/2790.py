#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<map>
using namespace std;
typedef long long LL;
LL n,k;
map<LL,LL> S;
int main()
{
	int T;
	LL n,ans;
	cin>>T;
	for(int qi=1;qi<=T;qi++)
	{
		printf("Case #%d: ",qi);
		cin>>n>>k;
		S.clear();
		S[n]=1;
		k--;
		while(k)
		{
			LL x,y;
			x=S.rbegin()->first;
			y=S.rbegin()->second;
			y=min(y,k);
			S[x]-=y;
			S[x-1>>1]+=y;
			S[x>>1]+=y;
			if(S.rbegin()->second==0)
				S.erase(x);
			k-=y;
		}
		LL t=S.rbegin()->first;
		cout<<(t>>1)<<' '<<(t-1>>1)<<endl;
	}
	return 0;
}
