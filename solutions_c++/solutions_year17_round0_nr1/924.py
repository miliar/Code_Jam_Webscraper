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

ll StringToNumber (string str)
{
	stringstream sstr(str);
	ll val;
	sstr >> val;
	return val;
}

int main()
{
	ll a[N],t,i=0,j,k,x,y,z,count=0,p,flag=0,ans=0,sum=0,l,n,m,max1,min1,pos,tmp,q,t1;
	
	//string s;
	
	scanf("%lld",&t);
	t1=t;
	
	while(t--)
	{
	    
	    string s;

	    cin >> s;
	    cin >> k;

	    l=s.length();
	    ans=0;

	    for(i=0;i<=l-k;i++)
	    {

	    	if(s[i]=='-')
	    	{
	    		for(j=i;j<i+k;j++)
	    		{
	    			if(s[j]=='+')
	    				s[j]='-';
	    			else
	    				s[j]='+';
	    		}
	    		ans++;
	    	}
	    }

	    for(i=l-k+1;i<l;i++)
	    {
	    	if(s[i]=='-')
	    	{
	    		ans=-1;
	    		break;
	    	}
	    }
		
	    if(ans!=-1)
			printf("Case #%lld: %lld\n",t1-t,ans);
		else
			printf("Case #%lld: IMPOSSIBLE\n",t1-t);
		
	}
	
	
	return 0;
}
