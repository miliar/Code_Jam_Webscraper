#include<bits/stdc++.h>
using namespace std;

#define sd(mark) scanf("%d",&mark)
#define ss(mark) scanf("%s",mark)
#define sl(mark) scanf("%lld",&mark)
#define debug(mark) printf("check%d\n",mark)
#define clr(mark) memset(mark,0,sizeof(mark))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define ll long long

bool isTidy(ll n)
{
	int prev=10;
	while(n)
	{
		int cur=n%10;
		n/=10;
		if(cur>prev)	return false;
		prev=cur;
	}
	return  true;
}

int main()
{
	// freopen ("B.in","r",stdin);
	// freopen ("B.out","w",stdout);
	int t;
	sd(t);
	for(int tt=1;tt<=t;tt++)
	{
		int n,i;
		sd(n);
		for(i=n;i>=1;i--)
			if(isTidy(i))
				break;
		printf("Case #%d: %d\n",tt,i);
	}
}