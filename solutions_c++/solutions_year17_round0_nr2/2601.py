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
char s[25];
int a[25];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,i,j,k,x,l;
    ll ans;
    sd(t);
    for(x=1;x<=t;x++)
    {
    	ss(s);
    	n=strlen(s);
    	for(i=0;i<n;i++)
    		a[i]=s[i]-'0';
    	l=0;
    	for(i=1;i<n;i++)
    	{
    		if(a[i]>a[l])
    			l=i;
    		else if(a[i]<a[l])
    			break;
    	}
    	printf("Case #%d: ",x);
    	if(i<n)
    	{
    		a[l]--;
    		for(i=l+1;i<n;i++)
    			a[i]=9;
    	}
    	ans=0;
    	for(i=0;i<n;i++)
    		ans=ans*10+a[i];
    	printf("%lld\n",ans);
    }
    return 0;
}