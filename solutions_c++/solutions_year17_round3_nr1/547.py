#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
const ld PI=acos(ld(-1));
void ioinit()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
}

struct Node
{
	ld h,r;
	bool operator < (const Node & t) const
	{
		return r>t.r||(r==t.r&&h>t.h);
	}
}a[1007];
ld dp[1007];
ld S(ld r,ld h)
{
	return 2*PI*r*h;
}
int main()
{
	ioinit();
	int T;
	cin>>T;
	for(int kase=1;kase<=T;kase++)
	{
		int n,k;
		cin>>n>>k;
		a[0].r=10000000;
		for(int i=1;i<=n;i++) cin>>a[i].r>>a[i].h;
		sort(a+1,a+n+1);
		for(int i=1;i<=n;i++) dp[i]=0;
		for(int i=1;i<=n;i++)
		{
			for(int j=(i<k?i:k);j>0;j--)
			{
				if(j==1) dp[j]=max(dp[j],S(a[i].r,a[i].h)+PI*a[i].r*a[i].r);
				else dp[j]=max(dp[j],dp[j-1]+S(a[i].r,a[i].h));
			}
			//cout << dp[1] << " " << dp[2] << endl;
		}
		printf("Case #%d: %.15f\n",kase,(double)dp[k]);
	}
	return 0;
}
