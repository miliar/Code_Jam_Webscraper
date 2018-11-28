#include<bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<LL,LL> PLL;
#define MP make_pair
PLL cal(LL n,LL k)
{
	//cout <<n<<" "<<k<<endl;
	if(n==1)
	{
		return MP(k/2,k/2-(k%2==0));
	}
	PLL res;
	if(n%2==0&&k%2==1)
		return res=cal(n/2,k/2);
	if(n%2==1&&k%2==1)	
		return res=cal(n/2,k/2);
	if(n%2==0&&k%2==0)
		return res=cal(n/2,k/2);
	if(n%2==1&&k%2==0)
		return res=cal(n/2,k/2-1);
}
void solve(int cas)
{
 	LL n,k;	
	scanf("%I64d%I64d",&n,&k);
	PLL res=cal(k,n);
	printf("Case #%d: %I64d %I64d\n",cas,res.first,res.second);
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;++cas)
		solve(cas);
}
