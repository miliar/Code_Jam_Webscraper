#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<ll> vl;

#define MOD 1000000007
#define tc int t;scanf("%d",&t);while(t--)
#define pb push_back
#define ff(i,a,b) for(int i=a;i<b;i++)
#define mp make_pair
#define pf printf
#define sf scanf
#define bs binary_search
#define nl printf("\n")
#define si(x) int x;scanf("%d",&x)
#define sll(x) ll x;scanf("%lld",&x)
#define pi(x) printf("%d\n",x )

int main()
{
	 freopen("B-small-attempt0.in","r",stdin);
    freopen("2.out","w",stdout);
    int x=1;
    tc
    {
    	
    	
    	sll(n);
    	cout<<"Case #"<<x<<": ";
    	if(n%10==n)
    		cout<<n<<"\n";
    	else
    	{
    		while(n)
    		{
    			vl v;
    			ll p=n;
    			int flag=1;
    			while(p>0)
    			{
    				int k1=p%10;
    				p/=10;
    			//	cout<<"k1="<<k1<<"\n";
    				v.pb(k1);

    			}
    			//break;
    			vl::iterator it;
    			for(it=v.begin();it!=v.end();it++)
    			{
    				if(*(it-1)<*(it) && it!=v.begin())
    				{
    					flag=0;
    					//cout<<*it<l;
    					break;
    				}
    				//cout<<*it;
    			}
    			if(flag==1)
    				break;
    			n--;
    			v.clear();
    		}
    		cout<<n<<"\n";
    		
    	}
    	x++;
    }
return 0;
}