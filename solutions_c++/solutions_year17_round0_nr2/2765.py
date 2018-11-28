#include <bits/stdc++.h>
#define si(n) scanf("%d",&n);
#define pi(n) printf("%d\n",n);
#define pl(n) printf("%lld\n",n);
#define sl(n) scanf("%lld",&n);
#define sd(n) scanf("%lf",&n);
#define pd(n) printf("%lf\n",n);
#define ss(s) scanf("%s",s);
#define ps(s) printf("%s\n",s);
#define pb push_back
#define ll long long int
#define maxn 10005
#define sqrtn 317
#define maxm 1000005
#define minv(a,b,c) min(a,min(b,c))
#define pii pair<int,int>
#define pll pair<ll,ll>
#define eps 1e-9
#define mod 1000000007
#define psi pair < string,ll>
#define mp make_pair
#define BLOCK 450
using namespace std;
ll s[20];

int main()
{
	int t;
	si(t);
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		ll num;
		sl(num);
		int c=0;
		while(num!=0)
		{
			s[c]=num%10;
			num=num/10;
			c++;
		}
		c--;
		for(int i=c-1;i>=0;i--)
		{
			if(s[i]<s[i+1])
			{
				s[i+1]--;
				for(int j=0;j<=i;j++)
				{
					s[j]=9;
				}
				int aux=i+1;
				while(aux<c && s[aux]<s[aux+1])
				{
					s[aux]=9;
					s[aux+1]--;
					aux++;
				}
			}
		}
		num=0;
		/*ps("");
		for(int i=0;i<=c;i++)
		{
			printf("%lld",s[i] );
		}*/
		for(int i=c;i>=0;i--)
		{
			num=num*10+s[i];
		}
		pl(num);
	}

}