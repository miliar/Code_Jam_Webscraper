#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int>   II;
typedef vector< II >      VII;
typedef vector<int>     VI;
typedef vector< VI > 	VVI;
typedef long long int 	LL;

#define PB push_back
#define MP make_pair
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define si(n) scanf("%d",&n)
#define dout(n) printf("%d\n",n)
#define sll(n) scanf("%lld",&n)
#define lldout(n) printf("%lld\n",n)
#define fast_io ios_base::sync_with_stdio(false);cin.tie(NULL)

int main()
{
	int t,l=1;
	si(t);
    for(l=1;l<=t;l++)
    {
    	char ar[1010];
    	scanf("%s",ar);
    	int k;
    	si(k);
    	int len = strlen(ar);
    	int f = 0,i=0,j=0;
    	for(i=0;i<len-k+1;i++)
    	{
    		if(ar[i] == '-')
    		{
    			f++;
    			for(j=i;j<i+k;j++)
    			{
    				if(ar[j] == '-')
    					ar[j] = '+';
    				else
    					ar[j] = '-';
    			}
    		}
    	}
    	int flag = 1;
    	for(i=0;i<len;i++)
    	{
    		if(ar[i]=='-')
    			flag = 0;
    	}
    	printf("Case #%d: ",l);
    	if(flag)
    		printf("%d\n",f);
    	else
    		printf("IMPOSSIBLE\n");
    }
	return 0;
}