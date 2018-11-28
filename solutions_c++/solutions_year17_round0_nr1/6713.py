//Sinha Saab
//NARUTO Fan



#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <math.h>

#define ll long long int
#define maxN 100000
#define maxVal 100000000
#define minVal -100000000
#define mod 1000000007LL

#define gcd(a,b) __gcd(a,b)

using namespace std;

int k,n;
char a[1005];

int main()
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef LOCAL_SYS
        freopen("A-large.in","r",stdin);
        freopen("out.txt","w",stdout);
    #endif
    int t,i,j,tc,z,ans;
    scanf("%d",&t);
    for(tc=1;tc<=t;tc++)
    {
    	scanf("%s%d",a,&k);
    	n=strlen(a);
    	ans=0;
    	z=1;
    	for(i=0;i<n;i++)
    	{
    		if(a[i]=='+')
    			continue;
    		if((i+k)<=n)
    		{
    			for(j=i;j<(i+k);j++)
    				if(a[j]=='+')
    					a[j]='-';
    				else
    					a[j]='+';
				ans++;
    		}
    		if(a[i]=='-')
    			z=0;
    	}
    	if(z)
    		printf("Case #%d: %d\n",tc,ans);
    	else
    		printf("Case #%d: IMPOSSIBLE\n",tc);
    }
    return 0;
}