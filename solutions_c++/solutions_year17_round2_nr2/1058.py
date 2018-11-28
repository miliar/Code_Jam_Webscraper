#include <bits/stdc++.h>
#define mp make_pair
#define ff first
#define se second
#define pb push_back
#define nn 1010
#define pii pair<int,int>
#define mt make_tuple
#define ll long long int
#define pdd pair<long double,long double>
#define db double
#define pll pair<ll,ll>
#define pli pair<ll,int>
#define inf 10000000000010ll
#define logn 20
#define mod 1000000007
#define mt make_tuple
 
using namespace std;

bool m[nn];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    #ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    #endif
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
    	cout<<"Case #"<<tt<<": ";
    	memset(m,0,sizeof m);
    	int l[nn];
    	int n,c[6];
    	set<int>a[6];
    	a[0].insert(2);
    	a[0].insert(3);
    	a[0].insert(4);
    	a[1].insert(4);
    	a[2].insert(0);
    	a[2].insert(4);
    	a[2].insert(5);
    	a[3].insert(0);
    	a[4].insert(0);
    	a[4].insert(2);
    	a[4].insert(1);
    	a[5].insert(2);
    	char ans[]={'R','O','Y','G','B','V'};
    	cin>>n;
    	int mc[6];
    	for(int i=0;i<6;i++)
    	{
    		cin>>c[i];
    		mc[i]=c[i];
    	}
    	int flag=0;
    	for(int st=0;st<6;st++)
    	{
    		for(int i=0;i<6;i++)
    			c[i]=mc[i];
    		if(!c[st])
    			continue;
    		flag=0;
    		int sz=1;
    		l[0]=st;
    		c[st]--;
    		for(int i=1;i<n;i++)
    		{
    			flag=0;
    			for(int j=0;j<6;j++)
    			{
    				if(!c[j])
    					continue;
    				int pos;
    				for(int k=0;k<sz;k++)
    				{
    					if(a[j].find(l[k])==a[j].end())
    						continue;
    					if(k<sz-1 && a[j].find(l[k+1])==a[j].end())
    						continue;
    					flag=1;
    					pos=k;
    					break;
    				}
    				if(!flag)
    					continue;
    				for(int k=sz-1;k>pos;k--)
    					l[k+1]=l[k];
    				l[pos+1]=j;
    				c[j]--;
    				sz++;
    				break;
    			}
    			if(!flag)
    				break;
    		}
    		if(!flag)
    			continue;
    		if(a[l[n-1]].find(l[0])==a[l[n-1]].end())
    		{
    			flag=0;
    			continue;
    		}
    		break;
    	}
    	if(!flag)
    	{
    		cout<<"IMPOSSIBLE"<<endl;
    		continue;
    	}
    	for(int i=0;i<n;i++)
    		cout<<ans[l[i]];
    	cout<<endl;
    }
    return 0;
}