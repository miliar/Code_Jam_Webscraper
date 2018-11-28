
#include<bits/stdc++.h>

using namespace std;

#define ll long long

#define sci(x) scanf("%d",&x)
#define scl(x) scanf("%lld",&x)
#define scd(x) scanf("%lf",&x)

#define pfi(x) printf("%d",x)
#define pfl(x) printf("%lld",x)
#define pfd(x) printf("%lf",x)
#define pfc(x) printf("Case #%d: ",x++)
#define ps printf(" ")
#define pn printf("\n")

#define pb(x) push_back(x)
#define ppb(x) pop_back(x)
#define pf(x) push_front(x)
#define ppf(x) pop_front(x)
#define in(x,y) insert({x,y})
#define sv(a) sort(a.begin(),a.end())

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    int test,caseno=1;
    sci(test);

    while(test--)
    {
    	string data;
    	cin>>data;
    	int k;
    	sci(k);
    	int len=data.length();
    	int ans=0;

    	for(int i=0;i<len;i++)
    	{
    		if(data[i]=='-')
    		{
    			if(i+k<len)
    			{
    				ans++;
    				for(int j=i;j<(i+k);j++)
    				{
    					if(data[j]=='-')
    					{
    						data[j]='+';
    					}
    					else
    						data[j]='-';
    				}
    			}
    		}
    	}

    	for(int i=len-1;i>=0;i--)
    	{
    		if(data[i]=='-')
    		{
    			if(i-k>=-1)
    			{
    				ans++;
    				for(int j=i;j>(i-k);j--)
    				{
    					if(data[j]=='-')
    					{
    						data[j]='+';
    					}
    					else
    						data[j]='-';
    				}
    			}
    		}
    	}
    	bool done=true;
    	for(int i=0;i<len;i++)
    	{
    		if(data[i]=='-')
    		{
    			done=false;
    		}

    	}
    	pfc(caseno);
    	if(done)
    	{
    		pfi(ans),pn;
    	}
    	else
    		printf("IMPOSSIBLE\n");
        
    }

    return 0;
}
