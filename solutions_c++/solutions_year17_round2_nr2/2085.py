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
	ll a[N],t,i=0,j,k,x,y,z,count=0,p,flag=0,sum=0,l,n,m,max1,min1,pos,tmp,q,t1,r,o,g,b,v;
	
	//string s;
	
	scanf("%lld",&t);
	t1=t;
	
	while(t--)
	{
		string ans="*";
		scanf("%lld",&n);
	    
	    scanf("%lld%lld%lld%lld%lld%lld",&r,&o,&y,&g,&b,&v);

	    p=max(r,max(y,g));

	    
	    while(n--)
	    {
	    	if(r==b && y==b)
	    	{
	    		if(ans[ans.length()-1]!='R')
	    		{
	    			ans+="R";
	    			r--;
	    		}
	    		else
	    		{
	    			ans+="Y";
	    			y--;
	    		}
	    	}
	    	else if(r==y)
	    	{
	    		if(b>y)
	    		{
	    			if(ans[ans.length()-1]!='B')
	    			{
	    				ans+="B";
	    				b--;
	    			}
	    			else// if(ans.length()>=1 && s[1]!='R')
	    			{
	    				ans+="R";
	    				r--;
	    			}
	    			// else
	    			// {
	    			// 	ans+="Y";
	    			// 	y--;
	    			// }

	    		}
	    		else
	    		{
	    			if(ans[ans.length()-1]!='R')
	    			{
	    				ans+="R";
	    				r--;
	    			}
	    			else
	    			{
	    				ans+="Y";
	    				y--;
	    			}
	    		}
	    	}
	    	else if(r==b)
	    	{
	    		if(y>r)
	    		{
	    			if(ans[ans.length()-1]!='Y')
	    			{
	    				ans+="Y";
	    				y--;
	    			}
	    			else
	    			{
	    				ans+="R";
	    				r--;
	    			}
	    		}
	    		else
	    		{
	    			if(ans[ans.length()-1]!='R')
	    			{
	    				ans+="R";
	    				r--;
	    			}
	    			else
	    			{
	    				ans+="B";
	    				b--;
	    			}
	    		}	
	    	}
	    	else if(y==b)
	    	{
	    		if(r>y)
	    		{
	    			if(ans[ans.length()-1]!='R')
	    			{
	    				ans+="R";
	    				r--;
	    			}
	    			else
	    			{
	    				ans+="Y";
	    				y--;
	    			}
	    		}
	    		else
	    		{
	    			if(ans[ans.length()-1]!='Y')
	    			{
	    				ans+="Y";
	    				y--;
	    			}
	    			else
	    			{
	    				ans+="B";
	    				b--;
	    			}
	    		}	
	    	}
	    	else
	    	{
	    		if(r>b && y>b)
	    		{
	    			if(r>y)
	    			{
		    			if(ans[ans.length()-1]!='R')
		    			{
		    				ans+="R";
		    				r--;
		    			}
		    			else
		    			{
		    				ans+="Y";
		    				y--;
		    			}
	    			}
	    			else
	    			{
		    			if(ans[ans.length()-1]!='Y')
		    			{
		    				ans+="Y";
		    				y--;
		    			}
		    			else
		    			{
		    				ans+="R";
		    				r--;
		    			}
	    			}
	    		}
	    		else if(r>y && b>y)
	    		{
	    			if(r>b)
	    			{
		    			if(ans[ans.length()-1]!='R')
		    			{
		    				ans+="R";
		    				r--;
		    			}
		    			else
		    			{
		    				ans+="B";
		    				b--;
		    			}
	    			}
	    			else
	    			{
		    			if(ans[ans.length()-1]!='B')
		    			{
		    				ans+="B";
		    				b--;
		    			}
		    			else
		    			{
		    				ans+="R";
		    				r--;
		    			}
	    			}
	    		}
	    		else if(b>r && y>r)
	    		{
	    			if(b>y)
	    			{
		    			if(ans[ans.length()-1]!='B')
		    			{
		    				ans+="B";
		    				b--;
		    			}
		    			else
		    			{
		    				ans+="Y";
		    				y--;
		    			}
	    			}
	    			else
	    			{
		    			if(ans[ans.length()-1]!='Y')
		    			{
		    				ans+="Y";
		    				y--;
		    			}
		    			else
		    			{
		    				ans+="B";
		    				b--;
		    			}
	    			}
	    		}

	    	}
	    	//cout << ans << "\n";
	    }

	    p=0;
	    ans=ans.substr(1);
	    for(i=0;i<ans.length();i++)
	    {
	    	if(ans[i]==ans[(i+1)%ans.length()])
	    		p=-1;

	    }

	    if(ans[ans.length()-1]==ans[0])
	    {
	    	if(ans[ans.length()-3]!=ans[0])
	    	{
	    		ans[ans.length()-1]=ans[ans.length()-2];
	    		ans[ans.length()-2]=ans[0];
	    		p=0;
	    	}
	    }

	    if(p==-1 || !(r==0 && y==0 && b==0))
	    	printf("Case #%lld: IMPOSSIBLE\n",t1-t);
	    else
		{
		
			printf("Case #%lld: ",t1-t);
			cout << ans << "\n";
		}

		
	}
	
	
	return 0;
}