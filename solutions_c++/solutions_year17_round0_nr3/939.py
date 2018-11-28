/*
    
    Jaydeep Khandelwal,
    CSE 3rd year,
    MNNIT Allahabad
    
    Kathumar, Alwar, Rajsthan.
    
*/
//For taking input line with spaces: getline(cin,s[i]);


#include<bits/stdc++.h>
using namespace std;

//Constants:
#define mod 1000000007
#define INF 1000000000
#define INFL 1000000000000000000
#define N 100005
#define PI (2.0*acos(0.0))

//Shortcuts:
#define ll long long
#define vec vector<ll>
#define matrix vector<vector<ll> >
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define sn struct node
#define sf1(a) scanf("%lld",&a);
#define sf2(a,b) scanf("%lld%lld",&a,&b);
#define sf3(a,b,c) scanf("%lld%lld%lld",&a,&b,&c);
#define pf1(a) printf("%lld\n",a);
#define pf2(a,b) printf("%lld %lld\n",a,b);
#define pf3(a,b,c) printf("%lld %lld %lld\n",a,b,c);
#define ffor(a,b) for(i=a;i<=b;i++)
#define rfor(a,b) for(i=a;i>=b;i--)

//Mistakes:
#define pritnf printf


int main()
{
	ll a[N],t,i=0,j,k,x,y,z,count=0,p,flag=0,ans=0,sum=0,l,n,m,max1,min1,pos,tmp,q,pp,qq,ans1,ans2;
	
	//string s;
	
	scanf("%lld",&t);
	ll t1=t;
	
	while(t--)
	{
	    scanf("%lld%lld",&n,&k);
	    
	    p=n;
	    q=n-1;
	    pp=1;
	    qq=0;
	    ans=0;
	    for(i=1;1;i*=2)
	    {
	    	if(k==1)
	    		break;
	    	x=p-1;
	    	
	    	if(x%2==0)
	    	{
	    		p=x/2;
	    		pp=pp*2;

	    		pp+=qq;
	    		qq=qq;


	    	}
	    	else
	    	{
	    		p=x/2+1;

	    		qq=qq*2;

	    		qq+=pp;
	    		pp=pp;


	    	}

	    	//printf("%lld %lld, %lld %lld\n",p,pp,p-1,qq);

	    	ans+=i;

	    	if(ans+2*i>=k)
	    		break;

	    }
	    
	    i=2*i;
	    if(k-ans<=pp)
	    {
	    	x=p-1;
	    	
	    	if(x%2==0)
	    	{
	    		ans1=x/2;
	    		ans2=x/2;
	    	}
	    	else
	    	{
	    		ans1=x/2+1;
	    		ans2=x/2;

	    	}

	    }
	    else
	    {
			x=p-2;
	    	
	    	if(x%2==0)
	    	{
	    		ans1=x/2;
	    		ans2=x/2;
	    	}
	    	else
	    	{
	    		ans1=x/2+1;
	    		ans2=x/2;

	    	}	    	


	    }
	    
	    
	    
	    
	    
	    
	    
	    
	    
		printf("Case #%lld: %lld %lld\n",t1-t,ans1,ans2);
		
	}
	
	
	return 0;
}
