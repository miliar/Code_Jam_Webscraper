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
	int t,k;
	si(t);
	for(k=1;k<=t;k++)
	{
		char ar[100];
		scanf("%s",ar);
		int len = strlen(ar), i=0, j=0;
		if(len!=1)
		{
			for(i=0;i<len-1;i++)
			{
				if(ar[i]-'0' > ar[i+1] - '0')
				{
					if(ar[i]-'0' == 1)
					{
						ar[i] = 0 + '0';
						for(j = i+1;j<len;j++)
						{
							ar[j] = 9 + '0';
						}
						if(i>0 && ar[i-1] - '0' > ar[i] - '0')
						{
							//printf("%d\n",i);
							i = i - 2;
						}
					}
					else
					{
						ar[i] =  ar[i] - 1;
						for(j = i+1;j<len;j++)
						{
							ar[j] = 9 + '0';
						}
						if(i>0 && ar[i-1] > ar[i])
						{
							i = i - 2;
						}
					}
				}
			}
	    }
	    printf("Case #%d: ",k);
	    int flag = 1;
	    for(i=0;i<len;i++)
	    {
            if(flag==0 || ar[i]!='0')
            {
            	flag = 0;
	            printf("%c",ar[i]);
            }
	    }
	    printf("\n");
	}
	return 0;
}