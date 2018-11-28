#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define ll long long
#define N 100005
#define S(x) scanf("%d",&x)
#define S2(x,y) scanf("%d%d",&x,&y)
#define wl(n) while(n--)
#define PB push_back
#define MP make_pair
#define P(x) printf("%d\n",x)
#define fl(i,n) for(i=0;i<n;i++)
#define fil(i,a,n) for(i=a;i<n;i++)
#define rev(i,a,n) for(i=n-1;i>=a;i--)

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    ll t,tmp;
    cin>>t;
    tmp=1;
    while(t--)
    {
    	ll n,arr[1010];
    	string s;
    	cin>>s;
    	cin>>n;

    	//cout<<"string="<<s<<"n="<<n<<endl;
    	ll i,sz;
    	sz=s.length();
    	for(i=0;i<sz;i++)
    	{
    		if(s[i]=='+')
    			arr[i]=1;
    		else if(s[i]=='-')
    			arr[i]=0;
    		//cout<<"s=="<<s[i]<<"arr="<<arr[i]<<endl;
    	}

    		/*	cout<<"array:"<<endl;
    			ll k;
    			for(k=0;k<sz;k++)
    				cout<<arr[k]<<" ";
    			cout<<endl;
			*/

    	ll flag=1,steps=0;
    	for(i=0;i<sz;i++)
    	{
    		if(arr[i]==0)
    		{
    			steps++;
    			//flip n nos ahead
    			ll j=i,cnt=0;
    			if(j+n-1<sz)
    			{	
    				while(j<sz && cnt<n)
    				{
    					//flip
    					arr[j]=(arr[j]+1)%2;
    					j++;
    					cnt++;
    				}
    			}	
    			/*
    			cout<<"Updated array:"<<endl;
    			ll k;
    			for(k=0;k<sz;k++)
    				cout<<arr[k]<<" ";
    			cout<<endl;
    		*/
    			
    		}
    	}

    	for(i=0;i<sz;i++)
    		if(arr[i]==0)
    			flag=0;

    	if(flag)
    		cout<<"Case #"<<tmp<<": "<<steps<<endl;
    	else
    		cout<<"Case #"<<tmp<<": "<<"IMPOSSIBLE"<<endl;

    	tmp+=1;			

    }

	return 0;
} 