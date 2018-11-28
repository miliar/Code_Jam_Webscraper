#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define ll long long
#define mod 1000000007
#define bitcount    __builtin_popcountll
#define pb push_back
#define fi first
#define se second
#define mp make_pair
#define pi pair<int,int>
int a[1003],b[1003];
char s[1003];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,m,i,j,k,l,ans;
    sd(t);
    for(k=1;k<=t;k++)
    {
    	ss(s);
    	n=strlen(s);
    	sd(m);
    	for(i=0;i<n;i++)
    	{
    		if(s[i]=='-')
    			a[i+1]=1;
    		else
    			a[i+1]=0;
    		b[i+1]=0;
    	}
    	ans=0;
    	l=0;
    	for(i=1;i<=(n-m+1);i++)
    	{
    		l+=b[i];
    		a[i]=(a[i]+l)%2;
    		if(a[i])
    		{
    			ans++;
    			a[i]=0;
    			l++;
    			b[i+m]--;
    		}
    	}
    	for(i;i<=n;i++)
    	{
    		l+=b[i];
    		a[i]=(a[i]+l)%2;
    	}
    	for(i=1;i<=n;i++)
    	{
    		if(a[i])
    			break;
    	}
    	printf("Case #%d: ",k);
    	if(i==n+1)
    		printf("%d\n",ans);
    	else
    		printf("IMPOSSIBLE\n");
    }
    return 0;
}