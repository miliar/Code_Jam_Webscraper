#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int T;
ll n;

bool check(ll n)
{
	int t=n%10;
	n/=10;
	while(n)
	{
		if(t>=n%10)
		{
			t=n%10;
			n/=10;
		}
		else
			return 0;
	}
	return 1;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B.out","w",stdout);
#endif
	scanf("%d",&T);
	int kase=1;
	bool flag=0;
	while(T--){
		cin >> n;
		flag=0;
		for(ll i=n;i>=0;i--)
		{
			if(check(i))
			{
				printf("Case #%d: %d\n",kase++,i);
				flag=1;
				break;
			}
		}


	}
	return 0;
}
